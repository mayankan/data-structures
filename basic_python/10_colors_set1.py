"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs
    """


def main():
    try:
        color_list_1 = set(["White", "Black", "Red"])
        color_list_2 = set(["Red", "Green"])
        diff_list = color_list_1.difference(color_list_2)
        print(set(sorted(diff_list)))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
