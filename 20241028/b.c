#include <stdio.h>
#include <math.h>

int main(void) {
    int i, n = 0;
    double out = 0;
    puts("計算回数を入力してください");
    scanf("%d",&n);
    for(i = 0; i < n; i++) {
        out += pow(-1, i) / (2*i + 1);
    }
    out = out * 4;
    printf("π=%lf\n",out);
}
