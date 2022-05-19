# Functions


def computepay(hrs,rate):
    payment=float(hrs)*float(rate)
    extrapay=(float(rate)*40)+((float(hrs)-40)*(float(rate)*1.5))
    if(float(hrs)>40):
        return extrapay
    return payment

hrs=float(input("enter the hrs\n"))
rate=float(input("enter the rate\n"))
p=computepay(hrs,rate)
float(p)
print("pay",p)