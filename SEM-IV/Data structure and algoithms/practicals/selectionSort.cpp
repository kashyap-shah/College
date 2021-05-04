#include <iostream>

using namespace std;

int main()
{
	int arr[] = {64, 25, 12, 22, 11};
    int n =5;

    int i, j, min,temp;

    for (i = 0; i < n-1; i++)
    {
        min = i;
        for (j = i+1; j < n; j++)
        {
        if (arr[j] < arr[min])
            min= j;
        }
        temp=arr[i];
        arr[i]=arr[min];
        arr[min]=temp;
    }
    for(int m=0;m<n;m++)
    {
     cout<<arr[m]<<",";
    }
}
