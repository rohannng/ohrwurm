from app.services.neo4j import Neo4jService
from app.services.postgres import PostgresService
from typing import List, Optional
from datetime import datetime

neo4j_service = Neo4jService()
postgres_service = PostgresService()

async def get_song_resolver(id: str) -> Optional[dict]:
    return neo4j_service.get_song(id)

async def search_songs_resolver(query: str) -> List[dict]:
    return neo4j_service.search_songs(query)

async def get_related_songs_resolver(song_id: str) -> List[dict]:
    return neo4j_service.get_related_songs(song_id)

async def add_upworm_resolver(from_song_id: str, to_song_id: str) -> bool:
    return neo4j_service.add_upworm(from_song_id, to_song_id)

async def add_song_resolver(name: str, artist: str) -> dict:
    return neo4j_service.add_song(name, artist) 