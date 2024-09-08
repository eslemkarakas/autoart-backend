# -*- coding: utf-8 -*-
import functools
import threading
from time import time
from typing import Union
from collections import defaultdict

timings = defaultdict(lambda: [])

def time_limiter(timeout:Union[int, float] = None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def target(result):
                result.append(func(*args, **kwargs))

            start_time = time()
            result = []
            thread = threading.Thread(target=target, args=(result,))
            thread.start()
            thread.join(timeout)

            if thread.is_alive():
                raise TimeoutError(f'[ERROR] Function {func.__name__} exceeded the timeout of {timeout} seconds.')
            else:
                end_time = time()
                timings[func.__name__].append(end_time-start_time)
                return result[0] if result else None
        return wrapper
    return decorator
