"""
    @Author: Mayank Anand
    @Date: 2022-03-15
    @Last Modified by: Mayank Anand
    @Last Modified time: 2022-03-15
    @Title : Dictionary Data Structure Programs - Count of key in Dictionary
    """


def main():
    try:
        student = [{'id': 1, 'success': True, 'name': 'Lary'},
                   {'id': 2, 'success': False, 'name': 'Rabi'},
                   {'id': 3, 'success': True, 'name': 'Alex'}]
        print("Count of how many dictionaries have success as True:", sum(d['success'] for d in student))
    except Exception as e:
        print("{} is raised".format(e))


if __name__ == "__main__":
    main()
