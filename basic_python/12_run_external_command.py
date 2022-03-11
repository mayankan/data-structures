"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs
    """
import os


def main():
    try:
        command_name = input("Enter command to run: ")
        output_cmd = os.system(command_name)
        print("Output of the command is", output_cmd)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
