from __future__ import annotations

NODE_ORDER = [
    "UC Makassar",
    "Kaizen",
    "Gyu Kaku",
    "CPI",
    "Upperhills",
    "Shabuhachi",
    "Shaburi & Kintan",
    "RM Bahari",
    "Akira Dragon",
    "Yottai Sungai Saddang",
    "Novotel",
    "Karebosi Premier",
    "Pasar Kalimbu",
    "Gembira Motor",
    "Phipo",
    "Dinas Bina Marga",
    "Momoyo",
    "Nasi Kuning Riburane",
    "Mall Panakukkang",
    "Lion Air Service Office",
    "Bintang",
    "Kaya Rempah",
    "Lapangan Tenis Pascasarjana",
    "Apotek Sejati Farma",
    "AUCE Kongkow",
    "Satu Sama Jaya Abadi",
    "Kopi Setia",
    "Coto Gagak",
    "Bank Sinarmas",
    "Nasgor Mas Akmal",
    "Hae Don",
]

GRAPH: dict[str, list[tuple[str, float]]] = {
    "UC Makassar": [
        ("Kaizen", 0.4),
        ("Gyu Kaku", 0.5),
        ("CPI", 1.7),
    ],
    "Kaizen": [
        ("UC Makassar", 0.4),
        ("CPI", 1.3),
        ("Gyu Kaku", 0.6),
    ],
    "Gyu Kaku": [
        ("UC Makassar", 0.5),
        ("CPI", 0.6),
        ("Kaizen", 0.6),
    ],
    "CPI": [
        ("RM Bahari", 0.8),
        ("Nasgor Mas Akmal", 0.85),
        ("Bank Sinarmas", 0.7),
    ],
    "Upperhills": [
        ("Shabuhachi", 1.5),
        ("Shaburi & Kintan", 1.2),
        ("Phipo", 1.0),
    ],
    "Shabuhachi": [
        ("Upperhills", 1.5),
    ],
    "Shaburi & Kintan": [
        ("Upperhills", 1.2),
    ],
    "RM Bahari": [
        ("Akira Dragon", 0.55),
        ("Yottai Sungai Saddang", 0.95),
    ],
    "Akira Dragon": [
        ("RM Bahari", 0.55),
        ("Bank Sinarmas", 0.25),
    ],
    "Yottai Sungai Saddang": [
        ("Novotel", 1.0),
        ("Gembira Motor", 1.4),
        ("Kopi Setia", 1.1),
    ],
    "Novotel": [
        ("Karebosi Premier", 0.8),
        ("Hae Don", 1.3),
        ("Pasar Kalimbu", 1.3),
    ],
    "Karebosi Premier": [
        ("Novotel", 0.8),
        ("Hae Don", 0.85),
        ("Pasar Kalimbu", 1.2),
    ],
    "Pasar Kalimbu": [
        ("Novotel", 1.3),
        ("Hae Don", 0.55),
        ("Gembira Motor", 0.55),
    ],
    "Gembira Motor": [
        ("Apotek Sejati Farma", 2.1),
        ("Kopi Setia", 1.3),
        ("Pasar Kalimbu", 0.55),
    ],
    "Phipo": [
        ("CPI", 1.3),
        ("Upperhills", 1.0),
    ],
    "Dinas Bina Marga": [
        ("Lion Air Service Office", 1.3),
        ("Kopi Setia", 1.3),
    ],
    "Momoyo": [
        ("Novotel", 1.2),
        ("Nasi Kuning Riburane", 1.2),
    ],
    "Nasi Kuning Riburane": [
        ("Karebosi Premier", 0.95),
        ("Momoyo", 1.2),
    ],
    "Mall Panakukkang": [
        ("Lion Air Service Office", 1.0),
        ("Bintang", 1.0),
        ("Kaya Rempah", 1.4),
    ],
    "Lion Air Service Office": [
        ("Bintang", 1.0),
        ("Mall Panakukkang", 1.0),
        ("Apotek Sejati Farma", 1.8),
    ],
    "Bintang": [
        ("Mall Panakukkang", 1.0),
        ("Lion Air Service Office", 1.0),
        ("Kaya Rempah", 1.0),
        ("Apotek Sejati Farma", 1.9),
    ],
    "Kaya Rempah": [
        ("Mall Panakukkang", 1.4),
        ("Bintang", 1.0),
        ("Lapangan Tenis Pascasarjana", 1.7),
        ("Apotek Sejati Farma", 1.9),
    ],
    "Lapangan Tenis Pascasarjana": [
        ("Kaya Rempah", 1.7),
        ("Apotek Sejati Farma", 2.2),
        ("AUCE Kongkow", 1.2),
    ],
    "Apotek Sejati Farma": [
        ("Lion Air Service Office", 1.8),
        ("Bintang", 2.1),
        ("Kaya Rempah", 1.9),
        ("Lapangan Tenis Pascasarjana", 2.2),
        ("AUCE Kongkow", 1.7),
        ("Kopi Setia", 1.4),
        ("Satu Sama Jaya Abadi", 2.3),
    ],
    "AUCE Kongkow": [
        ("Satu Sama Jaya Abadi", 1.1),
        ("Lapangan Tenis Pascasarjana", 1.2),
        ("Apotek Sejati Farma", 1.7),
    ],
    "Satu Sama Jaya Abadi": [
        ("AUCE Kongkow", 1.1),
        ("Apotek Sejati Farma", 2.3),
        ("Coto Gagak", 1.5),
    ],
    "Kopi Setia": [
        ("Apotek Sejati Farma", 1.4),
        ("Yottai Sungai Saddang", 1.1),
        ("Gembira Motor", 1.3),
    ],
    "Coto Gagak": [
        ("Satu Sama Jaya Abadi", 0.9),
        ("Nasgor Mas Akmal", 0.85),
        ("Upperhills", 2.9),
    ],
    "Bank Sinarmas": [
        ("Akira Dragon", 1.6),
        ("Nasgor Mas Akmal", 0.8),
        ("RM Bahari", 1.7),
        ("Yottai Sungai Saddang", 2.3),
    ],
    "Nasgor Mas Akmal": [
        ("Coto Gagak", 0.85),
        ("Bank Sinarmas", 0.8),
        ("CPI", 0.85),
    ],
    "Hae Don": [
        ("Pasar Kalimbu", 0.55),
        ("Gembira Motor", 1.0),
        ("Karebosi Premier", 0.85),
        ("Novotel", 1.3),
    ],
}

STARTING_POINTS = [
    "UC Makassar",
    "Mall Panakukkang",
    "Mall Pipo",
]
START_NODE_BY_LABEL = {
    "UC Makassar": "UC Makassar",
    "Mall Panakukkang": "Mall Panakukkang",
    "Mall Pipo": "Phipo",
}

GOAL_DISPLAY_NAMES = {
    "Shabuhachi": "Shabuhachi",
    "Kaizen": "Kaizen",
    "Gyu Kaku": "Gyukaku",
    "Akira Dragon": "Akira Grill (Akira Dragon)",
    "Hae Don": "Hae Don",
    "Shaburi & Kintan": "Shaburi",
    "AUCE Kongkow": "AUCE Kongkow",
}
GOAL_NODES = set(GOAL_DISPLAY_NAMES)

NAME_ALIASES = {
    "UC Makassar": ["UC Makassar", "UC makassar"],
    "Kaizen": ["Kaizen"],
    "Gyu Kaku": ["Gyu Kaku", "Gyukaku", "Gyu-kaku", "gyu kaku"],
    "CPI": ["CPI"],
    "Upperhills": ["Upperhills", "Upper Hills"],
    "Shabuhachi": ["Shabuhachi", "Shabuhaci"],
    "Shaburi & Kintan": ["Shaburi", "Shaburi & Kintan", "Shaburi Kintan"],
    "RM Bahari": ["RM Bahari", "R.M. Bahari"],
    "Akira Dragon": ["Akira Dragon", "Akira Grill", "Akira Grill (Akira Dragon)"],
    "Yottai Sungai Saddang": [
        "Yottai Sungai Saddang",
        "Yotta Sungai Saddang",
        "Yottai Sungai Sadang",
    ],
    "Novotel": ["Novotel"],
    "Karebosi Premier": ["Karebosi Premier"],
    "Pasar Kalimbu": ["Pasar Kalimbu"],
    "Gembira Motor": ["Gembira Motor"],
    "Phipo": ["Phipo", "Mall Pipo", "Mall Phipo"],
    "Dinas Bina Marga": ["Dinas Bina Marga"],
    "Momoyo": ["Momoyo"],
    "Nasi Kuning Riburane": ["Nasi Kuning Riburane"],
    "Mall Panakukkang": ["Mall Panakukkang", "Mall Panakkukang"],
    "Lion Air Service Office": ["Lion Air Service Office", "Lion Air Office"],
    "Bintang": ["Bintang"],
    "Kaya Rempah": ["Kaya Rempah"],
    "Lapangan Tenis Pascasarjana": ["Lapangan Tenis Pascasarjana"],
    "Apotek Sejati Farma": [
        "Apotek Sejati Farma",
        "Apotek Setia Farma",
        "Apotek Sejati",
    ],
    "AUCE Kongkow": ["AUCE Kongkow", "AUCE Kongkow"],
    "Satu Sama Jaya Abadi": ["Satu Sama Jaya Abadi"],
    "Kopi Setia": ["Kopi Setia"],
    "Coto Gagak": ["Coto Gagak"],
    "Bank Sinarmas": [
        "Bank Sinarmas",
        "ATM Bank Sinarmas",
        "ATM Bank Sinarmas KC Manggis",
    ],
    "Nasgor Mas Akmal": [
        "Nasgor Mas Akmal",
        "Nasi Goreng Mas Aksal",
        "Nasi Goreng Mas Akmal",
    ],
    "Hae Don": ["Hae Don"],
}


def _name_key(name: str) -> str:
    """Kunci normalisasi nama: huruf kecil dan hanya huruf/angka."""
    return "".join(ch.casefold() for ch in name if ch.isalnum())


ALIAS_LOOKUP: dict[str, str] = {}
for canonical, aliases in NAME_ALIASES.items():
    ALIAS_LOOKUP[_name_key(canonical)] = canonical
    for alias in aliases:
        ALIAS_LOOKUP[_name_key(alias)] = canonical


def canonicalize_name(name: str) -> str | None:
    """Mengubah variasi nama menjadi nama node standar; None jika tidak dikenal."""
    return ALIAS_LOOKUP.get(_name_key(name.strip()))


def format_neighbors(node: str) -> str:
    """Format daftar tetangga untuk tabel GUI."""
    neighbors = GRAPH.get(node, [])
    if not neighbors:
        return "Belum ada bobot tetangga di sumber"
    return "; ".join(f"{target} ({weight:g} km)" for target, weight in neighbors)
