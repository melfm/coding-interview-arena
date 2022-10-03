def generateParenthesis(self, n: int) -> List[str]:
    """Given n pairs of parentheses, write a function to
        generate all combinations of well-formed parentheses.
    """

    def generate(result=[]):

        if len(result) == n * 2:
            # check if valid
            if is_valid(result):
                answer.append("".join(result))

        else:
            result.append('(')
            generate(result)
            result.pop()
            result.append(')')
            generate(result)
            result.pop()

    def is_valid(result):
        balanced = 0

        for char in result:
            if char == '(':
                balanced += 1
            else:
                balanced -= 1

            if balanced < 0: return False
        return balanced == 0

    answer = []
    generate()
    return answer

# Backtracking
def generateParenthesis(self, n: int) -> List[str]:
    ans = []
    def backtrack(S = [], left = 0, right = 0):
        if len(S) == 2 * n:
            ans.append("".join(S))
            return
        if left < n:
            S.append("(")
            backtrack(S, left+1, right)
            S.pop()
        if right < left:
            S.append(")")
            backtrack(S, left, right+1)
            S.pop()
    backtrack()
    return ans