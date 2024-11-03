# Compiler and flags
CC = gcc
CFLAGS = -Wall -g

# Executable names
ENCODE = encode
DECODE = decode

# Source files
ENCODE_SRC = encode.c
DECODE_SRC = decode.c

# Object files (optional if you want to compile separately)
ENCODE_OBJ = encode.o
DECODE_OBJ = decode.o

# Default target: build both encode and decode
all: $(ENCODE) $(DECODE)

# Compile encode
$(ENCODE): $(ENCODE_SRC)
	$(CC) $(CFLAGS) -o $(ENCODE) $(ENCODE_SRC)

# Compile decode
$(DECODE): $(DECODE_SRC)
	$(CC) $(CFLAGS) -o $(DECODE) $(DECODE_SRC)

# Clean rule to remove compiled files
clean:
	rm -f $(ENCODE) $(DECODE) $(ENCODE_OBJ) $(DECODE_OBJ)

# Phony target to ensure 'clean' always runs
.PHONY: all clean
