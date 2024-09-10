# -*- coding: utf-8 -*-
"""
The file 'time.py' provides utilities for managing and limiting the runtime of time-sensitive functions. This is particularly useful for 
functions where execution time is unpredictable or needs to be constrained.

Components
----------
time_limiter
    A decorator used to enforce a maximum runtime for functions. If the function execution exceeds the specified time limit, it is 
    terminated, and 'RequestTimeoutError' is raised.

timings
    A defaultdict used to store and track the execution times of various functions. This helps in monitoring performance and diagnosing 
    timing issues.
"""
import functools
import threading
from time import time
from typing import Union
from collections import defaultdict

from src.controllers.errors import RequestTimeoutError

timings = defaultdict(lambda: []) # defaultdict is used instead of built-in dict data structure to make adding new key-pair easy

def time_limiter(timeout:Union[int, float] = None): # timeout unit is second
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
                raise RequestTimeoutError(f'The {func.__name__} exceeded the timeout of {timeout} seconds.')
            else:
                end_time = time()
                timings[func.__name__].append(end_time-start_time)
                return result[0] if result else None
        return wrapper
    return decorator
