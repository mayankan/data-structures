"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Dictionary Data Structure Programs - Check key in dictionary
    """


def main():
    dict_check = {'mayank': 9560, 'anand': 2911, 'prerak': 4923, 'neelesh': 1123, 'farzana': 4355}
    try:
        if 'prerak' in dict_check:
            print("Yes 'prerak' key exists in dict")
        else:
            raise KeyError
    except KeyError:
        print("No 'prerak' key does not exists in dict")


if __name__ == "__main__":
    main()
