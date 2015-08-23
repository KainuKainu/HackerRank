#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <climits>

#define MAX_ANS 200000

using namespace std;

int main() {
  int i, j, k, curr;
  int ans = MAX_ANS;

  /* Read inputs */
  int N, K;
  cin >> N >> K;

  int dp[K][N];
  vector< vector<int> > array;
  for (i=0; i<K; i++) {
    array.push_back(*(new vector<int>));
    for (j=0; j<N; j++) {
      cin >> curr;
      array[i].push_back(curr);
      if (!i)
        minVal += curr;
    }
  }

  return ans;
}
