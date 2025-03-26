import pytest
from app.api.graphql.resolvers import (
    Query,
    Mutation,
    get_song,
    get_similar_songs,
    get_song_recommendations,
    create_song,
    create_similarity,
    get_user,
    create_user,
    update_user,
    delete_user
)

def test_get_song_resolver(neo4j_session):
    # Create test song
    song_data = {
        "title": "Test Song",
        "artist": "Test Artist",
        "album": "Test Album",
        "year": 2024,
        "genre": "Test Genre"
    }
    
    # Create song in Neo4j
    result = neo4j_session.run(
        """
        CREATE (s:Song {
            title: $title,
            artist: $artist,
            album: $album,
            year: $year,
            genre: $genre
        })
        RETURN s
        """,
        song_data
    )
    song = result.single()["s"]
    
    # Test resolver
    result = get_song(None, song["id"])
    
    # Verify result
    assert result["id"] == song["id"]
    assert result["title"] == song_data["title"]
    assert result["artist"] == song_data["artist"]

def test_get_similar_songs_resolver(neo4j_session):
    # Create test songs
    song1 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 1",
            artist: "Artist 1",
            album: "Album 1",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    song2 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 2",
            artist: "Artist 2",
            album: "Album 2",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    # Create similarity relationship
    neo4j_session.run(
        """
        MATCH (s1:Song {id: $id1})
        MATCH (s2:Song {id: $id2})
        CREATE (s1)-[r:SIMILAR_TO {similarity: $similarity}]->(s2)
        """,
        {"id1": song1["id"], "id2": song2["id"], "similarity": 0.8}
    )
    
    # Test resolver
    result = get_similar_songs(None, song1["id"])
    
    # Verify result
    assert len(result) == 1
    assert result[0]["id"] == song2["id"]
    assert result[0]["similarity"] == 0.8

def test_get_song_recommendations_resolver(neo4j_session):
    # Create test songs
    song1 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 1",
            artist: "Artist 1",
            album: "Album 1",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    song2 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 2",
            artist: "Artist 2",
            album: "Album 2",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    song3 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 3",
            artist: "Artist 3",
            album: "Album 3",
            year: 2024,
            genre: "Pop"
        })
        RETURN s
        """
    ).single()["s"]
    
    # Create similarity relationships
    neo4j_session.run(
        """
        MATCH (s1:Song {id: $id1})
        MATCH (s2:Song {id: $id2})
        CREATE (s1)-[r:SIMILAR_TO {similarity: $similarity}]->(s2)
        """,
        {"id1": song1["id"], "id2": song2["id"], "similarity": 0.8}
    )
    
    neo4j_session.run(
        """
        MATCH (s1:Song {id: $id1})
        MATCH (s2:Song {id: $id2})
        CREATE (s1)-[r:SIMILAR_TO {similarity: $similarity}]->(s2)
        """,
        {"id1": song1["id"], "id2": song3["id"], "similarity": 0.3}
    )
    
    # Test resolver
    result = get_song_recommendations(None, song1["id"], limit=2)
    
    # Verify result
    assert len(result) == 2
    assert result[0]["id"] == song2["id"]  # Most similar
    assert result[1]["id"] == song3["id"]  # Less similar

def test_create_song_resolver(neo4j_session):
    # Test data
    song_data = {
        "title": "New Song",
        "artist": "New Artist",
        "album": "New Album",
        "year": 2024,
        "genre": "New Genre"
    }
    
    # Test resolver
    result = create_song(None, song_data)
    
    # Verify result
    assert result["title"] == song_data["title"]
    assert result["artist"] == song_data["artist"]
    assert result["album"] == song_data["album"]
    assert result["year"] == song_data["year"]
    assert result["genre"] == song_data["genre"]

def test_create_similarity_resolver(neo4j_session):
    # Create test songs
    song1 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 1",
            artist: "Artist 1",
            album: "Album 1",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    song2 = neo4j_session.run(
        """
        CREATE (s:Song {
            title: "Song 2",
            artist: "Artist 2",
            album: "Album 2",
            year: 2024,
            genre: "Rock"
        })
        RETURN s
        """
    ).single()["s"]
    
    # Test resolver
    result = create_similarity(None, song1["id"], song2["id"], 0.8)
    
    # Verify result
    assert result["source_id"] == song1["id"]
    assert result["target_id"] == song2["id"]
    assert result["similarity"] == 0.8

def test_user_resolvers(db_session):
    # Test data
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword123"
    }
    
    # Test create_user resolver
    created_user = create_user(None, user_data)
    assert created_user["email"] == user_data["email"]
    assert created_user["username"] == user_data["username"]
    
    # Test get_user resolver
    user = get_user(None, created_user["id"])
    assert user["id"] == created_user["id"]
    assert user["email"] == user_data["email"]
    
    # Test update_user resolver
    update_data = {
        "username": "updateduser",
        "email": "updated@example.com"
    }
    updated_user = update_user(None, created_user["id"], update_data)
    assert updated_user["username"] == update_data["username"]
    assert updated_user["email"] == update_data["email"]
    
    # Test delete_user resolver
    delete_user(None, created_user["id"])
    deleted_user = get_user(None, created_user["id"])
    assert deleted_user is None 