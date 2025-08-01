A=float(input("enter value"))
B=float(input("enter value"))
print("Select +, -, *, /" )
operator=input("enter operator")
if operator=="+":
    print(A+B)
elif operator=="-":
    print(A-B)
elif operator=="*":
    print(A*B)
elif operator=="/":
    print(A/B)
else:
    print("invalid operator")