

array = [10,20,30,40,50,60,70,80,90,100]

# for i in range(5):
#     print(i)
    
# for key , val in enumerate(array):
#     print(f"key -> {key} |  val-> {val}")

arr2 = [11,22,33,44,55,66,77,88,99]

array.extend(arr2)
print(array)

array.insert(1, 123456)
array.insert(2, 123456)

print(array)

array.remove(123456)
print(array)

last_num = array.pop()
print(last_num)

array.pop(1)
print(array)


i = array.index(77)
print(i)


array.sort()
print(array)

array.sort(reverse=True)
print(array)

sub_arr = array[1:5]
print(sub_arr)

arr = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(arr)

arr = [1,2,3,4,5,6]
filtered = [x for x in arr if x % 2 == 0]
print(filtered)

#mapping :

square = list(map(lambda x : x**2 , arr))
print(square)

arr2 = arr.copy()
check = list(map(lambda x , y : x + y , arr , arr2 ))
print(check)

#Reduce function
from functools import reduce
sum = reduce(lambda x , y : x + y , arr)
print(sum)