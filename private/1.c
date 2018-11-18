#include <stdio.h>
#define SIZE 5
int item[SIZE] = {1, 2, 3, 4, 5};
void main(void) {
    sum(item, SIZE);
    printf("Size of item = % d\n", sizeof item);
}
int sum(int a[], int n) {
    int i;
    int s = 0;
    printf("Size of a = % d\n", sizeof a);
    for (i = 0; i < n; i++)
        s += a[i];
    return s;
}