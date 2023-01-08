#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, next, count;
	count = 1;
	scanf("%d", &N);
	next = (((N / 10) + (N % 10)) % 10) + ((N % 10) * 10);
	
	while (N != next)
	{
	    next = (((next / 10) + (next % 10)) % 10) + ((next % 10) * 10);
	    count++;
	}
	printf("%d", count);
}