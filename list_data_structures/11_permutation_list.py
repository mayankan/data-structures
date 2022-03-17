"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : List Data Structure Programs - Permutation of all elements in the list
    """


def permutation(given_list):
    """
    Description:
        Calculates permutations of elements sequence in list.
    Parameter:
        given_list: List to be checked for all permutation sequence.
    Return:
        List with list of all permutation sequence in which elements can be assigned in given list.
    """
    # If given_list is empty then there are no permutations
    if len(given_list) == 0:
        return []

    # If there is only one element in given_list then, only one permutation is possible
    if len(given_list) == 1:
        return [given_list]

    # Find the permutations for lst if there are more than 1 characters

    permutation_list = []  # empty list that will store current permutation

    # Iterate the input(given_list) and calculate the permutation
    for index in range(len(given_list)):
        member = given_list[index]

        # Extract given_list[index] or member from the given_list. rem_list is remaining list
        rem_list = given_list[:index] + given_list[index+1:]

        # Generating all permutations where m is first element
        for each_p in permutation(rem_list):
            permutation_list.append([member] + each_p)
    return permutation_list


def main():
    try:
        sample_list = list('123')
        print("List:", sample_list)
        print("Permutation of all elements in the list:")
        for element in permutation(sample_list):
            print(element)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
