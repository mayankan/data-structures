"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Add member(s) in set
    """


def main():
    set1 = {3, 5, 7, 9}
    print("Set: ", set1)
    input_vals = int(input("Enter number of values to add in set: "))
    for val in range(input_vals):
        input_val = int(input("Input {} value: ".format(val+1)))
        set1.add(input_val)
    print("Set after adding member(s):", set1)


if __name__ == "__main__":
    main()
