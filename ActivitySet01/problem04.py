# Conditional Execution

#hrs = input("Enter hours? ")
hrs=float(input("input hours\n"))
rate=float(input("enter rate\n"))

if hrs<=40:
    pay=hrs*rate  
    print(pay)
else:
    ovrhrs=(hrs-40)
    regular=rate*40
    othrs=ovrhrs*(rate*1.5)
    ovrpay=(regular+othrs)
    print(ovrpay)
 