class Solution:
    def intToRoman(self, number: int) -> str:
        num = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        sym = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        l = []
        while number:
            div = number // num[i]
            number %= num[i]

            while div:
                l.append(sym[i])
                div -= 1
            i -= 1
        return "".join(l)