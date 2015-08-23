#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;

const ll INF = 1000000000000ll;

int main() {
  /* Enter your code here. Read input from STDIN. Print output to STDOUT */
  int N, K;
  scanf("%d %d", &N, &K);
  vector<vector<ll>> cost(K);
  for (int i = 0; i < K; ++i) for (int j = 0; j < N; ++j) {
    int x;
    scanf("%d", &x);
    cost[i].push_back(x);
  }
  vector<vector<ll>> DP(1<<K, vector<ll>(N+1, INF));

  for (int i = 0; i < (1<<K); ++i) DP[i][0] = 0;
  for (int j = 1; j <= N; ++j) for (int i = 1; i < (1 << K); ++i) {
    ll ans = INF;
    // select last to kill
    for (int z = 0; z < K; ++z) if ((i >> z) & 1) {
      int rest = i & (~(1<<z));
      // how many did z kill?
      ll temp = 0;
      for (int k = 0; k <= j; ++k) {
        ans = min(ans, temp + DP[rest][j-k]);
        temp += cost[z][j-k-1];
      }
    }
    DP[i][j] = ans;
  }
  cout << DP.back().back() << endl;
  return 0;
}
