import time

def execution_time(func):
    def wrapper(*args , **kwargs):
        starttime = time.time()
        result = func(*args , **kwargs)
        endtime = time.time()
        print(f"function {func.__name__} took {endtime - starttime} seconds to run")
        return result
    return wrapper



@execution_time
def check(n):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)
    return

def check_2(n):
    print(f"Sleeping for {n} seconds")
    time.sleep(n)
    return

def main():
    check_2(1)
    check(3)
    

if __name__ == "__main__":
    main()