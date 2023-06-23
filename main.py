from datetime import datetime, timedelta, date
# from datetime import date

list_users = (
    {"name": "Artem", "birthday": date(1979, 6, 28)},
    {"name": "Ira", "birthday": date(1980, 6, 24)},
    {"name": "Diana", "birthday": date(2002, 6, 18)},
    {"name": "Mila", "birthday": date(2014, 6, 23)}
)

list_users2 = (
    {"name": "Artem", "birthday": date(1979, 1, 1)},
    {"name": "Ira", "birthday": date(1980, 12, 30)},
    {"name": "Diana", "birthday": date(2002, 1, 3)},
    {"name": "Mila", "birthday": date(2014, 6, 23)},
    {"name": "Avrora", "birthday": date(2014, 12, 31)}

)


def get_period_birth() -> list:
    current_date = datetime.now().date()
    # current_date = datetime(year=2023, month=12, day=27)
    start = timedelta(days=(5 - current_date.weekday())) + current_date
    end = timedelta(days=7) + start
    list_period = []
    while start < end:
        temp_list = (start.month, start.day)
        list_period.append(temp_list)
        start += timedelta(days=1)
    return list_period


def compare_date(list_users: list) -> list:
    list_peiod = get_period_birth()
    current_year = datetime.now().date()
    result_list = []
    # if len(list_users) == 0:
    #     return f'not users in list'
    for i in list_users:
        birth = i['birthday']
        user_birth = (birth.month, birth.day)
        if user_birth in list_peiod:

            if current_year.month > birth.month:
                age = current_year.year - birth.year + 1
                birth = birth.replace(year=current_year.year+1)

            else:
                age = current_year.year - birth.year
                birth = birth.replace(year=current_year.year)
            new_user_info = {"day": birth.day,
                             "name": i["name"], "birthday": birth, "age": age}
            result_list.append(new_user_info)

    # print(result_list)
    return result_list


def get_birthdays_per_week(users: list) -> list:
    list_birth_users = compare_date(users)
    result_list = []
    for i in list_birth_users:
        birth = i['birthday']
        temp_list = (birth.strftime("%A"), i["name"], i["age"])
        result_list.append(temp_list)
        # result_list.append(
        #     f'{birth.strftime("%A")} {i["name"]} age {i["age"]}')
        # print(temp_list)
    # print(result_list)
    return result_list


def get_result_list(users: list) -> None:
    finish_list = get_birthdays_per_week(users)
    # finish_list.sort()
    for i in finish_list:

        print(f'{i[0]} {i[1]} age {i[2]}')
        # print(f'{i[0]} {i[1]}')
        # print(i)
    return None


if __name__ == "__main__":
    # get_period_birth()
    # compare_date(list_users)
    # get_birthdays_per_week(list_users)
    get_result_list(list_users)
