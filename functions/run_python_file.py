import os
import subprocess

def run_python_file(working_directory: str, file_path: str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        print("File not in the working dir")

    if not file_path.endswith(".py"):
        return "It's not a python file"

    try:
        output = subprocess.run(
            ["python3", file_path],
            cwd=abs_working_dir,
            timeout=30,
            capture_output=True
        )
        final_string = f"""
        STDOUT: {output.stdout}
        """
        return final_string
    except:
        print('Error executing python code.\n')
