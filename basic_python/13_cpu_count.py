"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - Used CPU Count
    """
import os


def main():
    try:
        cpu_cnt = os.cpu_count()
        print("CPUs Count is", cpu_cnt)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
