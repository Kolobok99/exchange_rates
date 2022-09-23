import functools
from loguru import logger


def logger_wraps(*, entry=True, exit=True, level="DEBUG"):

    def wrapper(func):
        name = func.__name__
        file = func.__module__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "START '{}' from {}", name, file)
            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "END '{}' from {}", name, file)
            return result

        return wrapped

    return wrapper