from functools import wraps


def make_html(tag: str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            value = func(*args, **kwargs)
            return f"<{tag}>{value}</{tag}>"
        return wrapper
    return decorator
