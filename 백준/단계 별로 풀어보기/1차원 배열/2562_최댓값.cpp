#include <iostream>
#include <vector>
using namespace std;

int main()
{
	int command, index;
	int max = 0;
	for (int i = 1; i <= 9; i++)
	{
	    scanf("%d", &command);
	    if (max < command)
	    {
	        max = command;
	        index = i;
	    }
	}
	printf("%d\n%d", max, index);
}