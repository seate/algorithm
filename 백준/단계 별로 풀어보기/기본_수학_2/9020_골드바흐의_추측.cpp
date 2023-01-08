#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <set>
using namespace std;

int main()
{
	int T, input;
	scanf("%d", &T);
	
	vector<int> Q;
	while (T--){
	    scanf("%d", &input);
	    Q.push_back(input);
	}
	
	int end = *max_element(Q.begin(), Q.end()) + 1;
	bool *save = new bool[end / 2];
	fill_n(save, end / 2, true);
	
	for (int i = 3; i < (int)sqrt(end) + 1; i += 2)
	{
		if (save[i / 2]){
			int k = i * i;
			for (int j = k / 2; j < end / 2; j += i) save[j] = false;
		}
	}
	
	set<int> primes;
	for (int i = 1; i < end / 2; i++){
		if (save[i] == true) primes.insert(2 * i + 1);
	}
	
	unsigned int half, start;
	for (unsigned int each : Q){
	    if (each == 4){
	        cout << "2 2\n";
	        continue;
	    }
	    half = each / 2;
	    if (!(half & 1)) start = 1;
	    else start = 0;
	    
	    for (int i = start; i < half; i += 2){
	        if (primes.count(half - i) == 1 and primes.count(half + i) == 1){
	            printf("%d %d\n", half - i, half + i);
	            break;
	        }
	    }
	}
}