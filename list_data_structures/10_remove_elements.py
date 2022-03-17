"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - List after removing indexes
    """



def main():
    try:
        sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
        print("List:", sample_list)
        # Remove 0th element.
        del sample_list[0]
        # Remove 4th and 5th element.
        del sample_list[3:5]
        print("List after removing 0th, 4th and 5th element", sample_list)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
