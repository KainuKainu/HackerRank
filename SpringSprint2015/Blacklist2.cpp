#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

static int minVal;
static int N, K;

void findSmallest(vector< vector<int> >* data, int preVal,
                    int nextK, int nextN) {
  int i, j;
  int val = preVal + (*data)[nextK][nextN];

  /* If last column and row, just return */
  if (nextN == N-1 && nextK == K-1) {
    if (val < minVal)
      minVal = val;
    return;
  }

  /* Loop thru the same row while recursing to next K */
  for (i = nextN; i < N; i++) {
    if (nextK == K-1)
  }

}

int main() {
  int i, j, curr;
  minVal = 0;

  /* Read inputs */
  cin >> N >> K;
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

  /* Calculate routes */
  for (i=0; i<K; i++) {
    if (i)
      array[i].swap(array[0]);
    findSmallest(&array, 0, 0, 0);
  }

  cout << minVal << '\n';

  return 0;
}
