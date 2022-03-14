"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Creating a dictionary using squares of key values.
    """


def main():
    dict_limit = int(input("Enter a number till which you want to create a dictionary: "))
    square_dict = {}
    for index in range(dict_limit):
        # saving actual index in no variable
        no = index+1
        # Squaring no and storing no as key and square as value in square_dict dictionary
        square_dict[no] = no * no
    print(square_dict)


if __name__ == "__main__":
    main()
