#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int N;
	scanf("%d", &N);
	int *score = new int[N];
	
	int sum = 0;
	int max = 0;
	for (int i = 0; i < N; i ++)
	{
	    scanf("%d", &score[i]);
	    if (max < score[i]) max = score[i];
	    sum += score[i];
	}
	printf("%lf", (float)(sum) / (max * N) * 100);
}