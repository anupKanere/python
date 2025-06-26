from datetime import datetime
import timeit

class Reverse:
    def reverse(self , string : str) -> str:
        return string[::-1]
    
    def _reverse(self , string : str) -> str:
        rev_str = ""
        for i in range(len(string) - 1 , -1 , -1):
            rev_str += string[i]
        return rev_str
    

if __name__ == "__main__":
    name = "Anup"
    rev = Reverse()

    # Benchmark slicing method
    time_slicing = timeit.timeit(lambda: rev.reverse(name), number=100000)
    print(f"Time for slicing method: {time_slicing:.10f} seconds")
    
    # Benchmark loop method
    time_loop = timeit.timeit(lambda: rev._reverse(name), number=100000)
    print(f"Time for loop method: {time_loop:.10f} seconds")

