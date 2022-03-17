"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Find repetitions in tuple
    """


def repetitions_tuple(given_tuple):
    """
    Description:
        Checks Repeated Items in Tuple.
    Parameter:
        given_tuple: Given tuple to check repeated items.
    Return:
        Tuple of Repeated items in given tuple.
    """
    repetitions = []
    for item in given_tuple:
        # Checks if item in tuple has count greater than 1 or is already their in repetitions list.
        if given_tuple.count(item) > 1 and item not in repetitions:
            # Appends Repeated Item in Repititions list.
            repetitions.append(item)
    return tuple(repetitions)


def main():
    try:
        sample_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z', 'p')
        print("Given tuple:", sample_tuple)
        print("Repeated items in given tuple are:", repetitions_tuple(sample_tuple))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
