class Converter():

    
    def integer_to_Roman(num):
        """ Convert integers to Roman Numerals"""
        
        num_value = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        roman_value = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
            
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // num_value[i]):
                roman_num += roman_value[i]
                num -= num_value[i]
            i += 1
        return roman_num

    def Roman_to_integer(roman):
        """ Convert Roman Numerals to integers"""

        num_value = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        roman_value = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_dict = dict(zip(roman_value,num_value))
                
        number = 0
        for i in range(len(roman) - 1):
            left = roman[i]
            right = roman[i + 1]
            if roman_dict[left] < roman_dict[right]:
                number -= roman_dict[left]
            else:
                number += roman_dict[left]
            number += roman_dict[roman[-1]]
        return  number
            
if __name__ == '__main__':
    print(Converter.integer_to_Roman(1045))
    print(Converter.Roman_to_integer('MXLV'))