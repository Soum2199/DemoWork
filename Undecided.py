
n = 4.5
print(" " ,n, "Already have printed \nTry printing" , n+1)
print(type(n))

age = int(input("Enter your age: "))
if age >= 18:
    print (age, " is a legal age")
else:
    print(" Sorry, you're ", age, ", cant vote")
    
print(3 | 4) # 7
print(3 & 4) # 0
print(3 <= 4) # True 
print(2 != 6) # True
print(6+7-8*9/10) # 5.8

arr= {1,2,3,4,5,6,7}
print(arr)
print(arr.pop())
# print(arr.shift())
print("hello world")
mixed = [1, True, "abcd", 3.8, None]
print(mixed)
for i in range(0, 4):
    print(mixed[i])
    print(type (mixed[i]) )
    
   
str = input()
print(str[::-1])