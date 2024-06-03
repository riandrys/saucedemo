import pytest


@pytest.mark.usefixtures("init_driver", "test_failed_check")
class BaseTest:
    pass
