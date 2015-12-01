#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int m, n;
  cin >> m >> n;
  int A[m];
  int B[n];
  int i, j;
  int dp[m+1][n+1];
  dp[0][0] = 0;

  // Reading input
  for (i=0; i<m; ++i) {
    cin >> A[i];
    dp[i+1][0] = 0;
  }
  for (j=0; j<n; ++j) {
    cin >> B[j];
    dp[0][j+1] = 0;
  }

  // Filling out DP array
  for (i=1; i<=m; ++i) {
    for (j=1; j<=n; ++j)
      dp[i][j] = (A[i-1]==B[j-1]) ? dp[i-1][j-1]+1 : max(dp[i-1][j],dp[i][j-1]);
  }

  // Getting 1 output
  vector<int> out;
  i = m;
  j = n;
  while (dp[i][j]) {
    if (dp[i-1][j] == dp[i][j]) --i;
    else if (dp[i][j-1] == dp[i][j]) --j;
    else {
      out.push_back(A[i-1]);
      --i;
      --j;
    }
  }
  for (i = dp[m][n]; i>0; --i)
    cout << out[i-1] << " ";
  cout << endl;

  // Print out the dp array
  for (i=1; i<=m; ++i) {
    for (j=1; j<=n; ++j) {
      cout << dp[i][j] << " ";
    }
    cout << endl;
  }

  return 0;
}
