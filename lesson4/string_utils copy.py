import pytest
from string_utils import StringUtils

utils=StringUtils()

def capitalize_pozitive():

    assert utils.capitalize("nica")=="Nica"
    assert utils.capitalize("my name nica")=="My name nica"
    assert utils.capitalize("666")=="666"

def capitalize_negative():

    assert utils.capitalize("")==""
    assert utils.capitalize("  ")=="  "



@pytest.mark.parametrize("input_string, expected_string", [

    ("  nica", "nica"),
    ("   my name nica", "my name nica"),
    ("   666", "666"),]) 
def trim_positive(input_string, expected_string):
    
    assert utils.trim(input_string)==expected_string

@pytest.mark.parametrize("input_string, expected_string", [

    ("   ", ""),
    ("", "")]) 
def trim_negative(input_string, expected_string):
    
    assert utils.trim(input_string)==expected_string



def to_list_positive():

    assert utils.to_list("n, i, c, a")==["n", "i", "c", "a"]
    assert utils.to_list("n; i; c; a")==["n", "i", "c", "a"]
    assert utils.to_list("n: i: c: a")==["n", "i", "c", "a"]
    assert utils.to_list("nica")==["nica"]

def to_list_negative():
    assert utils.to_list("")==[]
    assert utils.to_list("n i c a")==["n", "i", "c", "a"]



@pytest.mark.parametrize("string, symbol, true_false", [

    ("Skypro", "k", True),
    ("Skypro", "a", False),
    ("Скайпро", "к", True),
    ("Скайпро", "у", False)]) 
def contains_positive(string, symbol, true_false):
    
    assert utils.contains("string", "symbol")==true_false

@pytest.mark.parametrize("string, symbol, true_false", [

    ("", "s", False),
    ("    ", "s", False),
    (", , ,","s", False),
    ("Skypro", "s", True),
    ("Скайпро", "к", True),]) 
def contains_negative(string, symbol, true_false):
    
    assert utils.contains("string", "symbol")==true_false



def delete_symbol_positive():

    assert utils.delete_symbol("Skypro", "k")=="Sypro"
    assert utils.delete_symbol("Skypro", "a")=="Skypro"
    assert utils.delete_symbol("Скайпро", "к")=="Сайпро"
    assert utils.delete_symbol("Скайпро", "у")=="Скайпро"

def delete_symbol_negative():

    assert utils.delete_symbol("Skypro", "")=="Skypro"
    assert utils.delete_symbol("Скайпро", " ")=="Скайпро"



@pytest.mark.parametrize("string, symbol, true_false", [

    ("my name nica", "m", True),
    ("my name nica", "n", False),
    ("меня зовут Ника", "м", True),
    ("Меня зовут Ника", "н", False)]) 
def starts_with_positive(string, symbol, true_false):
    
    assert utils.starts_with("string", "symbol")==true_false

@pytest.mark.parametrize("string, symbol, true_false", [

    ("", "s", False),
    ("    ", "s", False),
    (",,,","s", False)]) 
def starts_with_negative(string, symbol, true_false):
    
    assert utils.starts_with("string", "symbol")==true_false



def end_with_positive():

    assert utils.end_with("Skypro", "o")==True
    assert utils.end_with("Skypro", "a")==False
    assert utils.end_with("Скайпро", "о")==True
    assert utils.end_with("Скайпро", "а")==False    

def end_with_negative():

    assert utils.end_with("Skypro", "")==False
    assert utils.end_with("Скайпро", " ")==False
    assert utils.end_with("", "а")==False



@pytest.mark.parametrize("string, true_false", [

    ("", True),
    ("", True),
    ("меня зовут Ника", False),
    ("My name Nica", False)]) 
def is_empty_positive(string, symbol, true_false):
    
    assert utils.is_empty("string")==true_false

@pytest.mark.parametrize("string, true_false", [
    
    ("...", False),
    (",,,", False)]) 
def is_empty_positive(string, true_false):
    
    assert utils.is_empty("string")==true_false 



def list_to_string_positive():

    assert utils.list_to_string(["n","i","c","a"])==("n, i, c, a")
    assert utils.list_to_string(["n","i","c","a"], "-")==("n-i-c-a")
    assert utils.list_to_string(["nica"])==("nica")
    assert utils.list_to_string([1,2,3,4])=="1, 2, 3, 4"

def list_to_string_negative():
    assert utils.list_to_string([""])==""