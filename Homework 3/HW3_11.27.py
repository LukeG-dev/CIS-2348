#  Luke Gilin
#  1216992

if __name__ == '__main__':
    playerOneNumber = int(input("Enter player 1's jersey number:\n"))
    playerOneRating = int(input("Enter player 1's rating:\n\n"))
    playerTwoNumber = int(input("Enter player 2's jersey number:\n"))
    playerTwoRating = int(input("Enter player 2's rating:\n\n"))
    playerThreeNumber = int(input("Enter player 3's jersey number:\n"))
    playerThreeRating = int(input("Enter player 3's rating:\n\n"))
    playerFourNumber = int(input("Enter player 4's jersey number:\n"))
    playerFourRating = int(input("Enter player 4's rating:\n\n"))
    playerFiveNumber = int(input("Enter player 5's jersey number:\n"))
    playerFiveRating = int(input("Enter player 5's rating:\n\n"))

    Players = {playerOneNumber: playerOneRating, playerTwoNumber: playerTwoRating,
               playerThreeNumber: playerThreeRating, playerFourNumber: playerFourRating,
               playerFiveNumber: playerFiveRating}
    print('ROSTER')

    for i in sorted(Players):
        print('Jersey number: {num}, Rating: {rate}'.format(num=i,rate=Players[i]))
    print()
    print('MENU')
    print('a - Add player')
    print('d - Remove player')
    print('u - Update player rating')
    print('r - Output players above a rating')
    print('o - Output roster')
    print('q - Quit\n')
    input('Choose an option:\n')

