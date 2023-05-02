import logging
import pytest
from prettyconf import Configuration
from _pytest.nodes import Item
from tests.configuration.properties import Properties
from tests.services.service_base import ServiceBase
from tests.models.schemas_model import SchemasModel
from tests.core.rest import Rest
from tests.core.schemas_files import SchemasFiles
from tests.utils.validate_run_tests import validate_only_run_env, validate_skip_env, validate_skip_device


def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='staging', help='Environment'
    )
    parser.addoption(
        '--country', action='store', default='ar', help='Country'
    )

@pytest.fixture
def log(request):
    return logging.getLogger(request.node.name)

@pytest.fixture
def props(request) -> Configuration:
    args = {
        "env": request.config.getoption('--env'),
        "country": request.config.getoption('--country')}
    return Properties.get_config(args)

@pytest.fixture
def rest(log, props):
    return Rest(log, props)

@pytest.fixture
def service(log, props, rest) -> ServiceBase:
    return ServiceBase(log, rest, props)

@pytest.fixture
def get_posts(log, rest, props) -> ServiceBase:
    return ServiceBase(log, rest, props)

@pytest.fixture
def posts_schema(log, rest, props) -> ServiceBase:
    return ServiceBase(log, rest, props)

@pytest.fixture
def schemas() -> SchemasModel:
    return SchemasModel(**SchemasFiles.get_dict())

def pytest_collection_modifyitems(items):
    items.sort(key=lambda x: getattr(x, 'last', 0))

def pytest_runtest_setup(item: Item):
    validate_only_run_env(item)
    validate_skip_env(item)
    validate_skip_device(item)
