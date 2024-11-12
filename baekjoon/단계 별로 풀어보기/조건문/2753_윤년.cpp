#include <stdio.h>
using namespace std;

int main()
{
	int a;
	scanf("%d", &a);
	
	if (!(a % 400)) printf("1");
	else if (!(a % 100)) printf("0");
	else if (!(a % 4)) printf("1");
	else printf("0");
}