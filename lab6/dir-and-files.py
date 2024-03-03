1.
import os

def list_directories(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

def list_files(path):
    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

def list_all(path):
    print("\nAll Directories and Files:")
    for item in os.listdir(path):
        print(item)

def main():
    specified_path = input("Enter the path: ")

    if os.path.exists(specified_path):
        list_directories(specified_path)
        list_files(specified_path)
        list_all(specified_path)
    else:
        print("Invalid path. Please enter a valid path.")

if __name__ == "__main__":
    main()

2.
import os

def check_path_access(path):
    if os.path.exists(path):
        print(f"{path} exists.")
        if os.access(path, os.R_OK):
            print(f"{path} is readable.")
        else:
            print(f"{path} is not readable.")

        if os.access(path, os.W_OK):
            print(f"{path} is writable.")
        else:
            print(f"{path} is not writable.")

        if os.access(path, os.X_OK):
            print(f"{path} is executable.")
        else:
            print(f"{path} is not executable.")
    else:
        print(f"{path} does not exist.")

def main():
    specified_path = input("Enter the path to check access: ")
    check_path_access(specified_path)

if __name__ == "__main__":
    main()

3.
import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"{path} exists.")

       
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        print(f"Filename: {filename}")
        print(f"Directory: {directory}")

    else:
        print(f"{path} does not exist.")

def main():
    specified_path = input("Enter the path to analyze: ")
    analyze_path(specified_path)

if __name__ == "__main__":
    main()

4.
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in {file_path}: {line_count}")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_path = input("Enter the path to the text file: ")
    count_lines(file_path)

if __name__ == "__main__":
    main()

5.
def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List successfully written to {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    data_to_write = [1, 2, 3, 4, 5]

    file_path = input("Enter the path for the output file: ")
    write_list_to_file(file_path, data_to_write)

if __name__ == "__main__":
    main()

6.
import string

def generate_files():
    try:
        for letter in string.ascii_uppercase:
            file_name = letter + ".txt"
            with open(file_name, 'w') as file:
                file.write(f"Content of {file_name}")
            print(file_name)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    generate_files()

if __name__ == "__main__":
    main()

7.
def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as source_file, open(destination_path, 'w') as destination_file:
            content = source_file.read()
            destination_file.write(content)
        print(f"Contents of {source_path} copied to {destination_path} successfully.")
    except FileNotFoundError:
        print(f"File {source_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_path = input("Enter the source file path: ")
    destination_path = input("Enter the destination file path: ")

    copy_file(source_path, destination_path)

if __name__ == "__main__":
    main()

8.
import os

def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            print(f"{file_path} exists.")

            # Check for access before deletion
            if os.access(file_path, os.W_OK):
                os.remove(file_path)
                print(f"File {file_path} deleted successfully.")
            else:
                print(f"You don't have write access to {file_path}. Cannot delete the file.")
        else:
            print(f"{file_path} does not exist. Nothing to delete.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    specified_path = input("Enter the path of the file to delete: ")
    delete_file(specified_path)

if __name__ == "__main__":
    main()