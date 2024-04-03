import config_log
import logging
import pytest

logger = logging.getLogger(__name__)

def test_valid():
    logger.warning("This is a problem!")
    assert True

def test_invalid():
    logger.info("SOme info")
    assert False
