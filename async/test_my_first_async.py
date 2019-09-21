import my_first_async


def test_producer_non_blocking():
    """
    Producer A is awaiting a result, and passes control to the event loop.
    """
    assert 1 == 2


def test_producer_concurrent():
    """
    Producer B does work while Producer A awaits a result.
    """
    assert 1 == 2


def test_consumer_non_blocking():
    """
    consumer A is awaiting a result, and passes control to the event loop.
    """
    assert 1 == 2


def test_consumer_concurrent():
    """
    consumer B does work while Producer A awaits a result.
    """
    assert 1 == 2
