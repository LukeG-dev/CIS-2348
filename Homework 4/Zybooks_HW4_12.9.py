# Luke Gilin
# 1216992
# 5/5/2021


# Split input into 2 parts: name and age
parts = input().split()
name = parts[0]

while name != '-1':

    try:
        age = int(parts[1]) + 1
    except ValueError as xcpt:
        age = 0

# FIXME: The following line will throw ValueError exception.
# Insert try/except blocks to catch the exception.

    print('{} {}'.format(name, age))

# Get next line
    parts = input().split()
    name = parts[0]
