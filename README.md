# AudioSteganography

#Usage
1) compile c executables via makefile
   ```bash
   make
2) encode command into input.wav file
   ```bash
   ./encode command
   
3) Decode
    - 3a) Decode using decode function
        ```bash
        ./decode filename
    - 3b) Run driver function to execute
        ```bash
        python3 driver.py