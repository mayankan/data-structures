def main():
    try:
        color_list = ["Red", "Green", "White", "Black"]
        print("First Color", color_list[0])
        print("Last Color", color_list[-1])
    except Exception as e:
        print("{} is raised.".format(e))


if __name__ == "__main__":
    main()
