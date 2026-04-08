import os

def write_file(working_directory: str, file_path: str, content: str):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        print("File not in the working dir")

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
            return f'content write: {content} with {len(content)} characteres. \n'
    except:
        return "Failed to write on file"
