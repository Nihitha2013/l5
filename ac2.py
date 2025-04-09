ac=int(input("Enter actual price of item:"))
sc=int(input("Enter sales amount:"))

if sc>ac:
    a=sc-ac
    print("Total Profit:",a)

else:
    l=ac-sc
    print("Total Loss:",l)
