#include <stdio.h>
using namespace std;

int main()
{
	int a, b, c;
	scanf("%d %d %d", &a, &b, &c);
	int fir = (a + b) % c, sec = (a * b) % c;
	printf("%d\n%d\n%d\n%d\n", fir, fir, sec, sec);
}