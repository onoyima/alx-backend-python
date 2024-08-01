import os
import subprocess

def check_newline(file_path):
    with open(file_path, 'rb') as f:
        f.seek(-1, os.SEEK_END)
        if f.read(1) != b'\n':
            return False
    return True

def check_shebang(file_path):
    with open(file_path, 'r') as f:
        first_line = f.readline().strip()
        return first_line == "#!/usr/bin/env python3"

def check_pycodestyle(file_path):
    # Check pycodestyle version
    version_process = subprocess.Popen(["pycodestyle", "--version"], stdout=subprocess.PIPE)
    version_output = version_process.communicate()[0].decode('utf-8')
    
    if "2.5" not in version_output:
        raise Exception("pycodestyle version is not 2.5")

    # Check file for pycodestyle issues
    style_process = subprocess.Popen(["pycodestyle", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    style_output = style_process.communicate()[0].decode('utf-8')
    return style_output.strip()

def check_executable(file_path):
    return os.access(file_path, os.X_OK)

def check_length(file_path):
    result = subprocess.Popen(["wc", "-l", file_path], stdout=subprocess.PIPE)
    output = result.communicate()[0].decode('utf-8')
    return int(output.strip().split()[0])

def check_documentation(file_path, entity):
    module_name = file_path.replace('.py', '').replace('/', '.')
    command = f"python3 -c 'print(__import__(\"{module_name}\").{entity}.__doc__)'"
    doc_process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    doc_output = doc_process.communicate()[0].decode('utf-8').strip()
    return bool(doc_output) and len(doc_output.split()) > 1

def check_all_files(file_paths):
    for file_path in file_paths:
        print(f"\nChecking {file_path}...")
        
        if not check_newline(file_path):
            print(f"Failed: {file_path} does not end with a new line.")
        
        if not check_shebang(file_path):
            print(f"Failed: {file_path} does not start with #!/usr/bin/env python3.")
        
        pycodestyle_issues = check_pycodestyle(file_path)
        if pycodestyle_issues:
            print(f"Failed: {file_path} has pycodestyle issues:\n{pycodestyle_issues}")
        
        if not check_executable(file_path):
            print(f"Failed: {file_path} is not executable.")
        
        if check_length(file_path) == 0:
            print(f"Failed: {file_path} is empty.")
        
        if not check_documentation(file_path, ''):
            print(f"Failed: {file_path} does not have module-level documentation.")
        
        if not check_documentation(file_path, 'MyClass'):
            print(f"Failed: {file_path} does not have class-level documentation.")
        
        if not check_documentation(file_path, 'my_function'):
            print(f"Failed: {file_path} does not have function-level documentation.")

def main():
    file_paths = [
        "0-add.py", "0-main.py", "1-concat.py", "1-main.py", "2-floor.py", "2-main.py",
        "3-main.py", "3-to_str.py", "4-define_variables.py", "4-main.py", "5-main.py",
        "5-sum_list.py", "6-main.py", "6-sum_mixed_list.py", "7-main.py", "7-to_kv.py",
        "8-main.py", "8-make_multiplier.py", "9-element_length.py", "9-main.py",
        "100-main.py", "100-safe_first_element.py", "101-main.py", "101-safely_get_value.py",
        "102-main.py", "102-type_checking.py"
    ]
    check_all_files(file_paths)

if __name__ == "__main__":
    main()

