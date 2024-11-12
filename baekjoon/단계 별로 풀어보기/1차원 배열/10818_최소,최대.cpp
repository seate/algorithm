#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int N, command;
	int M = -1000001;
	int m = 1000001;
	scanf("%d", &N);
	for (int i = 0; i < N; i++)
	{
	    scanf("%d", &command);
	    if (command < m) m = command;
	    if (M < command) M = command;
	}
    printf("%d %d", m, M);
}