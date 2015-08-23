#include <iostream>
#include <cstdio>
#include <cstring>
#include <climits>
#include <algorithm>
#include <vector>

using namespace std;

int mat[11][21];    // input matrix
int sum[11][21];    // sum!
int dp[11][21];
int best[11][21];   // best route
int id[11];         // targets' ID

int main() {
  int n, m;
  cin >> m >> n;

  for (int i = 1; i <= n; ++i) {
    sum[i][0] = 0;
    for (int j = 1; j <= m; ++j) {
      cin >> mat[i][j];
      sum[i][j] = sum[i][j - 1] + mat[i][j];
    }
  }

  for (int i = 0; i < n; ++i) {
    id[i] = i + 1;
  }

  int ans = INT_MAX;
  do {
    dp[0][0] = 0;
    for (int j = 0; j <= m; ++j)
      best[0][j] = 0;

    for (int i = 1; i <= n; ++i) {
      for (int j = 0; j <= m; ++j) {
        dp[i][j] = best[i - 1][j] + sum[id[i - 1]][j];
        if (i < n) {
          best[i][j] = dp[i][j] - sum[id[i]][j];
          if (j) {
            best[i][j] = min(best[i][j], best[i][j - 1]);
          }
        }
      }
    }
    ans = min(ans, dp[n][m]);
  } while (next_permutation(id, id + n));

  printf("%d\n", ans);
}
