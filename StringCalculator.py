import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        delimiter = ','

        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = re.escape(parts[0][2:])
            numbers = parts[1]
        
        numbers = re.split(f"{delimiter}|\n", numbers)
        
        numbers = [int(num) for num in numbers if num]
        
        negatives = [num for num in numbers if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")
        
        return sum(numbers)

calculator = StringCalculator()

print(calculator.add(""))
print(calculator.add("1"))
print(calculator.add("1,2"))
print(calculator.add("1\n2,3"))
print(calculator.add("//;\n1;2"))
try:
    print(calculator.add("1,-2,3,-5"))
except ValueError as e:
    print(e)

