import csv
import random

def main():
    print("Welcome to the Fun Game called GTSN 'Guess the song name'.\nFollowing are the rules:\n\t1. Login with Proper Credentials(Username&Password).\n\t2. A random song will be picked and displayed to you of which the first letters of each word in the title will be displayed for you to guess.\n\t3. The artist/composer of the song will also displayed for you to guess.\n\t4. On every correct guess, you will get 3 points.\n\t5. On every correct guess in the second attempt, you will get 1 point.\n\t6. Guessing incorrectly for the third time will end the game and points will be displayed to you.\n\t7. Game continues on each correct answer till the max points.\n\t8. Max points: 45")
    print("\nLogin Required!! Kindly Login")
    username = input('Enter your username: ')
    if username == "gamerish":
        password = input('Enter your password: ')
        if password == "gamer123#":
            playGame()
        else:
            print("\nWrong Password:\nCome Back Later!! Namaste /\\")
    else:
        print("\nWrong Username Or Username not Found:\nCome Back Later!! Namaste /\\")

def playGame():
    print("\n\nLets Start!!")

    initials = []
    artists = []
    titles = []
    
    with open('songs.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            initials.append(row.get('initials'))
            artists.append(row.get('artist'))
            titles.append(row.get('title'))
        songsCount = len(initials)

    guessCount = 0
    score = 0
    should_continue = True
    while(guessCount < 2 and should_continue):
        index = random.randrange(0, songsCount)
        print(f'\n\nGuess the song with following details:\n\tArtist/Composer: {artists[index]} \n\tInitials: {initials[index]} ')

        while (True):
            song_name = input('\nEnter SongName: ')
            guessCount = guessCount + 1
            if song_name.lower() == titles[index].lower():
                if guessCount == 1:
                    score = score + 3
                elif guessCount == 2:
                    score = score + 1
                guessCount = 0
                print(f'Correct answer!! Your score is: {score}')
                break
            else:
                if guessCount >= 2:
                    should_continue = False
                    print("OOPS!! Wrong Again!! Game will end now!\n\n")
                    break
                else:
                    print("OOPS!! Wrong answer!! Last chance!! Try Again ")

    print(f'\n\n###Game ended###\nYour score is: {score}\n\n')

if __name__ == '__main__':
    main()