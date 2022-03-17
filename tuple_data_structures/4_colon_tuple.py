"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Colon a tuple
    """


def colon_tuple(given_tuple):
    """
    Description:
        Using colon of tuple.
    Parameter:
        given_tuple: Given tuple to use colon feature.
    Return:
        Given tuple using colon
    """
    return given_tuple[:]


def main():
    try:
        sample_tuple = ('p','r','o','g','r','a','m','i','z')
        print("Given tuple:", sample_tuple)
        print("Colon of given tuple is:", colon_tuple(sample_tuple))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
