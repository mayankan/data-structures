"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Dictionary Data Structure Programs - Printing Dictionary in Table Format
    """


def main():
    try:
        dict_table = {'mayank': 9560, 'anand': 2911, 'prerak': 4923, 'neelesh': 1123, 'farzana': 4355}
        for name, number in dict_table.items():
            print('{}  :  {}'.format(name, number))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
