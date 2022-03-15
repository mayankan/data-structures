"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Dictionary Data Structure Programs - Convert list to Nested Dictionary
    """


def list_to_dict(input_list):
    """
    Description:
        Converts given list into nested dictionary.
    Parameter:
        input_list: given list to be converted to nested dictionary.
    Return:
        Nested Dictionary converted from given list.
    """
    nested_dict = working_dict = {}
    for name in input_list:
        working_dict[name] = {}
        working_dict = working_dict[name]
    return nested_dict


def main():
    try:
        num_list = [1, 2, 3, 4]
        derived_dict = list_to_dict(num_list)
        print("Nested Dictionary from given list is:",derived_dict)
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
