# Luke Gilin 1216992
# Zylabs 6.22 CIS 2348 LAB: Brute force equation solver


#  Get inputs from user
x_one = int(input())
y_one = int(input())
solve_for_one = int(input())
x_two = int(input())
y_two = int(input())
solve_for_two = int(input())


#  Create function to solve equation
def brute_force(x, y, solution):
    #  Create List to store solutions in
    solutions = []
    for i in range(-11, 10):
        for j in range(-11, 10):
            if ((x * i) + (y * j)) == solution:
                solutions.append('{x} {y}'.format(x=i, y=j))
    return solutions


#  Create function to compare solutions
def check_same_solutions(x1, y1, solution_1, x2, y2, solution_2):
    solution_set_1 = brute_force(x1, y1, solution_1)
    solution_set_2 = brute_force(x2, y2, solution_2)

    if len(solution_set_1) > len(solution_set_2):
        length = len(solution_set_1)
        for i in range(length):

            if solution_set_1[i] in solution_set_2:
                print(solution_set_1[i])
                break

            #  Print no solution if none is found
            if i == length - 1:
                print('No solution')
    else:
        length = len(solution_set_2)
        for i in range(length):
            if solution_set_2[i] in solution_set_1:
                print(solution_set_2[i])
                break

            #  Print no solution if none is found
            if i == length - 1:
                print('No solution')


#  Call solve and comparison function
check_same_solutions(x_one, y_one, solve_for_one, x_two, y_two, solve_for_two)
