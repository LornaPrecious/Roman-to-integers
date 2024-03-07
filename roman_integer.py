import pytest
def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    try:
        i = 0
        num = 0
        while i < len(s):
            # Check if the current character is in the roman dictionary
            if s[i] in roman:
                # If the next character exists and has a higher value, it's a subtraction case
                if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                    num += roman[s[i + 1]] - roman[s[i]]
                    i += 2
                else:
                    # Otherwise, just add the current character's value
                    num += roman[s[i]]
            else:
                 raise ValueError("Invalid input")
                                    
        return num
    except:
        raise ValueError("Invalid input") #Invalid letters such as Z


#TEST FOR NULL VALUE
def test_null():
    assert roman_to_int("") == 0

#Single letters
def test_single_letters():
    assert roman_to_int("I") == 1 #THIS ALSO TESTS THE FIRST NUMBER
    assert roman_to_int("V") == 5
    assert roman_to_int("X") == 10
    assert roman_to_int("L") == 50
    assert roman_to_int("C") == 100
    assert roman_to_int("D") == 500
    assert roman_to_int("M") == 1000

#test multiple values
def test_many_characters():
    assert roman_to_int("XI") == 11
    assert roman_to_int("XIII") == 13
    assert roman_to_int("MDXL") == 1540

#Subtractive Notation
def test_subtractive_notation():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XL") == 40
    assert roman_to_int("XC") == 90
    assert roman_to_int("CD") == 400

#With and without SN
def test_with_without_sn():
    assert roman_to_int("XLIX") == 49
    assert roman_to_int("MCMXCIV") == 1994
    assert roman_to_int("MDXL") == 1540

#TEST REPETITIVE COMBINATION OF ROMAN LETTERS
def test_repetition():
    assert roman_to_int("II") == 2
    assert roman_to_int("III") == 3
    assert roman_to_int("XX") == 20
    assert roman_to_int("XXX") == 30
    assert roman_to_int("CC") == 200

#Test invalid characters
def test_invalid_characters():
    invalid_inputs = ["IIII", "VV", "LL", "XIZ"]
    for invalid_input in invalid_inputs:
        with pytest.raises(ValueError):
            roman_to_int(invalid_input)

if __name__ == "__main__":
    s =  input("Enter a roman numeral: ").upper()
    print(roman_to_int(s))
    test_null()
    test_single_letters()
    test_many_characters()
    test_subtractive_notation()
    test_with_without_sn()
    test_repetition()
    test_invalid_characters()
    

    


