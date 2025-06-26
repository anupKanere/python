class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        prev1 = 1
        prev2 = 2

        for i in range(3 ,  n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return prev2
        
def main():
    sol = Solution()
    res = sol.climbStairs(5)
    print(f"res -> {res}")

if __name__ == "__main__":
    main()