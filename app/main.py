import sys


def main():
    
    

    # Wait for user input
    while True:
        sys.stdout.write("$ ")
        user_input = input()
        if (user_input == "exit 0"):
            break
        elif (user_input[0:5] == "echo "):
            print(f"{user_input[5:]}")
            continue
        print(f"{user_input}: command not found")


if __name__ == "__main__":
    main()
