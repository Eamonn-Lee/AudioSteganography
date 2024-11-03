#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HEADER_SIZE 44 // WAV header size
#define INPUT_FILE "input.wav" // Default input file name
#define OUTPUT_FILE "output.wav" // Default output file name
#define MESSAGE "This is a secret message" // Hardcoded message to hide

int main() {
    FILE *in = fopen(INPUT_FILE, "rb");
    FILE *out = fopen(OUTPUT_FILE, "wb");

    if (!in || !out) { //error checking files
        printf("Cannot find files\n");
        exit(1);
    }

    // Copy header into output
    unsigned char header[HEADER_SIZE];
    fread(header, sizeof(unsigned char), HEADER_SIZE, in);
    fwrite(header, sizeof(unsigned char), HEADER_SIZE, out);

    // Encode message length
    int len = strlen(MESSAGE);
    
    unsigned char byte;

    // embed 32 bit int
    for (int i = 0; i < 32; i++) {
        fread(&byte, sizeof(unsigned char), 1, in);
        byte = (byte & 0xFE) | ((len >> i) & 1); // clear least sig bit, slap bit into the LSB

        fwrite(&byte, sizeof(unsigned char), 1, out);
    }

    // embed message
    for (int i = 0; i < len; i++) { // each char of msg
        for (int bit = 0; bit < 8; bit++) { // each bit of char byte
            fread(&byte, sizeof(unsigned char), 1, in);

            byte = (byte & 0xFE) | ((MESSAGE[i] >> bit) & 1); // Embed message bits into the LSB

            fwrite(&byte, sizeof(unsigned char), 1, out);
        }
    }

    // shove rest in
    while (fread(&byte, sizeof(unsigned char), 1, in)) {
        fwrite(&byte, sizeof(unsigned char), 1, out);
    }

    fclose(in);
    fclose(out);

    printf("output %s\n", OUTPUT_FILE);
    return 0;
}
