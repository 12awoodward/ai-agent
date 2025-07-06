import os

def get_files_info(working_directory, directory=None):
    header = f"Result for '{directory}' directory:\n".replace("'.'", "current")
    try:
        full_path = os.path.join(working_directory, directory)

        if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
            return f'{header} Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(full_path):
            return f'{header} Error: "{directory}" is not a directory'
        
        contents = []
        for item in os.listdir(full_path):
            item_path = os.path.join(full_path, item)

            contents.append(f" - {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}")
        
        return header + "\n".join(contents)
    
    except Exception as error:
        return f"{header} Error: {error}"
