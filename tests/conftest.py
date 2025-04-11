import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)

import pytest
from services.concreteuserfactory import ConcreteUserFactory

@pytest.fixture
def user_data():
    return {"email": "test@example.com", "password": "password_123"}

@pytest.fixture
def user_factory():
    return ConcreteUserFactory()

@pytest.fixture
def developer_data():
    return {
        "email": "dev@example.com",
        "password": "pass123",
        "programmingLanguages": ["Python", "JavaScript"],
        "experienceLevels": {"Python": 4, "JavaScript": 3},
        "salary": 40000
    }

@pytest.fixture
def company_data():
    return {
        "email": "contact@startup.com",
        "password": "pass456",
        "companyName": "Startup Inc.",
        "description": "A small innovative startup."
    }