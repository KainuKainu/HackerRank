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
  int reg_index = -1;

  /* Pointers to linkable cells */
  cell_t * top_left = NULL;
  cell_t * top_right = NULL;
  cell_t * top = NULL;
  cell_t * left = NULL;
};

int main() {
  vector<int> regions;
  unsigned int m, n;
  unsigned int i, j;
  int max;
  cell_t * thisCell;
  int thisReg;
  int nextReg = 0;
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
      thisCell = &grid[i][j];

      /* Found cell with value 1 */
      if (thisCell->val == 1) {

        /* Get adjacent cells */
        if ( i>0 && j>0 )
          thisCell->top_left = &grid[i-1][j-1];
        if (i>0) {
          thisCell->top = &grid[i-1][j];
          if (j<n)
            thisCell->top_right = &grid[i-1][j+1];
        }
        if (j>0)
          thisCell->left = &grid[i][j-1];

        /* Update connected region */
        if ( (thisCell->top_left != NULL) && (thisCell->top_left->val == 1) )
          thisReg = thisCell->top_left->reg_index;
        else if ( (thisCell->top != NULL) && (thisCell->top->val == 1) )
          thisReg = thisCell->top_left->reg_index;
        else if ( (thisCell->left != NULL) && (thisCell->left->val == 1) )
          thisReg = thisCell->left->reg_index;

        if (thisReg != -1) {
          thisCell->reg_index = thisReg;
          regions[thisReg]++;
        }
        else {
          regions.push_back(-1);
          regions[nextReg]++;
          nextReg++;
        }

      }
    }
  }

  /* Pick out largest region */
  max = 0;
  for (i=0; i < regions.size(); i++) {
    if (regions[i] > max)
      max = regions[i];
  }

  cout << max << '\n';

  return 0;
}
