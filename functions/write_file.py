import os

def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not full_path.startswith(os.path.abspath(working_directory)):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        
        file_dir = os.path.dirname(full_path)
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        
        with open(full_path, "w") as file:
            file.write(content)
        
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as error:
        return f"Error: {error}"