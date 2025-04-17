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
        "experienceLevels": 5,
        "salary": '40000 - 65000'
    }

@pytest.fixture
def company_data():
    return {
        "email": "contact@startup.com",
        "password": "pass456",
        "companyName": "Startup Inc.",
        "description": "A small innovative startup."
    }

@pytest.fixture
def client():
    from app import create_app
    app = create_app()
    return app.test_client()


@pytest.fixture
def auth_headers(client):
    # Inscription entreprise pour auth
    res = client.post("/register/company", json={
        "email": "test@comp.com",
        "password": "pass",
        "company_name": "TestCo",
        "description": "..."
    })
    token = res.get_json()["token"]
    return {"company": {"Authorization": f"Bearer {token}"}}


@pytest.fixture
def created_job(client, auth_headers):
    res = client.post("/jobs/create", json={
        "title": "Job to update",
        "location": "Paris",
        "technologies": ["Django"],
        "experience_required": 2,
        "salary": 50000,
        "description": "To be updated"
    }, headers=auth_headers["company"])
    return res.get_json()


@pytest.fixture
def auth_headers(client):
    # Créer un développeur
    dev_res = client.post("/register/developer", json={
        "email": "dev@example.com",
        "password": "devpass",
        "first_name": "Jane",
        "last_name": "Doe"
    })
    dev_token = dev_res.get_json()["token"]

    # Créer une entreprise
    comp_res = client.post("/register/company", json={
        "email": "hr@corp.com",
        "password": "hrpass",
        "company_name": "Corp Ltd.",
        "description": "..."
    })
    comp_token = comp_res.get_json()["token"]

    return {
        "developer": {"Authorization": f"Bearer {dev_token}"},
        "company": {"Authorization": f"Bearer {comp_token}"}
    }
