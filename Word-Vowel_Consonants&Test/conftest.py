import pytest
from words import Words


@pytest.fixture
def word_info_obj():
    wd = Words('text1.txt')
    return wd
