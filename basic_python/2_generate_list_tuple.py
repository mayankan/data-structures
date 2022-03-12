"""
    @Author: Mayank Anand
    @Date: 2022-03-10
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Basic Python Data Structure Programs -
    """


def gen_list_tuple(_numbers):
    """
    Description:
        Returns List and Tuple for the numbers passed in parameter string separated by comma.
    Parameter:
        String containing numbers separated by comma.
    Return:
        List and Tuple having numbers given in parameter.
    """
    try:
        num_list = _numbers.split(", ")
        num_tuple = tuple(num_list)
        return num_list, num_tuple
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        numbers = input("Enter numbers separated by comma: ")
        num_list, num_tuple = gen_list_tuple(numbers)
        print("List:", num_list)
        print("Tuple:", num_tuple)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
