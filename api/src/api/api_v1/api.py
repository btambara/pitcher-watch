from fastapi import APIRouter
from player.routers import players_endpoints

player_router = APIRouter()
player_router.include_router(
    players_endpoints.router, prefix="/players", tags=["players"]
)
