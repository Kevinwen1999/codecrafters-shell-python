import sys
import os
import subprocess

def pwd():
    return os.getcwd()  # Returns the current working directory

def cd(new_directory):
    try:
        if (new_directory == "~"):
            os.chdir(os.environ.get("HOME", ""))
        else:
            os.chdir(new_directory)  # Changes the current working directory
        return f"success"
    except FileNotFoundError:
        return f"cd: {new_directory}: No such file or directory"
    except PermissionError:
        return f"cd: {new_directory}: No such file or directory"
    
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
    
    built_in_list = ["echo", "exit", "type", "pwd"]

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
        elif (user_input[0:3] == "pwd"):
            print(f"{pwd()}")
        elif (user_input[0:3] == "cd "):
            res = cd(user_input[3:])
            if res != "success":
                print(res)
        else:
            input_list = user_input.split(" ")
            find_rst = find_program_in_path(input_list[0])
            if (not find_rst):
                print(f"{user_input}: command not found")
                continue
            # Execute the program with arguments
            result = subprocess.run(input_list)
            continue

        # print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
