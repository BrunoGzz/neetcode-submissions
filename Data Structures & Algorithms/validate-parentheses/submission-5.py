class Solution:
    def isValid(self, s: str) -> bool:
        brackets = "([{)]}"

        last_open = []

        counter = 0

        for c in s:
            if c in brackets[:3]:
                last_open.append(c)
            elif c in brackets[3:]:
                if not last_open or last_open[-1] != brackets[brackets.index(c)-3]:
                    return False
                else:
                    last_open.pop()
        return False if last_open != [] else True