from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        if len(strs) == 0:
            return ""

        # find shortest string
        shortest_str = strs[0]
        for strings in strs:
            if len(strings) < len(shortest_str):
                shortest_str = strings
        
        print(f"shortest string -> {shortest_str}")

        for i , ch in enumerate(shortest_str):
            for st in strs:
                if ch != st[i]:
                    return shortest_str[0:i]
        
        return shortest_str
    
    def longest_common_prefix_optimized(self , strs: List[str]) -> str:
        if not strs:
            return ""

        if len(strs) == 1:
            return strs[0]
        
        shortest_string = min(strs)
        largest_string = max(strs)

        for i , ch in enumerate(shortest_string):
            if ch != largest_string[i]:
                return shortest_string[:i]

        return shortest_string
    
def main():
    sol = Solution()
    strs = ["flower","flow","flight"]

    longest_prefix = sol.longestCommonPrefix(strs)
    print(f"longest prefix -> {longest_prefix}")

    print("----------------------------------------")

    longest_prefix = sol.longest_common_prefix_optimized(strs)
    print(f"longest prefix optimized -> {longest_prefix}")

if __name__ == "__main__":
    main()