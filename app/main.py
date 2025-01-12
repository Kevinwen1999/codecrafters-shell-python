import sys


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
            else:
                print(f"{arg}: not found")
            continue
        print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
