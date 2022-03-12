"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Environment Variables saved in OS.
    """
import os


def main():
    try:
        print("Environment variables stored in this system are: ")
        os.system("printenv")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
