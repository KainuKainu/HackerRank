// ios::eof example
#include <iostream>     // std::cout
#include <fstream>      // std::ifstream
#include <string>
using namespace std;

int main () {
  string input;

  while (cin.good()) {
    getline(cin, input);
  }

  cout << "Wtf is this error?!\n";
  return 0;
}
