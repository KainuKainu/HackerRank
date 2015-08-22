#include <stdio.h>
#include <stdbool.h>
static const char* s = "abff";
static const int L = 4;

static int nibble(char c) {
  if(c >= '0' && c <= '9') return c;
  if(c >= 'a' && c <= 'f') return c - 'a' + 10;
  if(c >= 'A' && c <= 'F') return c - 'A' + 10;
  fprintf(stderr, "ERROR! c = %c\n", c);
  return 255;
}

int main() {
  bool arr[L*4];
  int in;
  in = L*4-1;
  int n, i, j;

  for (i = L-1; i >= 0; i--) {
    n = nibble((char)s[i]);
    for (j = 4; j > 0; j--) {
      arr[in] = (n%2);
      n = n >> 1;
      in--;
    }
  }

  // print
  for (i = 0; i < L*4; i++) {
    if (arr[i]) printf("1");
    else printf("0");
  }
  printf("\n");

  return 0;
}
