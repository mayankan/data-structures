"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Dictionary Data Structure Programs - Dictionary from string
    """


def str_to_dict(string):
    """
    Description:
        Converts String to Dictionary having count of each character.
    Parameter:
        string: Given string to be converted to dictionary.
    Return:
        Returns Dictionary with count of each character in given string.
    """
    try:
        result = {}
        for keys in string:
            result[keys] = result.get(keys, 0) + 1
        return result
    except Exception as e:
        print("{} is raised".format(e))


def main():
    try:
        input_string = input("Enter string to create dictionary: ")
        print("Dictionary created from string is", str_to_dict(input_string))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
