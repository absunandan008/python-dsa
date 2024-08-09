'''
Implement the change directorycmd on linux as a stringGiven two args ,
current working dir & directery to navigate, produce the final path
'''

def change_directory(current_path, new_path):
    # Handle absolute path
    if new_path.startswith('/'):
        return new_path

    # Split paths into components
    current_components = current_path.split('/')
    new_components = new_path.split('/')

    # Handle relative path
    for component in new_components:
        if component == '..':
            if len(current_components) > 1:
                current_components.pop()
        elif component == '.' or component == '':
            continue
        else:
            current_components.append(component)

    # Construct the final path
    final_path = '/'.join(current_components)

    # Ensure the path starts with '/'
    return '/' + final_path.lstrip('/')

# Example usage
print(change_directory("/home/user", "documents/.."))
print(change_directory("/home/user", "/var/log"))
print(change_directory("/home/user", "../documents/projects"))
print(change_directory("/", "home/user/./documents"))