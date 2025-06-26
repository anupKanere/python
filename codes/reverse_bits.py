class Solution:
    def reverseBits(self, n: int) -> int:
        bin_rep = bin(n)[2:]
        print(f"bin 1 =  {bin_rep}")

        bin_rep = bin_rep.zfill(32)
        print(f"bin 2 =  {bin_rep}")

        rev_bin =bin_rep[::-1]
        print(f"bin 3 =  {rev_bin}")

        return int(rev_bin,2)

        
if __name__ == "__main__":
    solution = Solution()
    # input = 00000010100101000001111010011100
    input = int("00000010100101000001111010011100" , 2)  
    print(f"input = {input}")
    rev_num = solution.reverseBits(input)

    print(f"Rev number = {bin(rev_num)}")
    print(f"rev number int = {rev_num}")

