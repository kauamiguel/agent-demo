import os

def get_files_info(working_directory: str, directory:str = "."):
    abs_working_dir = os.path.abspath(working_directory)
    abs_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not abs_dir.startswith(abs_working_dir):
        return "You're not in an allowed directory"

    final_response = ""
    contents = os.listdir(abs_dir)
    for content in contents:
        content_path = os.path.join(abs_dir, content)
        ## Show absolute directory + the file/dir of the current directory
        is_dir = os.path.isdir(content_path)
        file_info = os.path.getsize(content_path)
        final_response += f" - {content} : file_size={file_info}, is_dir={is_dir}\n"

    return final_response


schema_get_files_info = {
    "type" : "function",
    "function" : {
        "name" : "get_files_info",
        "description" : "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type" : "object",
            "properties": {
                "directory" : {
                    "type" : "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                }
            },
            "required": ["directory"]
        }
    }
}
