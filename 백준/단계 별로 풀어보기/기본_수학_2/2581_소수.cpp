#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main()
{
	cin.tie(NULL);
	cout.tie(NULL);
	ios_base::sync_with_stdio(false);
	
	int start, end, idx, S = 0;
	cin >> start >> end;
	vector<int> primes;
	bool *isprime = new bool[end + 1];
	fill_n(isprime, end + 1, true);
	
	for (int i = 2; i <= end; i++)
	{
	    if (!isprime[i]) continue;
	    primes.push_back(i);
	    for (int j = 2 * i; j <= end; j += i) isprime[j] = false;
	}
	
	int L = primes.size();
	
	for (idx = 0; idx < L; idx++)
	{
	    if (start <= primes[idx]) break;
	}
	
	if (L == 0 || primes[L - 1] < start)
	{
	    cout << "-1";
	    return 0;
	}
	
	for (int i = idx; i < L; i++) S += primes[i];
	
	cout << S << '\n' << primes[idx];
}