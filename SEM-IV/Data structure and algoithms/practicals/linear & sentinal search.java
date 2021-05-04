import java.util.*;
class Ha
{
  public static void main(String args[])
  {
int arr[]=new int[5];
arr[0]=1;
arr[1]=10;
arr[2]=11;
arr[3]=23;
arr[4]=25;
/*
//linear search
int flag=0;
for(int i=0;i<=4;i++)
{
 if(arr[i]==11)
 {
  flag=1;
 }
}
if(flag==1)
{
System.out.println("T");
}
else
{
System.out.println("F");
}
//sentinal search
int n=0,i=0;
int item=14,last;
last=arr[4];
arr[4]=item;
for(i=0;i<=4;i++)
{
while(arr[i]!=arr[4])
 {
   n++;
   i++;
 }
if(i<3 || arr[4]==last)
 {
System.out.println("Found");
 }
else
 {
System.out.println("Not Found");
 }
 }
*/
//binary search
int lb=0,ub=4,mb,item=14;
mb=(lb+ub)/2;
while(lb<=ub)
 {
   if(arr[mb]==item)
    {
      System.out.println("Found");
      break;
    }
    if(arr[mb]>item)
    {
      ub=mb-1;
    }
    if(arr[mb]<item)
    {
      lb=mb+1;
    }
 }
 if(lb>ub)
  {
    System.out.println(" Not Found");
  }
}
}
