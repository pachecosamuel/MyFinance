# src/tests/test_sample.py

from app.application.usecases import create_user

def test_create_user():
    user = create_user(1, "Jane Doe", "jane.doe@example.com")
    assert user.user_id == 1
    assert user.name == "Jane Doe"
    assert user.email == "jane.doe@example.com"
