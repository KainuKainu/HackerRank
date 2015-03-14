#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  string in_num;
  bool kapFound = false;
  bool i_found;
  unsigned long long min, max, i, j, square;
  unsigned long long l1, l2;                 // first and second half
  unsigned long long divPow;
  unsigned long long numLen;

  /* Get range values */
  getline(cin, in_num);
  min = (unsigned long long) stol(in_num);
  getline(cin, in_num);
  max = (unsigned long long) stol(in_num);

  /* Loop through all integers in range */
  for (i = min; i <= max; i++) {
    i_found = false;
    numLen = (to_string(i)).length();
    square = i*i;
    divPow = (unsigned long long) pow(10, numLen);
    l2 = square % divPow;
    l1 = (square - l2)/divPow;
    if ( l2 && (i == l1 + l2) )
      i_found = true;
    else {
      for (j = 1; (j <= numLen) && (l1%10 == 0); j++) {
        l1 /= 10;
        if ( i == l1 + l2 )
          i_found = true;
      }
    }
    if (!i_found) {
      divPow /= 10;
      l2 = square % divPow;
      if (l2) {
        l1 = (square - l2)/divPow;
        if ( i == l1 + l2 )
          i_found = true;
      }
    }

    if (i_found) {
      kapFound = true;
      cout << i;
      if (i != max)
        cout << ' ';
      continue;
    }
  }

  if (!kapFound)
    cout << "INVALID RANGE";
  cout << '\n';

  return 0;
}
