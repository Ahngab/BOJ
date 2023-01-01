#include <stdio.h>
long long sum(int *a, int n){
    long long sum = 0;
    int i;

    for(i = 0; i < n; i++){
        sum += a[i];
    }
    return sum;
}