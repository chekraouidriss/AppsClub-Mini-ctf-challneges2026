#include <stdio.h>
#include <string.h>

// 🔒 hidden flag
void hidden() {
    char flag[] = {
        'F','L','A','G','{',
        'f','0','l','l','0','w','_','t','h','3','_','c','0','d','3','}',
        '\0'
    };
    printf("%s\n", flag);
}

void fake() {
    printf("Nothing here...\n");
}

int main() {
    char input[50];

    printf("Enter password: ");
    scanf("%s", input);

    if (strcmp(input, "1234") == 0) {
        fake(); // ❌ wrong function
    } else {
        printf("Wrong password\n");
    }

    return 0;
}