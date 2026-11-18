def greet(name):
    """Return a greeting for name, raising ValueError for an empty name."""
    if name == "":
        raise ValueError("name must not be empty")
    return "Hello, {}!".format(name)
