import dataDest
from pytest_check import check

filename = "test2.txt"

def test_fileparseXY_isEqual():								#	pytest -v
	output = dataDest.check_equal(filename)
	assert output == 0
"""
def test_context_manager():
    with check:
        x = dataDest.check_equal("test1.txt")
        assert 1 < x < 4
"""

