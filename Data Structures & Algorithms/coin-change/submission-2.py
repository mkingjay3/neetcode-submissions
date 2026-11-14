from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        left = amount 
        length = len(coins)

        @cache
        def f(i, left):
            if(left == 0):
                return(0)
            if(left <= 0 or i >= length):
                return(float("inf"))

            take = 1 + f(i, left - coins[i])
            skip = f(i + 1, left)

            return(min(take, skip))
        ans = f(0, amount)
        if ans == float("inf"):
            return -1
        return ans

