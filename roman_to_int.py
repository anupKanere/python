class Solution:
    def romanToInt(self, s: str) -> int:

        map_obj = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        total = 0
        prev_val = 0
        for ch in reversed(s):
            curr_val = map_obj.get(ch)

            if curr_val < prev_val:
                total -= curr_val
            else:
                total += curr_val
            
            prev_val = curr_val
        
        return total

    # Good for longer Roman numerals
    # Time Complexity: O(1) since Roman numerals have a maximum length
    # Space Complexity: O(1)
    def romanToInt_replacement(self, s: str) -> int:
        # Replace subtraction cases with addition equivalents
        s = (s.replace('IV', 'IIII')
             .replace('IX', 'VIIII')
             .replace('XL', 'XXXX')
             .replace('XC', 'LXXXX')
             .replace('CD', 'CCCC')
             .replace('CM', 'DCCCC'))
        
        # Simple addition
        return (s.count('I') * 1 +
                s.count('V') * 5 +
                s.count('X') * 10 +
                s.count('L') * 50 +
                s.count('C') * 100 +
                s.count('D') * 500 +
                s.count('M') * 1000)
    
def main():
    sol = Solution()
    print("***********ROMAN TO INTEGER CONVERSION***********")

    roman = "XL"
    num = sol.romanToInt(roman)
    print(f"Roman -> {roman} \nInteger -> {num}")

    print("---------------------------------")

    roman = "LVIII"
    num = sol.romanToInt_replacement(roman)
    print(f"Roman -> {roman} \nInteger -> {num}")



if __name__ == "__main__":
    main()
