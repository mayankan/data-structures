"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Sorting dictionary in ascending and descending order.
    """


def main():
    sample_dict = {0: 10, 1: 20}
    print("Sorted dictionary by value in ascending order:", sorted(sample_dict.values()))
    print("Sorted dictionary by value in descending order:", sorted(sample_dict.values(), reverse=True))


if __name__ == "__main__":
    main()
