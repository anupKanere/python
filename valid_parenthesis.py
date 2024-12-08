class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif not stack:
                return False
            elif (
                ch == ")"
                and stack.pop() != "("
                or ch == "]"
                and stack.pop() != "["
                or ch == "}"
                and stack.pop() != "{"
            ):
                return False

        return len(stack) == 0

    def is_valid_2(self, s: str) -> bool:
        stack = []

        if len(stack) % 2 != 0:
            return False

        bracket_pairs = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch not in bracket_pairs:
                stack.append(ch)
            else:
                if not stack or stack.pop() != bracket_pairs[ch]:
                    return False

        return len(stack) == 0


def main():
    sol = Solution()
    # s = "()"
    s = "()[]{}"
    is_valid = sol.isValid(s)
    print(f"is valid -> {is_valid}")

    is_valid = sol.is_valid_2(s)
    print(f"is valid 2 -> {is_valid}")


if __name__ == "__main__":
    main()
