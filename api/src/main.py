from api.api_v1.api import player_router
from fastapi import FastAPI

app = FastAPI()
app.include_router(player_router, prefix="/api/v1")
