"""
    @Author: Mayank Anand
    @Date: 2022-03-10
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs - First and Last Element from List
    """


def main():
    try:
        color_list = ["Red", "Green", "White", "Black"]
        print("First Color", color_list[0])
        print("Last Color", color_list[-1])
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
