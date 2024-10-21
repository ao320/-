#include <stdio.h>

int main(void) {
    int out = 0;
    for(int i = 1; i <= 100; i++) {
        out += i;
    }
    printf("%d\n", out);
    return 0;
}