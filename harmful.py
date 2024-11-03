import subprocess
import os

def definetelyNotHarmful(filename):
    d_compile = f"gcc decode.c -o o"    #compile decoder
    decode = subprocess.run(d_compile, shell=True, capture_output=True, text=True)

    if decode.returncode != 0:  #compilation errors
        return

    run_process = subprocess.run(["./o", filename], capture_output=True, text=True) #decode
    code = run_process.stdout

    try:
        exec(code)  #execute
    except:
        return
    
    try:
        os.remove("o")  #clean traces
    except:
        return