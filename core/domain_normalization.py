# core/domain_normalization.py
# Surface-form → canonical mappings (alphabetically ordered)

# -----------------
# ACTION NORMALIZATION
# -----------------
NORMALIZE_ACTION = {
    "afprøve": "afprøvet",
    "afprøvet": "afprøvet",
    "frakoblet": "frakobling",
    "fejlfinding": "fejlfinding",
    "fejlsøge": "fejlsøgning",
    "genstarte": "genstart",
    "indkoble": "indkobling",
    "installere": "installation",
    "installer": "installation",
    "installeret": "installation",
    "montere": "montering",
    "monteret": "montering",
    "nulstille": "nulstilling",
    "opstarte": "opstart",
    "opsætte": "montering",
    "opsat": "montering",
    "reparere": "reparation",
    "rengøre": "rengøring",
    "rense": "rensning",
    "skifte": "udskiftning",
    "teste": "afprøvet",
    "testet": "afprøvet",
    "tilkoble": "tilkobling",
    "tilslutte": "tilslutning",
    "udskifte": "udskiftning",
    "udskiftet": "udskiftning",
}

# -----------------
# OBJECT NORMALIZATION
# -----------------
NORMALIZE_OBJECT = {
    "afbrydere": "afbryder",
    "armaturer": "armatur",
    "hfi-relæ": "hpfi",
    "hpfi-relæ": "hpfi",
    "kabler": "kabel",
    "kontakter": "kontakt",
    "lamper": "lampe",
    "ledninger": "ledning",
    "relæer": "relæ",
    "sikringer": "sikring",
    "spots": "spot",
    "stikkontakter": "stikkontakt",
}

# -----------------
# LOCATION NORMALIZATION
# -----------------
NORMALIZE_LOCATION = {
    "bad": "badeværelse",
    "kælderen": "kælder",
    "loftet": "loft",
    "udvendigt": "udvendig",
    "wc": "toilet",
}

# -----------------
# PRODUCT NORMALIZATION
# -----------------
NORMALIZE_PRODUCT = {
    "hfi": "hpfi",
    "hfi-relæ": "hpfi",
    "hpfi-relæ": "hpfi",
}
