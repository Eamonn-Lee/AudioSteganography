# AudioSteganography
Completed for COMP6841
## Failed techniques
Amplitude Zero crossing encoder and decoder are within 'failAmpZero/main.py'

Frequency Domain encoder and decoder are 'failFrequencyDomain/e.py' and 'failFrequencyDomain/d.py' respectively

## Application
'driver.py' utilises 'harmful.py' to simulate running harmful code as a example of using audiosteganography in a malicious context

## Usage
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
