products=float(input("Enter the no.of products: "))
price=float(input("Enter the price: "))
total=price*products
print("TOTAL COST: ",total)
sgst=total*(2.5/100)
cgst=total*(2.5/100)
print("SGST: ",sgst)
print("CGST: ",cgst)
TWGST=total+sgst+cgst
print("TWGST: ",TWGST)
