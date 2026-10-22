rate=300
hours=int(input("enter your hours:"))
if hours<=3:
    rate=300
    print("care rent:",rate)
elif hours<=6:
    rate=500
    print("car rent:",rate)
elif hours<=10:
    rate=800
    print("car rent:",rate)
else :
    rate=1200
    print("orginal rate:",rate)  
if rate>=800:
    discount=rate*10/100
    rate=rate-discount
    print("discount amount:",discount)
    print("total amount:",rate)
