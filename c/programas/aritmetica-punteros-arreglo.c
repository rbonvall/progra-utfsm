#include <stdio.h>

int main() {
    int nrs[6] = { 11, 44, 22, 88, 55, 77 };
    int *p;

    for (p = nrs; p < nrs + 6; ++p) {
        printf("%d\n", *p);
    }

    return 0;
}
