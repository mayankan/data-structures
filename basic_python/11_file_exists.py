"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - File Exist Check
    """
import os


def main():
    try:
        file_name = input("Enter file name to check whether it exists or not?: ")
        if os.path.exists(file_name):
            print("File exists.")
        else:
            print("File doesn't exist.")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
