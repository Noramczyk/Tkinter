import dataDest2.0

def test_fileparseXY_isEqual():
	output = dataDest2.0.check_equal("test1.txt")
    assert output == 0