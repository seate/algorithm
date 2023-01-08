#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	int remain[42]{0,};
	int command;
	int sum = 0;
	
	for (int i = 0; i < 10; i++)
	{
	    scanf("%d", &command);
	    remain[command % 42] = 1;
	}
	for (int i = 0; i < 42; i++) sum += remain[i];
	printf("%d", sum);
}