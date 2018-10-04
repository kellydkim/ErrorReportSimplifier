# Created by Da Kim and Edward M. Abrahamson

# Importing to make file parsing easier.
import json

def file_input():
    print("Hello!\n")
    print("Please enter the complete filename for the .json you'd like to parse.\n")
    file_name = input()

    print("Name of file is: " + file_name)

    while not file_name.lower().endswith('.json'):
        print("\n\nHey!  Let me help you:\n\n"
              "SYNTAX FOR USING THIS:\n\n"
              "> filename.json")
        file_name = input()




def main():
    file_input()





if __name__ == "__main__":
    main()