from fastapi import APIRouter
from player.routers import players_endpoints, stats_endpoints

player_router = APIRouter()
player_router.include_router(
    players_endpoints.router, prefix="/players", tags=["players"]
)
player_router.include_router(
    stats_endpoints.router, prefix="/player/stats", tags=["stats"]
)

