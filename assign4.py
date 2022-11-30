
filename=("order.text")
f=open("order.txt", "r")
bill=0

for line in f:
    [name, price1, price2]=line.split()
    price=[price1,price2]
    total=(float(price1)*float(price2))
    print(name,total)
    bill=bill+total
print("please pay",bill)







