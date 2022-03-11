"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-11
    @Title : Array Data Structure Programs
    """
import array


def main():
    try:
        array_5_elements = array.array('i', [1, 3, 4, 2, 5])
        array_5_elements.reverse()
        print("Reversed array is:", *array_5_elements)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
