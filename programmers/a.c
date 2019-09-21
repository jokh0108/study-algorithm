#include <stdio.h>
#define N 20


int main(void){
 
    // [n][r] 이다.
    unsigned long long Combination[N + 1][N + 1] = {0,};
 
    Combination[1][1] = 1;
    for (int i = 2; i <= N; i++){
        for (int j = 1; j <= i; j++){
            Combination[i][j] = Combination[i - 1][j - 1] + Combinatio  n[i - 1][j];
            printf("%d ", Combination[i][j]);
        }
        printf("\n");
    }
    return 0;
}
