import java.util.*;

class binary_search
{
	public static void main(String[] args) {
int i=0;
int a[]=new int[]{2,3,5,8,11,15};
int n=a.length;
int item=18;
System.out.println(n);
int lb=0;
int ub=n-1;
int mid=lb+ub/2;
System.out.println("lb"+lb);
System.out.println("ub"+ub);
System.out.println("mid"+mid);

while(lb<=ub)
{
	if(a[mid]==item)
	{
		System.out.println("found");
	break;
	}

	if(a[mid]>item)
		{
			ub=mid-1;
		}
			mid=(ub+lb)/2;
	

	if(a[mid]<item)
		{
			lb=mid+1;
		}
			mid=(ub+lb)/2;
	
	
}
if(lb>ub)
{
	System.out.println("not found");
}
}
}
