import pytest
from string_utils import StringUtils

utils=StringUtils()

def test_capitalize():
    #OK
    assert utils.capitilize("nica")=="Nica"
    assert utils.capitilize("my name nica")=="My name nica"
    assert utils.capitilize("666")=="666"

    #NeOK
    assert utils.capitilize("")==""
    assert utils.capitilize("  ")=="  "

@pytest.mark.parametrize("input_string, expected_string", [
    #OK
    ("  nica", "nica"),
    ("   my name nica", "my name nica"),
    ("   666", "666"),

    #NeOK
    ("   ", "   "),
    ("", ""),
]) 


def trim(input_string, expected_string):
    
    assert utils.trim(input_string)==expected_string
