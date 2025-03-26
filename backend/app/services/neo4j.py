from neo4j import GraphDatabase
from typing import List, Dict, Any
import os
from datetime import datetime

class Neo4jService:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI", "bolt://localhost:7687"),
            auth=(os.getenv("NEO4J_USER", "neo4j"), 
                  os.getenv("NEO4J_PASSWORD", "ohrwurm123"))
        )

    def close(self):
        self.driver.close()

    def get_song(self, song_id: str) -> Dict[str, Any]:
        with self.driver.session() as session:
            result = session.run("""
                MATCH (s:Song {id: $song_id})
                RETURN s
            """, song_id=song_id)
            record = result.single()
            return dict(record["s"]) if record else None

    def search_songs(self, query: str) -> List[Dict[str, Any]]:
        with self.driver.session() as session:
            result = session.run("""
                MATCH (s:Song)
                WHERE s.name CONTAINS $query OR s.artist CONTAINS $query
                RETURN s
                LIMIT 10
            """, query=query)
            return [dict(record["s"]) for record in result]

    def get_related_songs(self, song_id: str) -> List[Dict[str, Any]]:
        with self.driver.session() as session:
            result = session.run("""
                MATCH (s:Song {id: $song_id})
                MATCH (s)-[r:UPWORM]->(related:Song)
                RETURN related, count(r) as upworm_count
                ORDER BY upworm_count DESC
                LIMIT 10
            """, song_id=song_id)
            return [dict(record["related"]) for record in result]

    def add_upworm(self, from_song_id: str, to_song_id: str) -> bool:
        with self.driver.session() as session:
            try:
                session.run("""
                    MATCH (s1:Song {id: $from_id})
                    MATCH (s2:Song {id: $to_id})
                    MERGE (s1)-[r:UPWORM]->(s2)
                    ON CREATE SET r.created_at = datetime()
                """, from_id=from_song_id, to_id=to_song_id)
                return True
            except Exception:
                return False

    def add_song(self, name: str, artist: str) -> Dict[str, Any]:
        with self.driver.session() as session:
            result = session.run("""
                CREATE (s:Song {
                    id: randomUUID(),
                    name: $name,
                    artist: $artist,
                    created_at: datetime(),
                    updated_at: datetime()
                })
                RETURN s
            """, name=name, artist=artist)
            return dict(result.single()["s"]) 