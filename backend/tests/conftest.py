import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from neo4j import GraphDatabase
from app.main import app
from app.services.postgres import Base, get_db
from app.services.neo4j import get_neo4j_driver

# Test database URLs
TEST_POSTGRES_URL = "postgresql://ohrwurm:ohrwurm123@localhost:5432/ohrwurm_test"
TEST_NEO4J_URI = "bolt://localhost:7687"
TEST_NEO4J_USER = "neo4j"
TEST_NEO4J_PASSWORD = "ohrwurm123"

# Create test database engine
test_engine = create_engine(TEST_POSTGRES_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)

@pytest.fixture(scope="session")
def db_engine():
    Base.metadata.create_all(bind=test_engine)
    yield test_engine
    Base.metadata.drop_all(bind=test_engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    connection = db_engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    del app.dependency_overrides[get_db]

@pytest.fixture(scope="function")
def neo4j_driver():
    driver = GraphDatabase.driver(
        TEST_NEO4J_URI,
        auth=(TEST_NEO4J_USER, TEST_NEO4J_PASSWORD)
    )
    yield driver
    driver.close()

@pytest.fixture(scope="function")
def neo4j_session(neo4j_driver):
    session = neo4j_driver.session()
    yield session
    session.close()
    # Clean up test data
    with neo4j_driver.session() as cleanup_session:
        cleanup_session.run("MATCH (n) DETACH DELETE n") 