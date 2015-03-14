#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  bool kapFound = false;
  bool i_found;
  unsigned long min, max, i, j, square;
  unsigned long l1, l2;                 // first and second half
  unsigned long divPow;
  unsigned long sqrLen;

  /* Get range values */
  cin >> min >> max;
  if (min > max) {
    i = min;
    min = max;
    max = i;
  }

  /* Loop through all integers in range */
  for (i = min; i <= max; i++) {
    i_found = false;
    square = i*i;
    sqrLen = (to_string(square)).length();

    divPow = 1;
    for (j = 0; (j < sqrLen) && (!i_found); j++) {
      divPow *= 10;
      l2 = square % divPow;
      if (l2 <= 0)
        continue;
      else {
        l1 = (square - l2) / divPow;
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
