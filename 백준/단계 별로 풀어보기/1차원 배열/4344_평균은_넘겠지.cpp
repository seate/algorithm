#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
    cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	cout << fixed;
	cout.precision(3);
	
	int T, N, sum, counter;
	float average;
	cin >> T;
	
	
	
	for (int i = 0; i < T; i++)
	{
	    sum = 0;
	    counter = 0;
	    
	    cin >> N;
	    int *data = new int[N];
	    
	    for (int j = 0; j < N; j++)
	    {
	        cin >> data[j];
	        sum += data[j];
	    }
	    
	    average = (float)(sum) / N;
	    
	    for (int j = 0; j < N; j++)
	    {
	        if (average < data[j]) counter++;
	    }
	    
	    cout << (float)(counter) / N * 100 << '%' << '\n';
	}
	
}