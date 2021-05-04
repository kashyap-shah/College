#include <iostream>

using namespace std;


int main()
{
	int arr[20];
	int data[10]={1,4,8,17,13,22,26,37,47,58};
	/*arr[0]=0;
	arr[1]=1;
	for(int i=1;i<20;i++)
	{
      arr[i+2]=arr[i]+arr[i+1];
	}
	*/
    int key=8;
	int fbn=21,fbn1=13,fbn2=8;
    while(fbn>1)
    {
    int offset=0;
     if(key==arr[fbn+offset])
     {
      cout<<"found";
      break;
     }
     if(key>arr[fbn+offset])
     {
      fbn=fbn2+fbn;
      fbn1=fbn1+fbn2;
      fbn2=fbn-fbn1;
     }
     offset=fbn1+1;
     if(key<arr[fbn+offset])
     {
      fbn=fbn1;
      fbn1=fbn-fbn2;
      fbn2=fbn-fbn1;
     }
    }
}
