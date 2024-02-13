def roman_to_int(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    try:
        i = 0
        num = 0
        while i < len(s):
            # Check if the current character is in the Roman dictionary
            if s[i] in roman:
                # If the next character exists and has a higher value, it's a subtraction case
                if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                    num += roman[s[i + 1]] - roman[s[i]]
                    i += 2
                else:
                    # Otherwise, just add the current character's value
                    
             
                    num += roman[s[i]]
                    i += 1
            else:
                # If the current character is not a valid Roman numeral, return an error message
                return "Invalid input"
        
        return num
    except:
        return "Invalid input"


roman_char = input("Enter a roman number: ").upper()

if (roman_char.count("V") > 1):
    print("Invalid")
elif (roman_char.count("M") > 3):
    print("Invalid")
elif (roman_char.count("C") > 3):
    print("Invalid")
elif (roman_char.count("I") > 3):
    print("Invalid")
elif (roman_char.count("L") > 1):
    print("Invalid")

else:
    print(roman_to_int(roman_char))