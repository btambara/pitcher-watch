from fastapi import APIRouter
from player.routers import pitches_endpoints, players_endpoints, stats_endpoints

player_router = APIRouter()
player_router.include_router(
    players_endpoints.router, prefix="/players", tags=["players"]
)
player_router.include_router(
    stats_endpoints.router, prefix="/player/stats", tags=["stats"]
)
player_router.include_router(
    pitches_endpoints.router, prefix="/player/pitches", tags=["pitches"]
)
