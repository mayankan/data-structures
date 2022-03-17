"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Sort List by Tuple's Last Member
    """

def sort_tuple(given_list):
    """
    Description:
        Sorts List of tuples based on last member of each tuple.
    Parameter:
        given_list: The list of tuple elements which have to be sorted by last member of each tuple.
    Return:
         List of tuples after sorting based on last member of each tuple.
    """
    for row in range(len(given_list)):
        for col in range(len(given_list)-1):
            # Use of Bubble sort on last index of tuple
            if given_list[col][-1] > given_list[col+1][-1]:
                given_list[col],given_list[col+1] = given_list[col+1], given_list[col]
    # Another method
    # def last_member(given_tuple):
    #     return given_tuple[-1]
    # given_list = sorted(given_list, key = last_member)
    return given_list


def main():
    try:
        sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
        print("Sorted Tuple as per last member is:", sort_tuple(sample_list))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
