from checkio_referee import RefereeBase

import settings
import settings_env
from tests import TESTS

cover = """def cover(func, data):
    result = func(tuple(data))
    if not isinstance(result, (list, tuple)):
        raise TypeError("The result should be a list or a tuple")
    return result
"""


class Referee(RefereeBase):
    TESTS = TESTS
    EXECUTABLE_PATH = settings.EXECUTABLE_PATH
    CURRENT_ENV = settings_env.CURRENT_ENV
    FUNCTION_NAME = "absolute_sorting"
    ENV_COVERCODE = {
        "python_2": cover,
        "python_3": cover,
        "javascript": None
    }