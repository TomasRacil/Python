#include<stdio.h>
#include<time.h>
//#include "primeheader.h"

int isPrime(int n) {
    for (int i = 2; i < n / 2; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}

int kthPrime(int k) {
    int candidate = 2;
    while (k) {
        if (isPrime(candidate))
            k--;
        candidate++;
    }
    return candidate - 1;
}

// Driver code
int main() {
    clock_t t;
    t = clock();
    int prime = kthPrime(1500);
    t = clock() - t;
    double time_taken = ((double)t) / CLOCKS_PER_SEC;

    printf("Prvocislo: %d \n", prime);
    printf("Cas: %f s\n", time_taken);
    return 0;
}
