#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    int x, y, w, h, mini;
	scanf("%d %d %d %d", &x, &y, &w, &h);
	
	mini = x;
	if (y < mini) mini = y;
	if (w - x < mini) mini = w - x;
	if (h - y < mini) mini = h - y;
	
	printf("%d", mini);
}