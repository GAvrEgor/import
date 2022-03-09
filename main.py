from datetime import date
from application import salary
from db import people


def main():
    print(date.today())
    salary.calculate_salary()
    people.get_employess()


if __name__ == '__main__':
    main()
