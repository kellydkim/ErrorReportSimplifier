# Created by Da Kim and Edward M. Abrahamson

import errno
import json

def file_input():
    print("Hello!\n")
    print("Please enter the complete filename for the .json you'd like to parse.")
    file_name = input()

    print("\nName of file is: " + file_name + "\n")

    try:
        jdata = json.loads(open(file_name).read())
        print("File is readable!")
    except IOError as e:
        if e.errno == errno.EACCES:
            print("file exists, but isn't readable")
        elif e.errno == errno.ENOENT:
            print("Files not found!\n")

    return jdata



def main():
    jdata = file_input()


if __name__ == "__main__":
    main()