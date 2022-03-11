import os


def main():
    try:
        cpu_cnt = os.cpu_count()
        print("CPUs Count is", cpu_cnt)
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
