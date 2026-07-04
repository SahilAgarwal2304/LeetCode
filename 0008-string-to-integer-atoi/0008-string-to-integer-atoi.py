class Solution:
    def myAtoi(self, s: str) -> int:
        ns = s.lstrip()

        if not ns:
            return 0

        sign = 1
        i = 0

        if ns[0] == "-":
            sign = -1
            i = 1
        elif ns[0] == "+":
            i = 1

        num = 0

        while i < len(ns) and ns[i].isdigit():
            num = num * 10 + int(ns[i])
            i += 1

        num *= sign

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX

        return num