from fastapi import FastAPI, HTTPException
from random import choice

from src.services.poem_repo import load_poems
from src.domain.poem_types import PoemResponse


# Application FastAPI minimal
app = FastAPI(title="Poèmes API", version="0.1.0")


@app.get("/poemes/random", response_model=PoemResponse)
async def get_random_poem():
    """
    TODO: implémenter cet endpoint lors de la phase d'implémentation.
    Critères d'acceptation: retourne un objet correspondant à PoemResponse.
    Ne pas ajouter de logique ici — ce fichier est un squelette.
    """
    try:
        poems = load_poems()
    except FileNotFoundError as exc:
        raise HTTPException(status_code=500, detail=str(exc))
    except ValueError as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    if not poems:
        raise HTTPException(status_code=500, detail="No poems available")

    selected = choice(poems)
    return PoemResponse(poem=selected)
