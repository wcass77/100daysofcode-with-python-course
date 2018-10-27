from functools import wraps


def make_html(element):
    def decorator(function):
        @wraps(function)
        def wrapped(*args, **kargs):
            return f"<{element}>{function(*args, **kargs)}</{element}>"

        return wrapped

    return decorator


# Tests


def test_make_html():
    @make_html("p")
    @make_html(element="strong")
    def get_text(text="I code with PyBites"):
        return text

    assert get_text() == "<p><strong>I code with PyBites</strong></p>"


if __name__ == "__main__":
    test_make_html()
