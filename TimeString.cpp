#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

void printNumber(int num) {     // 0 <= num <= 30
  /* 0 minute */
  if (num == 0) {
    cout << "o' clock";
    return;
  }

  /* halfs and quarters */
  if (num == 15) {
    cout << "quarter";
    return;
  }
  if (num == 30) {
    cout << "half";
    return;
  }

  int one_digit = num%10;
  int ten_digit = num/10;

  /* Print tens */
  switch (ten_digit) {
    case 0: break;
    case 1:
      switch (one_digit) {
        case 0:
          cout << "ten";
          break;
        case 1:
          cout << "eleven";
          break;
        case 2:
          cout << "twelve";
          break;
        case 3:
          cout << "thirteen";
          break;
        case 4:
          cout << "fourteen";
          break;
        case 5:
          cout << "fifteen";
          break;
        case 6:
          cout << "sixteen";
          break;
        case 7:
          cout << "seventeen";
          break;
        case 8:
          cout << "eighteen";
          break;
        case 9:
          cout << "nineteen";
          break;
      }
      break;
    case 2:
      cout << "twenty";
      break;
  }

  /* Print ones */
  if (ten_digit != 1) {
    switch (one_digit) {
      case 0: break;
      case 1:
        cout << "one";
        break;
      case 2:
        cout << "two";
        break;
      case 3:
        cout << "three";
        break;
      case 4:
        cout << "four";
        break;
      case 5:
        cout << "five";
        break;
      case 6:
        cout << "six";
        break;
      case 7:
        cout << "seven";
        break;
      case 8:
        cout << "eight";
        break;
      case 9:
        cout << "nine";
        break;
    }
  }
}

int main() {
  int hr, min;
  int p_hr, p_min;
  string p_loc;

  cin >> hr >> min;

  if (!min) {
    printNumber(hr);
    cout << ' ';
    printNumber(min);
    return 0;
  }

  if (min <= 30) {
    p_min = min;
    p_hr = hr;
    p_loc = " past ";
  }
  else {
    p_min = 60 - min;
    p_hr = hr+1;
    p_loc = " to ";
  }

  printNumber(p_min);
  if (p_min == 1)
    cout << " minute";
  else if ( (p_min != 15) && (p_min != 30) )
    cout << " minutes";
  printNumber(p_hr);

  return 0;
}
