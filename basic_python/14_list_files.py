"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Run List Structure Command using Python
    """
import os


def main():
    try:
        print("List of files in this directory are: ")
        os.system("ls")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
