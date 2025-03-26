# Ohrwurm Development Environment

## Prerequisites

### Required Software
- Node.js (v18 or higher)
- Docker and Docker Compose
- Git

### Installation

1. Install Node.js and npm:
```bash
brew install node
```

2. Install Docker and Docker Compose:
```bash
brew install docker docker-compose
```

3. Clone the repository:
```bash
git clone <repository-url>
cd ohrwurm
```

## Project Structure
```
ohrwurm/
├── frontend/           # React frontend application
├── backend/           # Node.js backend application
├── docker-compose.yml # Docker services configuration
└── package.json       # Root package.json for workspace management
```

## Development Setup

### 1. Start Database Services
```bash
# Start Neo4j, PostgreSQL, and pgAdmin
docker-compose up -d
```

Access points:
- Neo4j Browser: http://localhost:7474
  - Username: neo4j
  - Password: ohrwurm123
- PostgreSQL: localhost:5432
  - Database: ohrwurm
  - Username: ohrwurm
  - Password: ohrwurm123
- pgAdmin: http://localhost:5050
  - Email: admin@ohrwurm.com
  - Password: admin123

### 2. Install Dependencies
```bash
# Install dependencies for all packages
npm install
```

### 3. Start Development Servers
```bash
# Start both frontend and backend servers
npm run dev

# Or start them separately:
npm run dev:frontend  # Frontend only (http://localhost:3000)
npm run dev:backend   # Backend only (http://localhost:4000)
```

## Available Scripts

### Root Level
```bash
npm run dev           # Start both frontend and backend
npm run dev:frontend  # Start frontend only
npm run dev:backend   # Start backend only
npm run build        # Build all packages
npm run test         # Run tests in all packages
npm run lint         # Run linter in all packages
```

### Frontend
```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
npm run lint         # Run linter
```

### Backend
```bash
cd backend
npm run dev          # Start development server
npm run build        # Build for production
npm run test         # Run tests
npm run lint         # Run linter
```

## Development Workflow

### Database Management

1. **Neo4j**
   - Access Neo4j Browser at http://localhost:7474
   - Use Cypher queries to manage graph data
   - Default credentials: neo4j/ohrwurm123

2. **PostgreSQL**
   - Access pgAdmin at http://localhost:5050
   - Connect to PostgreSQL server:
     - Host: postgres
     - Port: 5432
     - Database: ohrwurm
     - Username: ohrwurm
     - Password: ohrwurm123

### Code Organization

1. **Frontend**
   - React components in `frontend/src/components`
   - GraphQL queries in `frontend/src/graphql`
   - State management in `frontend/src/store`
   - Types in `frontend/src/types`

2. **Backend**
   - GraphQL resolvers in `backend/src/resolvers`
   - Database models in `backend/src/models`
   - Services in `backend/src/services`
   - Types in `backend/src/types`

## Troubleshooting

### Common Issues

1. **Port Conflicts**
   - Frontend: 3000
   - Backend: 4000
   - Neo4j: 7474, 7687
   - PostgreSQL: 5432
   - pgAdmin: 5050

2. **Database Connection Issues**
   - Ensure Docker services are running: `docker-compose ps`
   - Check service logs: `docker-compose logs [service-name]`
   - Verify credentials in docker-compose.yml

3. **Node.js Issues**
   - Clear node_modules: `rm -rf node_modules`
   - Clear npm cache: `npm cache clean --force`
   - Reinstall dependencies: `npm install`

### Useful Commands

```bash
# View running containers
docker-compose ps

# View container logs
docker-compose logs -f [service-name]

# Restart services
docker-compose restart [service-name]

# Stop all services
docker-compose down

# Clean up volumes
docker-compose down -v
```

## Environment Variables

### Frontend
Create `frontend/.env`:
```
VITE_API_URL=http://localhost:4000
```

### Backend
Create `backend/.env`:
```
PORT=4000
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ohrwurm123
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=ohrwurm
POSTGRES_USER=ohrwurm
POSTGRES_PASSWORD=ohrwurm123
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## Additional Resources

- [Neo4j Documentation](https://neo4j.com/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [React Documentation](https://reactjs.org/docs)
- [GraphQL Documentation](https://graphql.org/learn/) 