# Ohrwurm Development Environment

## Prerequisites

### Required Software
- Python 3.12 or higher
- Node.js (v18 or higher)
- Docker and Docker Compose
- Git

### Installation

1. Install Python:
```bash
brew install python
```

2. Install Node.js and npm:
```bash
brew install node
```

3. Install Docker and Docker Compose:
```bash
brew install docker docker-compose
```

4. Clone the repository:
```bash
git clone <repository-url>
cd ohrwurm
```

## Project Structure
```
ohrwurm/
├── frontend/           # React frontend application
├── backend/           # Python FastAPI backend application
│   ├── app/
│   │   ├── api/      # API endpoints and GraphQL schema
│   │   ├── models/   # Data models
│   │   ├── services/ # Business logic and database services
│   │   └── utils/    # Utility functions
│   ├── tests/        # Test files
│   └── requirements.txt
├── docker-compose.yml # Docker services configuration
└── package.json      # Root package.json for workspace management
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

### 2. Backend Setup

1. Create and activate Python virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install Python dependencies:
```bash
pip install -e .
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

The backend API will be available at:
- Main API: http://localhost:8000
- GraphQL Playground: http://localhost:8000/graphql

### 3. Frontend Setup

1. Install Node.js dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The frontend will be available at http://localhost:3000

## Available Scripts

### Root Level
```bash
npm run dev           # Start frontend development server
npm run build        # Build frontend for production
npm run test         # Run frontend tests
npm run lint         # Run frontend linter
```

### Backend
```bash
# Activate virtual environment first
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Run development server
uvicorn app.main:app --reload

# Run tests
pytest

# Format code
black .
isort .

# Run linter
flake8
```

### Frontend
```bash
cd frontend
npm run dev          # Start development server
npm run build        # Build for production
npm run preview      # Preview production build
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

1. **Backend**
   - GraphQL schema in `backend/app/api/graphql/schema.py`
   - Resolvers in `backend/app/api/graphql/resolvers.py`
   - Database services in `backend/app/services/`
   - Models in `backend/app/models/`

2. **Frontend**
   - React components in `frontend/src/components`
   - GraphQL queries in `frontend/src/graphql`
   - State management in `frontend/src/store`
   - Types in `frontend/src/types`

## Troubleshooting

### Common Issues

1. **Port Conflicts**
   - Frontend: 3000
   - Backend: 8000
   - Neo4j: 7474, 7687
   - PostgreSQL: 5432
   - pgAdmin: 5050

2. **Database Connection Issues**
   - Ensure Docker services are running: `docker-compose ps`
   - Check service logs: `docker-compose logs [service-name]`
   - Verify credentials in docker-compose.yml

3. **Python Issues**
   - Ensure virtual environment is activated
   - Check Python version: `python --version`
   - Verify dependencies: `pip list`

4. **Node.js Issues**
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

### Backend
Create `backend/.env`:
```
PORT=8000
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=ohrwurm123
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=ohrwurm
POSTGRES_USER=ohrwurm
POSTGRES_PASSWORD=ohrwurm123
```

### Frontend
Create `frontend/.env`:
```
VITE_API_URL=http://localhost:8000
```

## Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests and linting
4. Submit a pull request

## Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Strawberry GraphQL Documentation](https://strawberry.rocks/)
- [Neo4j Documentation](https://neo4j.com/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [React Documentation](https://reactjs.org/docs)
- [GraphQL Documentation](https://graphql.org/learn/) 