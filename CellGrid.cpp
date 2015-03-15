#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/* Hold cell info */
typedef struct cell_t cell_t;
struct cell_t {
  int val = 0;
  int reg_index = 0;
};

/* Connect to existing region */


int main() {
  vector<int> regions;
  int m, n;
  int i, j;

  regions.push_back(0);
  int nextReg = 1;
  cin >> m >> n;

  /* Get all data */
  cell_t grid[m][n];
  for (i=0; i<m; i++) {
    for (j=0; j<n; j++) {
      cin >> grid[i][j].val;
    }
  }

  /* Go through again to find regions */
  for (i=0; i<m; i++) {
    for (j=0; j<n; j++) {

      /* Found cell with value 1 */
      if (grid[i][j].val == 1) {
        if (!grid[i][j].reg_index)
          grid[i][j].reg_index = nextReg++;
        if (i<m) {
          grid[i+1][j].reg_index
          if (j<n) {


  return 0;
}
