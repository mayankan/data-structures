"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Remove member(s) in set if present
    """


def main():
    try:
        set1 = {3, 5, 7, 9, 11, 13, 15, 17, 19}
        print("Set: ", set1)
        input_vals = int(input("Enter number of values to remove in set: "))
        for val in range(input_vals):
            input_val = int(input("Input {} value: ".format(val+1)))
            set1.discard(input_val)
        print("Set after removing member(s):", set1)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
