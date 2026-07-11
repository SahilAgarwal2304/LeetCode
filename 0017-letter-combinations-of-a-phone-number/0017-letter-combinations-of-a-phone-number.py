from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        l = [
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z']
        ]

        res = []

        def backtrack(index, path):
            if index == len(digits):
                res.append("".join(path))
                return

            letters = l[int(digits[index]) - 2]
            for ch in letters:
                path.append(ch)
                backtrack(index + 1, path)
                path.pop()

        backtrack(0, [])
        return res