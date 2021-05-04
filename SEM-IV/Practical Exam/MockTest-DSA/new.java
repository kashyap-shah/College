import java.util.*;
class insertion_sort
{
	public static void main(String[] args) 
	{
		System.out.println("Consider ACE=1, JACK=11, QUEEN=12, KING=13");
		System.out.println("Enter the size of deck(array) ::");
		Scanner s1=new Scanner(System.in);
		int x=s1.nextInt();

		System.out.println("Enter the card numbers::");
		Scanner s= new Scanner(System.in);
		int[] a=new int[x];
		for(int i=0;i<x;i++)
		{
			a[i]=s.nextInt();
		}

		int i,j;
		int temp;
		for(i=1;i<x;i++)
		{
			temp=a[i];
			for(j=i-1;j>=0 && a[j]>temp;j--)
			{
				a[j+1]=a[j];
			}
			a[j+1]=temp;
		}
		System.out.println("After Sorting cards are::");
		for(i=0;i<x;i++)
		{
			System.out.println(a[i]);
		}
	}
}