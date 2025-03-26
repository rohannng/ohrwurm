# Ohrwurm Project Status

## Project Overview
Ohrwurm is a crowdsourced music recommendation system that uses a graph-based approach to model song relationships. Users can discover related songs through "upworms" (user-contributed relationships between songs), add new relationships, and explore the music graph.

## Current Project State

### Completed Setup
1. Project structure established:
   ```
   ohrwurm/
   ├── frontend/           # React frontend application
   ├── backend/           # Node.js backend application
   ├── docker-compose.yml # Database services configuration
   ├── package.json       # Root workspace configuration
   ├── DEVELOPMENT.md     # Development environment documentation
   └── PROJECT_STATUS.md  # This file
   ```

2. Development environment configured:
   - Docker Compose setup with Neo4j and PostgreSQL
   - Node.js workspace configuration
   - Environment files and variables
   - Development documentation

3. Database Services:
   - Neo4j (Graph DB) running on ports 7474 (HTTP) and 7687 (Bolt)
   - PostgreSQL running on port 5432
   - pgAdmin running on port 5050

### Current Configuration

#### Database Credentials
1. Neo4j:
   - URL: bolt://localhost:7687
   - Browser: http://localhost:7474
   - Username: neo4j
   - Password: ohrwurm123

2. PostgreSQL:
   - Host: localhost:5432
   - Database: ohrwurm
   - Username: ohrwurm
   - Password: ohrwurm123

3. pgAdmin:
   - URL: http://localhost:5050
   - Email: admin@ohrwurm.com
   - Password: admin123

## Next Steps

### 1. Backend Development
- [ ] Set up Node.js/Express backend with TypeScript
- [ ] Configure GraphQL server (Apollo)
- [ ] Create Neo4j database schema for songs and relationships
- [ ] Implement PostgreSQL schema for user data
- [ ] Develop GraphQL resolvers for:
  - [ ] Song queries and mutations
  - [ ] User authentication
  - [ ] Upworm management

### 2. Frontend Development
- [ ] Initialize React application with Vite
- [ ] Set up Material-UI components
- [ ] Implement React Force Graph for visualization
- [ ] Create core components:
  - [ ] Song search
  - [ ] Graph visualization
  - [ ] Song relationship management
  - [ ] User authentication

### 3. Database Schema Implementation
#### Neo4j (Songs and Relationships)
```cypher
// Example schema to implement
CREATE (s:Song {
    id: string,
    name: string,
    artist: string,
    releaseDate: date,
    spotifyId: string,
    createdAt: datetime,
    updatedAt: datetime
})

CREATE (s1:Song)-[r:UPWORM {
    weight: integer,
    createdAt: datetime,
    createdBy: string
}]->(s2:Song)
```

#### PostgreSQL (User Data)
```sql
-- Example schema to implement
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    username VARCHAR(50) UNIQUE,
    created_at TIMESTAMP,
    last_login TIMESTAMP
);

CREATE TABLE sessions (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    token VARCHAR(255),
    expires_at TIMESTAMP
);
```

### 4. API Development
#### GraphQL Schema
```graphql
# Example schema to implement
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

## Immediate Next Actions
Choose one of these paths to proceed:

1. **Backend First Approach**:
   - Initialize Node.js/Express backend
   - Set up GraphQL server
   - Implement database schemas
   - Create initial resolvers

2. **Frontend First Approach**:
   - Set up React with Vite
   - Implement basic UI components
   - Create graph visualization prototype
   - Add mock data for development

3. **Database First Approach**:
   - Implement Neo4j schema
   - Create PostgreSQL tables
   - Add sample data
   - Test queries and relationships

## Development Notes
- The Neo4j instance had memory issues initially but was resolved by adjusting the memory configuration
- The project uses a monorepo structure with workspaces
- All services are containerized for consistent development
- The application will use GraphQL for flexible data querying

## Prompt for Continuing Development

To continue development on this project, you should:

1. Review the existing files:
   - `docker-compose.yml` for database configuration
   - `DEVELOPMENT.md` for setup instructions
   - `package.json` files for dependencies
   - Environment files for configuration

2. Choose one of the "Immediate Next Actions" paths

3. Follow the development workflow:
   - Use the provided database credentials
   - Follow the monorepo structure
   - Implement features according to the schema designs
   - Test connections and functionality
   - Document new components and features

4. Key considerations:
   - Maintain type safety with TypeScript
   - Follow GraphQL best practices
   - Ensure proper error handling
   - Implement security best practices
   - Write tests for new features

Would you like to proceed with any of these next steps? 