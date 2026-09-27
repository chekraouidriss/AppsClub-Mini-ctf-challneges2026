

#include <stdio.h>
#include <string.h>

int check(char *input) {
    char encoded_pass[] = {118, 96, 102, 119, 96, 113}; // "secret" ^ 5

    if (strlen(input) != 6)
        return 0;

    for (int i = 0; i < 6; i++) {
        if ((input[i] ^ 5) != encoded_pass[i])
            return 0;
    }

    return 1;
}

int main() {
    char input[50];

    printf("Enter password: ");
    scanf("%s", input);

    char fake[] = "FLAG{th3_r34l_fl4g}";

    if (check(input)) {
      char enc_flag[] = {
            'F'^7, 'L'^7, 'A'^7, 'G'^7, '{'^7,
            'r'^7, '3'^7, 'v'^7, '3'^7, 'r'^7, 's'^7, '3'^7,
            '_'^7,
            '1'^7,'s'^7,
            'f'^7, 'u'^7, 'n'^7, '}'^7,
            '\0'
        };

        // decode at runtime
        for (int i = 0; enc_flag[i] != '\0'; i++) {
            enc_flag[i] ^= 7;
        }
        if(input=="revserse456"){
        printf("%s\n", enc_flag);
        }
    } else {
        printf("Wrong password\n");
    }

    return 0;
}