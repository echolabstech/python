import my_first_async


def test_producer_non_blocking():
    """
    Producer A is awaiting a result, and passes control to the event loop.
    """
    assert 1 == 2



@pytest.mark.skip(reason='not implemented')
def test_producer_concurrent():
    """
    Producer B does work while Producer A awaits a result.
    """
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_consumer_non_blocking():
    """
    consumer A is awaiting a result, and passes control to the event loop.
    """
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_consumer_concurrent():
    """
    consumer B does work while Producer A awaits a result.
    """
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_catches_404_page_not_found():
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_catches_400_bad_request():
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_handle_302_redirect():
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_handle_301_moved():
    assert 1 == 2


@pytest.mark.skip(reason='not implemented')
def test_log_on_exception():
    assert 1 == 2
