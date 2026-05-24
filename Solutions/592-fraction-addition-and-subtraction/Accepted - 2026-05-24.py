class Solution:
    def fractionAddition(self, expression: str) -> str:
        if len(expression) % 4 != 0:
            expression = "+" + expression
        nume = []
        deno = []
        denominator = 1
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)
        for i in range(len(expression)):
            if expression[i] in "+-":
                nume.append(int(expression[i: i+2]))
            if expression[i] == "/":
                deno.append(int(expression[i + 1]))
                denominator = lcm(denominator, deno[-1])
        numerator = 0
        for i in range(len(deno)):
            numerator += (denominator/deno[i]) * nume[i]
        numerator = int(numerator)
        return f"{int(numerator/math.gcd(numerator, denominator))}/{int(denominator/math.gcd(numerator, denominator))}"