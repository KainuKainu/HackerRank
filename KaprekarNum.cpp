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
  unsigned long min, max, i, square;
  unsigned long l1, l2;                 // first and second half
  unsigned long divPow;
  unsigned long numLen;

  /* Get range values */
  getline(cin, in_num);
  min = (unsigned long) stol(in_num);
  getline(cin, in_num);
  max = (unsigned long) stol(in_num);

  /* Loop through all integers in range */
  for (i = min; i <= max; i++) {
    numLen = (to_string(i)).length();
    square = i*i;
    divPow = (unsigned long) pow(10, numLen);
    l2 = square % divPow;
    l1 = (square - l2)/divPow;
    if ( i == l1 + l2 ) {
      kapFound = true;
      cout << i;
      if (i != max)
        cout << ' ';
    }
  }

  if (!kapFound)
    cout << "INVALID RANGE";
  cout << '\n';

  return 0;
}
