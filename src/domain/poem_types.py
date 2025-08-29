from typing import List
from pydantic import BaseModel


class Poem(BaseModel):
    """Domain model for a poem (types only).

    Champs requis et validés par Pydantic. Aucune logique / I/O ici.
    """
    id: int
    titre: str
    auteur: str
    contenu: str
    tags: List[str] = []


class PoemResponse(BaseModel):
    """Response schema wrapping a single poem."""
    poem: Poem
