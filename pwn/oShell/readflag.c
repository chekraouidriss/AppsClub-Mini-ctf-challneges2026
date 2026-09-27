#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *f = fopen("/flag.txt", "r");
    if (!f) {
        printf("Error opening flag\n");
        return 1;
    }

    char flag[128];
    fgets(flag, sizeof(flag), f);
    printf("%s\n", flag);

    fclose(f);
    return 0;
}