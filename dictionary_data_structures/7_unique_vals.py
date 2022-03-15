"""
    @Author: Mayank Anand
    @Date: 2022-03-11
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-14
    @Title : Dictionary Data Structure Programs - Unique values in dictionary
    """


def main():
    sample_data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
                   {"V": "S009"}, {"VIII": "S007"}]
    print("Unique Values:", set(value for d_data in sample_data for value in d_data.values()))


if __name__ == "__main__":
    main()
