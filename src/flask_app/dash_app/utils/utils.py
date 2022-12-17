import functools

from collections import OrderedDict


def custom_callback(dash_app, outputs, inputs):
    outputs = OrderedDict(outputs)
    results = outputs.copy()
    results.update((key, None) for key in results.keys())

    def actual_decorator(fn):
        @functools.wraps(fn)
        @dash_app.callback(list(outputs.values()), inputs)
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)

            results.update(res)

            return tuple(results.values())

        return wrapper

    return actual_decorator
