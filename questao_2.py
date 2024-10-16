# ORIENTADO A OBJETO - Desenvolva um conversor de números romanos para decimais e vice-versa. O programa  deve lidar com números de 1 a 3999. Implemente funções separadas para cada direção  de conversão e inclua verificações de entrada válida.

class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    
    def roman_to_decimal(self, roman):
        if not self.is_valid_roman(roman):
            return "Número romano inválido."
        
        decimal = 0
        prev_value = 0
        for numeral in reversed(roman):
            value = self.roman_numerals[numeral]
            if value < prev_value:
                decimal -= value
            else:
                decimal += value
            prev_value = value
        
        return decimal
    
    def decimal_to_roman(self, decimal):
        if not self.is_valid_decimal(decimal):
            return "Número decimal inválido."
        
        roman = ''
        value_map = [
            ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
            ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
            ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)
        ]
        for numeral, value in value_map:
            while decimal >= value:
                roman += numeral
                decimal -= value
        
        return roman
    
    def is_valid_roman(self, roman):
        return all(numeral in self.roman_numerals for numeral in roman)
    
    def is_valid_decimal(self, decimal):
        return 1 <= decimal <= 3999
    
    def convert(self):
        print("Bem-vindo ao conversor de números romanos!")
        print("Digite '1' para converter de romano para decimal.")
        print("Digite '2' para converter de decimal para romano.")
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            roman = input("Digite um número romano: ")
            decimal = self.roman_to_decimal(roman)
            print(f"O número romano '{roman}' é equivalente a {decimal}.")
        elif choice == '2':
            decimal = int(input("Digite um número decimal: "))
            roman = self.decimal_to_roman(decimal)
            print(f"O número decimal {decimal} é equivalente a '{roman}'.")
        else:
            print("Opção inválida. Tente novamente.")
            self.convert()
        
        print("Obrigado por usar o conversor de números romanos!")
        
if __name__ == '__main__':
    converter = RomanNumeralConverter()
    converter.convert()
