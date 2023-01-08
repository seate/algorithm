#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
	int input;
	vector<int> Ns;
	
	while (true){
		scanf("%d", &input);
		if (!input) break;
		Ns.push_back(input);
	}
	
	int prime_limit = *max_element(Ns.begin(), Ns.end()) * 2 + 1;
	bool *save = new bool[prime_limit / 2];
	fill_n(save, prime_limit / 2, true);
	
	for (int i = 3; i < (int)sqrt(prime_limit) + 1; i += 2)
	{
		if (save[i / 2]){
			int k = i * i;
			for (int j = k / 2; j < prime_limit / 2; j += i) save[j] = false;
		}
	}
	
	vector<int> primes;
	primes.push_back(2);
	for (int i = 1; i < prime_limit / 2; i++){
		if (save[i] == true) primes.push_back(2 * i + 1);
	}
	
	int start, end, left, right, mid;
	for (auto n : Ns){
		start = n;
		left = 0;
		right = primes.size() - 1;
		while (left <= right){
			mid = left + (right - left) / 2;
			if (primes[mid] == start){
				mid++;
				break;
			}
			else if (primes[mid] < start) left = mid + 1;
			else right = mid - 1;
		}
		if (primes[mid] <= start) mid++;
		start = mid;
		
		end = 2 * n;
		left = 0;
		right = primes.size() - 1;
		while (left <= right){
			mid = left + (right - left) / 2;
			if (primes[mid] == end){
				mid++;
				break;
			}
			else if (primes[mid] < end) left = mid + 1;
			else right = mid - 1;
		}
		if (end < primes[mid]) mid--;
		end = mid;
		
		printf("%d\n", end - start + 1);
	}
}