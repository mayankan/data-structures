import os


def main():
    try:
        print("Environment variables stored in this system are: ")
        os.system("printenv")
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
