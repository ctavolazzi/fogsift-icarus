"""Smoke tests — package imports cleanly and version is set."""

import fogsift_icarus


def test_version_exists():
    assert fogsift_icarus.__version__ == "0.0.1"


def test_version_is_string():
    assert isinstance(fogsift_icarus.__version__, str)


def test_cli_importable():
    from fogsift_icarus import cli

    assert callable(cli.main)
