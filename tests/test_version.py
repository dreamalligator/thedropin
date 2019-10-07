from thedropin.version import __version__

def test_version():
    """
    a very simple unit test for demonstration purposes.

    version file gets overwritten when releasing.
    """

    assert len(__version__) >= 5
    assert __version__.count('.') == 2
