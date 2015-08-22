#include <stdbool.h>
#include <stdio.h>

int read_hex(bool* result, FILE* fp)
{
    int x;
    if (fp == NULL) {
       fprintf(stderr, "Can't open input file in.list!\n");
       return -1;
    }
    int start_index = 0;
    while( fscanf(fp, "%1x", &x) != -1)
    {
        printf("%d\n", x); 
        for (int j = 3; j >= 0; j--) {
            result[start_index+j] = (x%2);
            x = x >> 1;
        }
        start_index+=4;
    }
    return start_index;
}

int main()
{
    int length;
    bool arr[304];
    int x;
    FILE *fp;
    fp = fopen("discovered.txt", "r");
    length = read_hex(arr, fp);

    for (int i = 0; i < length; i++) {
        if(i%4 == 0 && i != 0 ) printf(" ");
        printf("%d", arr[i]);
    }
}

