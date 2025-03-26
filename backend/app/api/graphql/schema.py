import strawberry
from typing import List, Optional
from datetime import datetime

@strawberry.type
class Song:
    id: str
    name: str
    artist: str
    release_date: Optional[datetime]
    spotify_id: Optional[str]
    created_at: datetime
    updated_at: datetime
    related_songs: List["Song"]
    upworm_count: int

@strawberry.type
class Query:
    @strawberry.field
    async def get_song(self, id: str) -> Optional[Song]:
        # TODO: Implement Neo4j query
        pass

    @strawberry.field
    async def search_songs(self, query: str) -> List[Song]:
        # TODO: Implement Neo4j query
        pass

    @strawberry.field
    async def get_related_songs(self, song_id: str) -> List[Song]:
        # TODO: Implement Neo4j query
        pass

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def add_upworm(self, from_song_id: str, to_song_id: str) -> bool:
        # TODO: Implement Neo4j mutation
        pass

    @strawberry.mutation
    async def add_song(self, name: str, artist: str) -> Song:
        # TODO: Implement Neo4j mutation
        pass

schema = strawberry.Schema(query=Query, mutation=Mutation) 