# Ohrwurm Backend

A Python FastAPI backend for the Ohrwurm music recommendation system.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at http://localhost:8000
GraphQL playground at http://localhost:8000/graphql

## Project Structure

```
backend/
├── app/
│   ├── api/           # API endpoints and GraphQL schema
│   ├── models/        # Data models
│   ├── services/      # Business logic and database services
│   └── utils/         # Utility functions
├── tests/             # Test files
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## API Documentation

### GraphQL Endpoints

#### Queries
- `getSong(id: ID!)`: Get a song by ID
- `searchSongs(query: String!)`: Search songs by name or artist
- `getRelatedSongs(songId: ID!)`: Get songs related by upworms

#### Mutations
- `addUpworm(fromSongId: ID!, toSongId: ID!)`: Add an upworm between songs
- `addSong(name: String!, artist: String!)`: Add a new song

## Development

### Running Tests
```bash
pytest
```

### Code Style
This project uses:
- Black for code formatting
- isort for import sorting
- flake8 for linting

### Database Migrations
The project uses SQLAlchemy for PostgreSQL and Neo4j for graph data.
No migrations are needed as the schema is managed by the ORM. 