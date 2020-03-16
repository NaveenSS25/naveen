products=float(input("Enter the no.of products: "))
price=float(input("Enter the price: "))
total=price*products
print("TOTAL COST: ",total)
sgst=total*(2.5/100)
cgst=total*(2.5/100)
print("SGST: ",sgst)
print("CGST: ",cgst)
TWGST=total+sgst+cgst
print("Total With GST: ",TWGST)
from num2words import num2words
print(num2words(TWGST to ='currency'))




import java.util.*;
public class Main
{
	public static void main(String[] args)
	{
	    int sum,a,b,c,d,e,f;
	    Scanner s=new Scanner(System.in);
	    a=s.nextInt();
	    sum=a%10;
	    b=a/10;
	    c=b+sum;
	    d=c%10;
	    e=c/10;
	    f=d+e;
		System.out.println("" + f);
	}
}
