"""
    @Author: Mayank Anand
    @Date: 2022-03-16
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-17
    @Title : Tuple Data Structure Programs - Slicing tuples.
    """


def main():
    sample_tuple = (11, 22, 33, 44, 55, 66, 77, 88, 99, 100)
    print("Tuple:", sample_tuple)

    slice1 = sample_tuple[1:5]
    print("Tuple Items from 1 to 4 index:", slice1)

    slice2 = sample_tuple[-3:]
    print("Last Three Tuple Items:", slice2)

    slice3 = sample_tuple[:3]
    print("First Two Tuple Items:", slice3)

    slice4 = sample_tuple[1:8:3]
    print("Tuple items from 1st Index to 7th Index with step from every 3 element:", slice4)


if __name__ == "__main__":
    main()
