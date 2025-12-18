# core/domain_lexicon_gold.py
# Canonical, deduplicated, production-ready gold lexicons
# All entries are lowercase and alphabetically sorted

# -----------------
# ACTIONS
# -----------------
ACTIONS = {
    "afblænding",
    "afhentning",
    "afmelding",
    "afprøvet",
    "bestilling",
    "demontering",
    "færdiggørelse",
    "fejlfinding",
    "fejlsøgning",
    "frakobling",
    "genstart",
    "gennemgang",
    "indkobling",
    "indstilling",
    "installation",
    "kontrol",
    "levering",
    "måling",
    "montering",
    "nulstilling",
    "opstart",
    "programmering",
    "reparation",
    "rensning",
    "rengøring",
    "tilkobling",
    "tilslutning",
    "udskiftning",
}

# -----------------
# OBJECTS
# -----------------
OBJECTS = {
    "afbryder",
    "armatur",
    "brugsgenstand",
    "display",
    "gang",
    "gruppe",
    "installation",
    "kabel",
    "komfur",
    "kogeplade",
    "kontakt",
    "køleanlæg",
    "ladekabel",
    "lampe",
    "ledning",
    "motor",
    "nødlys",
    "ovn",
    "pumpe",
    "relæ",
    "røgalarm",
    "samledåse",
    "sensor",
    "sikring",
    "spot",
    "stikkontakt",
    "styring",
    "tavle",
    "udgangsskilt",
    "udstyr",
    "varmepumpe",
    "ventilator",
}

# -----------------
# LOCATIONS
# -----------------
LOCATIONS = {
    "badeværelse",
    "butik",
    "garage",
    "gang",
    "hal",
    "kælder",
    "kontor",
    "køkken",
    "ladestander",
    "lager",
    "loft",
    "maskinrum",
    "opgang",
    "stue",
    "tag",
    "toilet",
    "udendørs",
    "udvendig",
    "værksted",
    "værelse",
}


LOCATION_PREPOSITIONS = {
    "badeværelse": "på",
    "butik": "i",
    "garage": "i",
    "gang": "i",
    "hal": "i",
    "kælder": "i",
    "kontor": "på", 
    "køkken": "i",
    "ladestander": "på",
    "lager": "på",
    "loft": "på",
    "maskinrum": "i",
    "opgang": "i",
    "stue": "i",
    "tag": "på",
    "toilet": "på",
    "udendørs": "",
    "udvendig": "",
    "værksted": "på",
    "værelse": "i",
}


# -----------------
# PRODUCTS (fallback only)
# -----------------
PRODUCTS = {
    "carrier",
    "daikin",
    "danfoss",
    "duka",
    "hpfi",
    "ihc",
    "indedel",
    "lg",
    "mitsubishi",
    "panasonic",
    "plc",
    "rcd",
    "samsung", 
    "siemens",
    "sony",
    "samsung",
    "shucko",   
    "udedel",
}

# -----------------
# UNITS
# -----------------
UNITS = {
    "m2", 
    "m3", 
    "g", 
    "kg", 
    "cm",
    "dm",
    "mm",  
    "m", 
    "l",
    "ml",
    "dl",
    "C°",
    "stk",
}
