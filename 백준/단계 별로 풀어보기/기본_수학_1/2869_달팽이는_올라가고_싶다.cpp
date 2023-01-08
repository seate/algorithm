#include <stdio.h>
#include <cmath>
using namespace std;

int main()
{
	double A, B, V;
	scanf("%lf %lf %lf", &A, &B, &V);
	printf("%.0lf", ceil((V - A) / (A - B)) + 1);
}