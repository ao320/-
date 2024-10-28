#include <stdio.h>

int main(void) {
    int a,b = 0;
    int j = 1;
    puts("比較したい数1つ目の数字を入力して下さい");
    scanf("%d",&a);
    puts("比較したい数2つ目の数字を入力して下さい");
    scanf("%d",&b);

    while (j) {
        j = a % b;
        a = b;
        b = j;
    }
    printf("最大公約数：%d\n",a);
    return 0;
}
