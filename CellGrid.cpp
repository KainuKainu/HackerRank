#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/* Hold region info */
typedef struct reg_t reg_t;
struct reg_t {
  int sum = 0;
};

/* Hold cell info */
typedef struct cell_t cell_t;
struct cell_t {
  int val = 0;
  reg_t * conReg = NULL;

  /* Pointers to linkable cells */
  cell_t * top_left = NULL;
  cell_t * top_right = NULL;
  cell_t * top = NULL;
  cell_t * left = NULL;
  cell_t * right = NULL;
};

int main() {
  vector<reg_t*> regions;
  unsigned int m, n;
  unsigned int i, j;
  int max;
  cell_t * thisCell;
  reg_t * thisReg;
  reg_t * rightCellReg;
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
          if (j<n-1)
            thisCell->top_right = &grid[i-1][j+1];
        }
        if (j>0)
          thisCell->left = &grid[i][j-1];
        if (j<n-1)
          thisCell->right = &grid[i][j+1];

        /* Update connected region */
        thisReg = thisCell->conReg;
        if ( (thisCell->top_left != NULL) && (thisCell->top_left->val == 1) )
          thisReg = thisCell->top_left->conReg;
        else if ( (thisCell->top != NULL) && (thisCell->top->val == 1) )
          thisReg = thisCell->top->conReg;
        else if ( (thisCell->left != NULL) && (thisCell->left->val == 1) )
          thisReg = thisCell->left->conReg;

        if (thisReg != NULL) {
          thisCell->conReg = thisReg;
          thisReg->sum += 1;
        }
        else {
          regions.push_back(new reg_t());
          thisCell->conReg = regions.back();
          thisCell->conReg->sum += 1;
          thisReg = thisCell->conReg;
        }

        /* Top right cell check */
        if ( (thisCell->top_right != NULL) && (thisCell->top_right->val == 1) ){
          rightCellReg = thisCell->top_right->conReg;
          thisReg->sum += rightCellReg->sum;
          thisCell->top_right->conReg = thisReg;
          if ( (thisCell->top_right->right != NULL) &&
            (thisCell->top_right->right->val == 1) )
            thisCell->top_right->right->conReg = thisReg;
        }

      }
    }
  }

  /* Pick out largest region */
  max = 0;
  for (i=0; i < regions.size(); i++) {
    if (regions[i]->sum > max)
      max = regions[i]->sum;
  }

  cout << max << '\n';

  return 0;
}
