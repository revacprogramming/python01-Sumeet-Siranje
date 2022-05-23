# Loops & Iterators

sum=0
count=0
try:
    while True:
        num=input("enter the number")
               
        if num=="done":
           break
        sum += int(num)
        count+=1
    print(sum, count,sum/count )  
except ValueError:
    print("invalid")
   