import pytest
from app.services.postgres import PostgresService
from app.models.user import UserCreate, UserUpdate

def test_create_user(db_session):
    service = PostgresService(db_session)
    
    # Test data
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123"
    )
    
    # Create user
    user = service.create_user(user_data)
    
    # Verify user was created
    assert user.email == user_data.email
    assert user.username == user_data.username
    assert user.password != user_data.password  # Password should be hashed

def test_get_user_by_id(db_session):
    service = PostgresService(db_session)
    
    # Create test user
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123"
    )
    created_user = service.create_user(user_data)
    
    # Get user by ID
    user = service.get_user_by_id(created_user.id)
    
    # Verify user was retrieved
    assert user.id == created_user.id
    assert user.email == user_data.email
    assert user.username == user_data.username

def test_get_user_by_email(db_session):
    service = PostgresService(db_session)
    
    # Create test user
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123"
    )
    created_user = service.create_user(user_data)
    
    # Get user by email
    user = service.get_user_by_email(user_data.email)
    
    # Verify user was retrieved
    assert user.id == created_user.id
    assert user.email == user_data.email
    assert user.username == user_data.username

def test_update_user(db_session):
    service = PostgresService(db_session)
    
    # Create test user
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123"
    )
    created_user = service.create_user(user_data)
    
    # Update user
    update_data = UserUpdate(
        username="updateduser",
        email="updated@example.com"
    )
    updated_user = service.update_user(created_user.id, update_data)
    
    # Verify user was updated
    assert updated_user.id == created_user.id
    assert updated_user.username == update_data.username
    assert updated_user.email == update_data.email

def test_delete_user(db_session):
    service = PostgresService(db_session)
    
    # Create test user
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword123"
    )
    created_user = service.create_user(user_data)
    
    # Delete user
    service.delete_user(created_user.id)
    
    # Verify user was deleted
    deleted_user = service.get_user_by_id(created_user.id)
    assert deleted_user is None

def test_verify_password(db_session):
    service = PostgresService(db_session)
    
    # Create test user
    password = "testpassword123"
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password=password
    )
    created_user = service.create_user(user_data)
    
    # Verify correct password
    assert service.verify_password(created_user.id, password) is True
    
    # Verify incorrect password
    assert service.verify_password(created_user.id, "wrongpassword") is False 