def reverse_name(_f_name, _l_name):
    try:
        return _l_name + " " + _f_name
    except Exception as e:
        print("{} is raised.".format(e))


def main():
    try:
        f_name = input("Enter your first name: ")
        l_name = input("Enter your last name: ")
        print(reverse_name(f_name, l_name))
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
