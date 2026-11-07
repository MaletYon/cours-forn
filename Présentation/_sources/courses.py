"""Métadonnées du cours FORN (LPI342, Université de Garoua) et répartition des
15 séances de 2 heures (30 heures)."""

COURS = r"C:\Users\Thierry MINKA\OneDrive\Documents\COURS"

FORN = {
    "sigle": "FORN",
    "code": "LPI342",
    "titre": "Forensique Numérique",
    "sous_titre": "De la scène numérique à la preuve opposable devant le juge",
    "master": "Master Professionnel en Sécurité des Systèmes Informatiques et des Données",
    "bandeau": "Université de Garoua",
    "ecole": "Faculté des Sciences",
    "logo_g": "garoua",
    "logo_d": "garoua",
    "n_jours": 15,
    "annee": "2026-2027",
    "dossier": COURS + r"\UG-DMI\LPI342\Présentation",
    "fil_rouge": "Opération TSANAGA",
    "parties": [
        ("Prologue", "La scène numérique", "P00"),
        ("Partie I", "Fondements du forensique", "C01-C03"),
        ("Partie II", "Cadre juridique et recevabilité", "C04-C06"),
        ("Partie III", "Acquisition des preuves", "C07-C09"),
        ("Partie IV", "L'analyse par domaine", "C10-C15"),
        ("Partie V", "Les défis de l'enquête", "C16-C17"),
        ("Partie VI", "Restituer l'enquête", "C18-C20"),
    ],
    # jour : (thème court, contenu détaillé, ateliers/chapitres, labs)
    "jours": {
        1: ("Ouverture · La scène numérique", "Présentation du cours + Prologue", ["P00"], []),
        2: ("Qu'est-ce que la forensique numérique", "C01", ["C01"], []),
        3: ("La démarche d'enquête · Éthique et impartialité", "C02 + C03", ["C02", "C03"], []),
        4: ("Le droit de la preuve · La chaîne de possession", "C04 + C05", ["C04", "C05"], ["LAB-01"]),
        5: ("Recevabilité et admissibilité", "C06", ["C06"], ["LAB-08"]),
        6: ("Identifier et préserver les sources", "C07", ["C07"], []),
        7: ("Duplication et hachage", "C08", ["C08"], ["LAB-02"]),
        8: ("Ordre de volatilité et acquisition à chaud", "C09", ["C09"], []),
        9: ("Forensique disque et systèmes de fichiers", "C10", ["C10"], ["LAB-03"]),
        10: ("Fichiers supprimés, fragments et artefacts", "C11", ["C11"], ["LAB-04"]),
        11: ("Forensique mémoire", "C12", ["C12"], ["LAB-05"]),
        12: ("Forensique réseau · Forensique mobile", "C13 + C14", ["C13", "C14"], ["LAB-06", "LAB-07"]),
        13: ("Forensique du nuage · Anti-forensique et chiffrement", "C15 + C16", ["C15", "C16"], []),
        14: ("Reconstitution chronologique · Le rapport forensique", "C17 + C18", ["C17", "C18"], ["LAB-09", "LAB-10"]),
        15: ("Devant le tribunal · Mesurer et progresser · clôture", "C19 + C20", ["C19", "C20"], []),
    },
}

ALL = {"FORN": FORN}
