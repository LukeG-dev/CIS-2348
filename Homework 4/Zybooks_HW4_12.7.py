#  Luke Gilin
#  1216992
#  5/4/2021


def fat_burning_heart_rate(age):
    fat_rate = .7 * (220 - age)
    format(fat_rate, '.1f')
    return fat_rate


def get_age():
    user_age = int(input())
    if user_age < 18 or user_age > 75:
        raise ValueError('Invalid age.')
    else:
        fat = fat_burning_heart_rate(user_age)
        print('Fat burning heart rate for a {user_age} year-old: {fat} bpm'.format(user_age=user_age, fat=fat))


if __name__ == '__main__':

    try:
        get_age()

    except ValueError as xcpt:
        print(xcpt)
        print('Could not calculate heart rate info.\n')





