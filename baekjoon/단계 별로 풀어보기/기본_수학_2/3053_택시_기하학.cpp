#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	double N, PI = 3.141592653589793;
	scanf("%lf", &N);
	N *= N;
	printf("%.5lf\n%.5lf", PI * N, 2 * N);
}