from typing import Protocol, List
import json
from pathlib import Path

from src.domain.poem_types import Poem


class PoemRepository(Protocol):
    """Contract / interface pour un repository de poèmes.

    Ne contient pas d'implémentation. Les méthodes sont définies pour être
    implémentées plus tard (JSON, DB, etc.).
    """

    async def list_poems(self) -> List[Poem]:
        """Retourne la liste complète des poèmes disponibles."""

    async def get_random_poem(self) -> Poem:
        """Retourne un poème aléatoire."""


def load_poems(path: str = "data/poemes.json") -> List[Poem]:
    """Charge et valide la liste des poèmes depuis un fichier JSON local.

    Retourne une liste de `Poem` validés par Pydantic.

    Lève FileNotFoundError si le fichier est absent, ou ValueError si le contenu
    est invalide.
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"Poems file not found: {path}")

    try:
        with p.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except Exception as exc:
        raise ValueError(f"Failed to read or parse JSON from {path}: {exc}")

    if not isinstance(data, list):
        raise ValueError("Poems JSON must be a list")

    poems: List[Poem] = []
    for idx, item in enumerate(data):
        try:
            poem = Poem.parse_obj(item)
            poems.append(poem)
        except Exception as exc:
            raise ValueError(f"Invalid poem at index {idx}: {exc}")

    return poems
