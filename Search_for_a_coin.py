#Game to search for a coin. 
import random

locations = ['Flower Bed', 'Park Bench', 'Picnic Table', 'Forest', 'Pond', 'Playground', 'Gazebo', 'Fountain', 'Statue', 'Bridge']
print('You have 5 guesses to find a coin that is randomly hidden!')
print('The coin could be hidden in one of the following locations:')
for location in locations:
    print(f"- {location}")
coin = random.choice(locations)
for i in range(5):
    guess = input('Where do you think the coin is? ')
    if guess == coin:
        print('Congratulations! You found the coin!')
        break
    else:
        print('Sorry, that is not correct. Try again!')
        i += 1
        if i == 5:
            print(f"Game Over! The coin was hidden in the {coin}.")
