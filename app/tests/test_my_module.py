import pytest
from app.services.user_service import UserService


def test_my_function():
    user_service = UserService()
    assert user_service.get_user_data() == {"username": "SampleUser", "age": 30}
