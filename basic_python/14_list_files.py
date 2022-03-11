import os


def main():
    try:
        print("List of files in this directory are: ")
        os.system("ls")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
