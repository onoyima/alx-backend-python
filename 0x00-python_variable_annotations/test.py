import os
import subprocess

def run_script(script_name):
    try:
        result = subprocess.run([f"./{script_name}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        print(f"Running {script_name}...")
        print(result.stdout)
        if result.stderr:
            print("Errors:")
            print(result.stderr)
        print("\n")
    except Exception as e:
        print(f"Failed to run {script_name}: {e}")

def main():
    scripts = [
        "0-main.py",
        "1-main.py",
        "2-main.py",
        "3-main.py",
        "4-main.py",
        "5-main.py",
        "6-main.py",
        "7-main.py",
        "8-main.py",
        "9-main.py",
        "100-main.py",
        "101-main.py",
        "102-main.py"
    ]
    
    for script in scripts:
        run_script(script)

if __name__ == "__main__":
    main()

