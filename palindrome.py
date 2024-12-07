class Solution:
    # Current Implementation
    # Time Complexity: O(log n) - where n is the input number
    # Space Complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        org = x
        rev_num = 0
        
        while x > 0:
            rem = x % 10
            rev_num = rev_num * 10 + rem
            x = x // 10
        
        return rev_num == org

    # Optimization 1: Early exit for negative numbers and numbers ending with 0
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def isPalindrome_optimized(self, x: int) -> bool:
        # All negative numbers are not palindromes
        if x < 0:
            return False
            
        # Single digit numbers are always palindromes
        if x < 10:
            return True
            
        # Numbers ending with 0 can't be palindromes unless it's 0
        if x % 10 == 0 and x != 0:
            return False
        
        rev_num = 0
        while x > rev_num:
            rev_num = rev_num * 10 + x % 10
            x = x // 10
            
        # For even length numbers: x == rev_num
        # For odd length numbers: x == rev_num // 10
        return x == rev_num or x == rev_num // 10

    # Optimization 2: String conversion approach (surprisingly efficient for smaller numbers)
    # Time Complexity: O(log n)
    # Space Complexity: O(log n)
    def isPalindrome_string(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
            
        s = str(x)
        return s == s[::-1]

    # Optimization 3: Compare digits directly without full reversal
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def isPalindrome_division(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0 and x != 0:
            return False
            
        # Find the length of the number
        div = 1
        while x // div >= 10:
            div *= 10
            
        while x > 0:
            left = x // div
            right = x % 10
            
            if left != right:
                return False
                
            # Remove leftmost and rightmost digits
            x = (x % div) // 10
            div //= 100
            
        return True
    

def main():
    solution = Solution()
    
    # Test cases
    test_cases = [
        121,  # Palindrome
        -121, # Not a palindrome (negative number)
        10,   # Not a palindrome (ends with 0 but not 0)
        0,    # Palindrome (single digit, special case)
        12321 # Palindrome
    ]
    
    print("Testing `isPalindrome`:")
    for num in test_cases:
        print(f"Is {num} a palindrome? {solution.isPalindrome(num)}")
    
    print("\nTesting `isPalindrome_optimized`:")
    for num in test_cases:
        print(f"Is {num} a palindrome? {solution.isPalindrome_optimized(num)}")
    
    print("\nTesting `isPalindrome_string`:")
    for num in test_cases:
        print(f"Is {num} a palindrome? {solution.isPalindrome_string(num)}")
    
    print("\nTesting `isPalindrome_division`:")
    for num in test_cases:
        print(f"Is {num} a palindrome? {solution.isPalindrome_division(num)}")

if __name__ == "__main__":
    main()
