#include <stdio.h>
using namespace std;

int main()
{
	int a, b;
	scanf("%d\n%d", &a, &b);
	
	if (0 < a)
	{
	    if (0 < b) printf("1");
	    else printf("4");
	}
	else
	{
	    if (0 < b) printf("2");
	    else printf("3");
	}
}