# Text Normalization Pipeline — Architecture (v1)

## Status

**Frozen architecture, production-grade.**
This document is the authoritative technical specification for the Danish text normalization pipeline.

---

## 1. Objective

Normalize Danish technical free text into **deterministic, canonical sentences** aligned with `large_training_text.txt`.

The system must:

* eliminate ambiguity
* be human-auditable
* avoid heuristic or probabilistic NLP
* scale via explicit artifacts (lexicons, maps, rules)

---

## 2. Non‑Negotiable Invariants

### 2.1 Gold Lexicons Define Meaning Space

All semantic meaning originates from **gold lexicons**:

* `ACTIONS`
* `OBJECTS`
* `LOCATIONS`
* `PRODUCTS`

Lexicons may overlap. Overlap is intentional and resolved structurally.

---

### 2.2 Role Exclusivity (Hard Constraint)

A token may be assigned **exactly one semantic role per sentence**.

Enforced via a **claimed-token registry** shared across all extractors.

---

### 2.3 Priority Order (Global)

```
ACTION → LOCATION → OBJECT → PRODUCT
```

If a token appears in multiple lexicons, the first extractor in this order that claims it wins.

---

### 2.4 No Heuristics

The pipeline must not contain:

* statistical inference
* confidence thresholds
* fallback guessing

All behavior must be traceable to:

* gold lexicons
* normalization maps
* extractors
* formatter rules

---

## 3. Pipeline (Final Order)

```
raw text
 → spell correction
 → abbreviation expansion
 → lemmatization
 → role extraction
 → sentence realization
```

**Surface-form logic must occur before lemmatization.**

---

## 4. Components

### 4.1 Spell Correction

**Purpose:** Correct misspellings conservatively toward known domain vocabulary.

**Rules:**

* Only correct to tokens present in gold lexicons or normalization maps
* Deterministic
* No novel token generation

---

### 4.2 Abbreviation Expansion (Actions)

**Purpose:** Expand abbreviated action tokens.

**Mechanism:**

* Prefix-match against `ACTIONS`
* Expand only if the match is unique
* Executed **before lemmatization**

**Examples:**

```
inst → installation
mont → montering
```

---

### 4.3 Lemmatization

Standard Danish lemmatization applied after surface normalization.

---

### 4.4 Claimed Token Registry

**Purpose:** Enforce role exclusivity and priority.

**Interface:**

```python
registry.claim(token, role)
registry.is_claimed(token)
```

**Properties:**

* Global per sentence
* Queried by all extractors

---

### 4.5 Extractor Suite

Each extractor:

1. Normalizes token
2. Checks its gold lexicon
3. Checks registry
4. Claims token if available
5. Appends to role list

**Extractors return:**

```python
actions:   List[str]
objects:   List[str]
locations: List[str]
products:  List[str]
```

**Properties:**

* Order-preserving
* Duplicate-safe
* Multi-value capable
* Polysemy-safe

---

### 4.6 Sentence Realization

**Approach:** Declarative glue rules.

**Canonical Pattern:**

```
<actions> af <objects> i <locations>. afprøvet.
```

Supports multiple values in each role.

---

### 4.7 Special Disambiguation Rule

If:

* the only action is `afprøvet`
* objects exist

Then output:

```
<object> afprøvet.
```

Prevents empty or ambiguous sentences.

---

## 5. End‑to‑End Example

**Input:**

```
inst 2 lampr i køken
```

**Output:**

```
installation af lampe i køkken. afprøvet.
```

---

## 6. Design Principle (Summary)

> Lexicons define possible meanings.
> Extractors assign roles.
> Registry enforces exclusivity.
> Formatter removes ambiguity.

---

## 7. Extension Policy

Allowed extensions:

* add lexicon entries
* add normalization mappings
* add extractors (with registry compliance)
* add formatter glue rules

Forbidden extensions:

* heuristics
* probabilistic logic
* extractor-local disambiguation

---

**This document defines v1. Any change requires explicit revision.**
