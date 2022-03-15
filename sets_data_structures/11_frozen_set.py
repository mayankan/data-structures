"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Sets Data Structure Programs - Frozen Sets
    """


def main():
    try:
        set1 = {3, 5, 7, 9, 11, 13, 15, 17, 19}
        f_set1 = frozenset(set1)
        print("Frozen Set: ", f_set1)
        # Immutable
        f_set1.add(2)  # throws an error
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
