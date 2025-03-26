import pytest
from app.services.neo4j import Neo4jService

def test_create_song(neo4j_session):
    service = Neo4jService(neo4j_session)
    
    # Test data
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "year": 2024,
        "genre": "Test Genre"
    }
    
    # Create song
    song = service.create_song(song_data)
    
    # Verify song was created
    assert song["title"] == song_data["title"]
    assert song["artist"] == song_data["artist"]
    assert song["album"] == song_data["album"]
    assert song["year"] == song_data["year"]
    assert song["genre"] == song_data["genre"]

def test_get_song_by_id(neo4j_session):
    service = Neo4jService(neo4j_session)
    
    # Create test song
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "year": 2024,
        "genre": "Test Genre"
    }
    created_song = service.create_song(song_data)
    
    # Get song by ID
    song = service.get_song_by_id(created_song["id"])
    
    # Verify song was retrieved
    assert song["id"] == created_song["id"]
    assert song["title"] == song_data["title"]
    assert song["artist"] == song_data["artist"]

def test_get_similar_songs(neo4j_session):
    service = Neo4jService(neo4j_session)
    
    # Create test songs
    song1 = service.create_song({
        "title": "Song 1",
        "artist": "Artist 1",
        "album": "Album 1",
        "year": 2024,
        "genre": "Rock"
    })
    
    song2 = service.create_song({
        "title": "Song 2",
        "artist": "Artist 2",
        "album": "Album 2",
        "year": 2024,
        "genre": "Rock"
    })
    
    # Create similarity relationship
    service.create_similarity(song1["id"], song2["id"], 0.8)
    
    # Get similar songs
    similar_songs = service.get_similar_songs(song1["id"])
    
    # Verify similar songs were retrieved
    assert len(similar_songs) == 1
    assert similar_songs[0]["id"] == song2["id"]
    assert similar_songs[0]["similarity"] == 0.8

def test_create_similarity(neo4j_session):
    service = Neo4jService(neo4j_session)
    
    # Create test songs
    song1 = service.create_song({
        "title": "Song 1",
        "artist": "Artist 1",
        "album": "Album 1",
        "year": 2024,
        "genre": "Rock"
    })
    
    song2 = service.create_song({
        "title": "Song 2",
        "artist": "Artist 2",
        "album": "Album 2",
        "year": 2024,
        "genre": "Rock"
    })
    
    # Create similarity relationship
    similarity = service.create_similarity(song1["id"], song2["id"], 0.8)
    
    # Verify similarity was created
    assert similarity["source_id"] == song1["id"]
    assert similarity["target_id"] == song2["id"]
    assert similarity["similarity"] == 0.8

def test_get_song_recommendations(neo4j_session):
    service = Neo4jService(neo4j_session)
    
    # Create test songs
    song1 = service.create_song({
        "title": "Song 1",
        "artist": "Artist 1",
        "album": "Album 1",
        "year": 2024,
        "genre": "Rock"
    })
    
    song2 = service.create_song({
        "title": "Song 2",
        "artist": "Artist 2",
        "album": "Album 2",
        "year": 2024,
        "genre": "Rock"
    })
    
    song3 = service.create_song({
        "title": "Song 3",
        "artist": "Artist 3",
        "album": "Album 3",
        "year": 2024,
        "genre": "Pop"
    })
    
    # Create similarity relationships
    service.create_similarity(song1["id"], song2["id"], 0.8)
    service.create_similarity(song1["id"], song3["id"], 0.3)
    
    # Get recommendations
    recommendations = service.get_song_recommendations(song1["id"], limit=2)
    
    # Verify recommendations
    assert len(recommendations) == 2
    assert recommendations[0]["id"] == song2["id"]  # Most similar
    assert recommendations[1]["id"] == song3["id"]  # Less similar 