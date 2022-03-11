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
        array_5_elements = array.array('i', [1, 3, 4, 3, 2, 5])
        count_dict = {}
        for index in range(len(array_5_elements)):
            if array_5_elements[index] not in count_dict.keys():
                array_element = array_5_elements[index]
                count_dict[array_element] = array_5_elements.count(array_element)
        for key, value in count_dict.items():
            print("No of values for {} is {}.".format(key, value))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
