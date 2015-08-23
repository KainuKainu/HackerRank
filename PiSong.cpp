#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

int main() {
  unsigned int i, j, count;
  char currentChar;
  string input_line, inSong;
  const string piNum = "31415926535897932384626433833\n";

  /* Get number of tests */
  getline(cin, input_line);
  unsigned long numTest = (unsigned long) stol(input_line);
  int outputSong[numTest];
  for (i=0; i < numTest; i++)
    outputSong[i] = 1;

  /* Reading all input_lines */
  inSong.clear();
  i = 0;

  while (cin.good()) {
    getline(cin, input_line);

    /* Translating to song */
    if ( (i < numTest) && !(input_line.empty()) ) {
      count = 0;
      for (j=0; j < input_line.length(); j++ ) {
        currentChar = input_line.at(j);
        if ( (currentChar >= 'A' && currentChar <= 'Z') ||
            (currentChar >= 'a' && currentChar <= 'z') ) {
          count++;
        }
        else {
          if (count)
            inSong += to_string(count);
          count = 0;
        }
      }
      inSong += to_string(count);
      count = 0;

      /* Check if it is pi song */
      for (j=0; (j < inSong.length()) && (j < piNum.length()); j++) {
        if ( inSong.at(j) != piNum.at(j) ) {
          outputSong[i] = 0;
          break;
        }
      }
    }

    else
      outputSong[i] = -1;

    inSong.clear();
    i++;
  }

  for (i=0; i < numTest; i++) {
    if (outputSong[i] == 1)
      cout << "It's a pi song.\n";
    else if (outputSong[i] == 0)
      cout << "It's not a pi song.\n";
  }

  return 0;
  }
