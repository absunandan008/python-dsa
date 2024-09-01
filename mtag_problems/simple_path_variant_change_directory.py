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


def cd(cwd, destination):
    # Split paths into parts
    cwd_parts = cwd.split('/')
    dest_parts = destination.split('/')

    # Initialize a list to keep track of the resulting path
    path = []

    # Start with the current working directory parts if it's an absolute path
    if cwd.startswith('/'):
        path = cwd_parts

    # Navigate through the destination path parts
    for part in dest_parts:
        if part == '' or part == '.':
            # Ignore empty and current directory components
            continue
        elif part == '..':
            # Pop the last directory if we have directories to pop
            if path and path[-1] != '':
                path.pop()
        else:
            # Add the directory to the path
            path.append(part)

    # Join the path components to form the final path
    final_path = '/' + '/'.join(filter(None, path))
    return  final_path
# Example usage
print(change_directory("/home/user", "documents/.."))
print(cd("/home/user", "documents/.."))
print(change_directory("/home/user", "/var/log"))
print(cd("/home/user", "/var/log"))
print(change_directory("/home/user", "../documents/projects"))
print(cd("/home/user", "../documents/projects"))
print(change_directory("/", "home/user/./documents"))
print(cd("/", "home/user/./documents"))
