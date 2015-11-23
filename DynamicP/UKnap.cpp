#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int T, N, S;
  cin >> T;

  int i, j, k;
  for (i=0; i<T; ++i) {
    cin >> N >> S;
    int array[N+1];
    int dp[S+1][N+1];

    array[0] = 0;
    for (j=0; j<=S; ++j)
      dp[j][0] = 0;
    for (j=1; j<=N; ++j){
      cin >> array[j];
      dp[0][j] = 0;
    }

    for (k=1; k<=S; ++k) {
      for (j=1; j<=N; ++j) {
        if (!(k % array[j])) dp[k][j] = k;
        else {
          int tmp = k - array[j];
          tmp = (tmp >= 0) ? dp[tmp][j] : dp[k-1][j];
          int x = ((tmp = tmp + array[j]) <= k) ? tmp : tmp - array[j];
          int y = ((tmp = dp[k][j-1] + array[j]) <= k) ? tmp : tmp - array[j];
          dp[k][j] = max(x, y);
        }
      }
    }

    for (k=1; k<=S; ++k) {
      for (j=1; j<=N; ++j) {
        cout << dp[k][j] << " ";
      }
      cout << endl;
    }

    cout << dp[S][N] << "\n";
  }

  return 0;
}
