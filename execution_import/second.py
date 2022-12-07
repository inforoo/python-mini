print(f"что-то выводит скрипт {__name__}")


def helper():
    print(f"скрипт {__name__}, вызвана функция helper")


def main():
    print(f"скрипт {__name__}, главная функция")


if __name__ == '__main__':
    main()
