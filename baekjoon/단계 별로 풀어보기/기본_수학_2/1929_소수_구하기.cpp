#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int start, end, sq_end;
	cin >> start >> end;
	end++;
	
	bool *save = new bool[end / 2];
	fill_n(save, end / 2, true);
	
	for (int i = 3; i < (int)sqrt(end) + 1; i += 2)
	{
		if (save[i / 2]){
			int k = i * i;
			for (int j = k / 2; j < end / 2; j += i) save[j] = false;
		}
	}
	
	vector<int> primes;
	primes.push_back(2);
	for (int i = 1; i < end / 2; i++){
		if (save[i] == true) primes.push_back(2 * i + 1);
	}
	
	int idx;
	for (idx = 0; idx < primes.size(); idx++){
		if (start <= primes[idx]) break;
	}
	
	for (; idx < primes.size(); idx++) cout << primes[idx] << '\n';
}