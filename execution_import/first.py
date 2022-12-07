import second

print(f"что-то выводит скрипт {__name__}")


def main():
    print(f"скрипт {__name__}, главная функция")
    second.helper()


if __name__ == '__main__':
    main()
