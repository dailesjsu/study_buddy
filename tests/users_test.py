import pytest
from app.models import User

@pytest.fixture(scope='module')
def new_user():
    user = User('patkennedy79@gmail.com', 'FlaskIsAwesome')
    return user


def test_new_user(new_user):
    assert new_user.email == 'patkennedy79@gmail.com'
    assert new_user.password_hash != 'FlaskIsAwesome'
    assert not new_user.authenticated
    assert new_user.role == 'user'


def test_setting_password(new_user):
    new_user.set_password('MyNewPassword')
    assert new_user.hashed_password != 'MyNewPassword'
    assert new_user.is_correct_password('MyNewPassword')
    assert not new_user.is_correct_password('MyNewPassword2')
    assert not new_user.is_correct_password('FlaskIsAwesome')


def test_check_password(new_user):
    new_user.check_password("MyNewPassword")
    assert new_user.check_password != 'MyNewPassword'
    assert new_user.is_correct_check_password('MyNewPassword')
    assert not new_user.is_correct_check_password('MyNewPassword2')
    assert not new_user.is_correct_check_password('FlaskIsAwesome')


