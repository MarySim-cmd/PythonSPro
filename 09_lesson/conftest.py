import pytest
from sqlalchemy import create_engine


@pytest.fixture(scope="session")
def db_engine():
    """Создание подключения к БД один раз на всё"""
    DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
    engine = create_engine(DATABASE_URL)
    return engine


@pytest.fixture
def db_connection(db_engine):
    """Создание соединения для каждого теста"""
    connection = db_engine.connect()
    transaction = connection.begin()
    yield connection
    transaction.rollback()
    connection.close()
