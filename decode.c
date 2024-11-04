#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HEADER_SIZE 44 // WAV header size

int main(int argc, char *argv[]) {
    FILE *in = fopen(argv[1], "rb");

    if (!in) {
        printf("Error file\n");
        exit(1);
    }

    // Skip header
    fseek(in, HEADER_SIZE, SEEK_SET);

    unsigned char byte;
    int len = 0;

    for (int i = 0; i < 32; i++) {
        fread(&byte, sizeof(unsigned char), 1, in);
        len |= (byte & 1) << i; // Reconstruct decode length
    }

    char *decode = (char*)malloc(len + 1);  // create string array
    memset(decode, 0, len + 1);

    // Extract decode
    for (int i = 0; i < len; i++) {
        for (int bit = 0; bit < 8; bit++) {
            fread(&byte, sizeof(unsigned char), 1, in);
            decode[i] |= (byte & 1) << bit; // Reconstruct each byte of the decode from the LSBs
        }
    }

    fclose(in);

    printf("%s", decode);
    free(decode);
    return 0;
}
