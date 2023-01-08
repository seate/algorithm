#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int command;
	int result = 1;
	int counter[10] = {0,};
	
	for (int i = 0; i < 3; i++)
	{
	    scanf("%d", &command);
	    result *= command;
	}
	
	while (result != 0)
	{
	    counter[result % 10]++;
	    result /= 10;
	}
	
	for (int i = 0; i < 10; i++) printf("%d\n", counter[i]);
}