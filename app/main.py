import sys
import os

def find_program_in_path(program_name):
    # Get the PATH environment variable
    path_dirs = os.environ.get("PATH", "").split(os.pathsep)
    
    for directory in path_dirs:
        # Construct the full path of the program
        program_path = os.path.join(directory, program_name)
        if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
            return program_path  # Return the first found executable path
    
    return None  # Return None if the program is not found


def main():
    
    built_in_list = ["echo", "exit", "type"]

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        if (user_input == "exit 0"):
            break
        elif (user_input[0:5] == "echo "):
            print(f"{user_input[5:]}")
            continue
        elif (user_input[0:5] == "type "):
            arg = user_input[5:]
            if (arg in built_in_list):
                print(f"{arg} is a shell builtin")
            elif (find_rst := find_program_in_path(arg)):
                print(f"{arg} is {find_rst}")
            else:
                print(f"{arg}: not found")
            continue
        print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
