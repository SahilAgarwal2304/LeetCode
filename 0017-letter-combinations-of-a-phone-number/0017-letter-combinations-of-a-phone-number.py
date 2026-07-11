class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f'],
            ['g', 'h', 'i'],
            ['j', 'k', 'l'],
            ['m', 'n', 'o'],
            ['p', 'q', 'r', 's'],
            ['t', 'u', 'v'],
            ['w', 'x', 'y', 'z']
        ]

        ans = []

        def dfs(i, curr):
            if i == len(digits):
                ans.append("".join(curr))
                return

            chars = phone[int(digits[i]) - 2]

            for ch in chars:
                curr.append(ch)
                dfs(i + 1, curr)
                curr.pop()

        dfs(0, [])
        return ans