# Ohrwurm Architecture

## System Overview
Ohrwurm is a crowdsourced music recommendation system that uses a graph-based approach to model song relationships through user interactions called "upworms". The system allows users to discover related songs and contribute to the recommendation engine through their interactions.

## Technology Stack

### Frontend
- **Framework**: React with TypeScript
- **UI Components**: 
  - Material-UI (MUI) for base components
  - React Force Graph for 3D graph visualization
  - React Query for data fetching and caching
- **State Management**: Zustand (lightweight alternative to Redux)
- **Mobile**: React Native (for future mobile app)

### Backend
- **Framework**: Node.js with Express.js
- **API**: GraphQL (for flexible querying of graph data)
- **Authentication**: Auth0 or Firebase Auth
- **API Documentation**: GraphQL Playground

### Databases
- **Graph Database**: Neo4j
  - Stores song relationships and upworms
  - Enables efficient graph traversal and recommendations
- **Relational Database**: PostgreSQL
  - Stores user data, authentication info, and other transactional data
  - Handles user sessions and application state

### Infrastructure
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **CI/CD**: GitHub Actions
- **Monitoring**: Prometheus + Grafana
- **Logging**: ELK Stack

## Data Models

### Neo4j Graph Model
```cypher
// Song Node
CREATE (s:Song {
    id: string,
    name: string,
    artist: string,
    releaseDate: date,
    spotifyId: string,
    createdAt: datetime,
    updatedAt: datetime
})

// Upworm Relationship
CREATE (s1:Song)-[r:UPWORM {
    weight: integer,
    createdAt: datetime,
    createdBy: string
}]->(s2:Song)
```

### PostgreSQL Schema
```sql
-- Users Table
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    username VARCHAR(50) UNIQUE,
    created_at TIMESTAMP,
    last_login TIMESTAMP
);

-- User Sessions
CREATE TABLE sessions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    token VARCHAR(255),
    expires_at TIMESTAMP,
    created_at TIMESTAMP
);
```

## Key Features & Components

### 1. Song Discovery
- Interactive 3D graph visualization
- Force-directed layout for relationship visualization
- Zoom and pan capabilities
- Click to expand/collapse relationships
- Hover information for songs

### 2. Upworm System
- One-click upworm addition
- Weighted relationship visualization
- Real-time updates
- Animated transitions

### 3. Song Management
- Add new songs
- Link to Spotify for metadata
- Manual relationship creation
- Song search and filtering

### 4. User Features
- User authentication
- Personal upworm history
- Favorite songs
- Custom playlists

## API Endpoints

### GraphQL Schema
```graphql
type Song {
    id: ID!
    name: String!
    artist: String!
    relatedSongs: [Song!]!
    upwormCount: Int!
}

type Query {
    getSong(id: ID!): Song
    searchSongs(query: String!): [Song!]!
    getRelatedSongs(songId: ID!): [Song!]!
}

type Mutation {
    addUpworm(fromSongId: ID!, toSongId: ID!): Boolean!
    addSong(name: String!, artist: String!): Song!
}
```

## Security Considerations
- JWT-based authentication
- Rate limiting for API endpoints
- Input validation and sanitization
- CORS configuration
- Data encryption at rest

## Performance Optimizations
- Graph query caching
- Pagination for large result sets
- Lazy loading of graph components
- WebSocket for real-time updates
- CDN for static assets

## Deployment Architecture
```
[Client Browser/Mobile App]
         ↓
[Load Balancer (Nginx)]
         ↓
[API Gateway]
         ↓
[Backend Services]
    ↙         ↘
[Neo4j]    [PostgreSQL]
```

## Monitoring & Analytics
- User engagement metrics
- Song popularity tracking
- Graph traversal patterns
- System performance metrics
- Error tracking and logging

## Future Considerations
- Mobile app development
- Social features (following users, sharing)
- Advanced recommendation algorithms
- Integration with other music services
- Offline support 