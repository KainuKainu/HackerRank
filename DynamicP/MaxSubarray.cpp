#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int max_cont(int N, int array[]) {
  int best_sum = 0;
  int best_x = 0;
  int best_y = 0;
  int curr = 0;
  int curr_index = -1;
  int temp;
  int i;

  /* Check if all negative */
  int maxVal = array[0];
  bool neg = true;
  for (i = 0; i < N; ++i) {
    if (array[i] > 0) {
      neg = false;
      break;
    }
    maxVal = max(maxVal, array[i]);
  }
  if (neg) return maxVal;

  /* At least 1 positive element */
  for (i = 0; i < N; ++i) {
    temp = curr + array[i];
    if (temp > 0) {
      if (curr == 0) curr_index = i;
      curr = temp;
    }
    else curr = 0;
    if (curr > best_sum) {
      best_sum = curr;
      best_x = curr_index;
      best_y = i;
    }
  }

  /* Debug msg */
  cerr << "best_x = " << best_x << "; best_y = " << best_y << "\n";
  return best_sum;
}

int max_noncont(int N, int array[]) {
  int best_sum = array[0];
  int curr = array[0];
  int temp;
  for (int i = 1; i < N; ++i) {
    temp = (curr >= 0) ? curr + array[i] : array[i];
    if (temp > curr) curr = temp;
    if (curr > best_sum) best_sum = curr;
  }
  return best_sum;
}

int main() {
  int curr = 0;

  /* Read inputs */
  int T, N, i, j;
  cin >> T;
  for (i = 0; i < T; ++i) {
    //Get each test case
    cin >> N;
    int array[N];
    for (j = 0; j < N; ++j) {
      cin >> array[j];
      curr += array[j];
    }
    //Contiguous subarray
    cout << max_cont(N, array) << " ";
    //Non-contiguous subarray
    cout << max_noncont(N, array) << "\n";
  }

  return 0;
}
