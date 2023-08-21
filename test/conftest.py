import pytest

def pytest_addoption(parser):
    parser.addoption("--username", action="store", help="NASA Earthdata username")
    parser.addoption("--password", action="store", help="NASA Earthdata password")

@pytest.fixture(scope="session")
def username(request):
    """ Returns NASA Earthdata username """
    return request.config.getoption("--username")

@pytest.fixture(scope="session")
def password(request):
    """ Returns NASA Earthdata password """
    return request.config.getoption("--password")
