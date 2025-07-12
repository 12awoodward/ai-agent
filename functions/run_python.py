import os
import subprocess

def run_python_file(working_directory, file_path):
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'
    
    if os.path.splitext(full_path)[1] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    
    exe_txt = f'Executing file "{file_path}":\n'

    try:
        result = subprocess.run(["python3", file_path], cwd=working_directory, timeout=30, capture_output=True, text=True)
    except Exception as error:
        return f"{exe_txt}Error: executing Python file: {error}"
    
    output = "No output produced"
    if len(result.stdout) + len(result.stderr) > 0:
        output = f" STDOUT: {result.stdout}\n STDERR: {result.stderr}"
    
    if result.returncode != 0:
        output += f"\n Process exited with code {result.returncode}"
    
    return exe_txt + output
