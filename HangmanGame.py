import random
import os
clear = lambda: os.system('cls')

# List of random words
wordsList = ('apple airplane antelope baboon balloon beach bear bicycle '
         'bison boat buffalo bulldozer bus butterfly camel car caravan '
         'cardiff cat chicago chimpanzee city clock cloud computer cow '
         'crane crow dallas deer detroit dog donkey dragonfly eagle '
         'elephant falcon firetruck fish flamingo frog giraffe goat '
         'goose helicopter hill hippopotamus hornet house husky jaguar '
         'jeep jellyfish kangaroo kayak kingfisher kite koala lion lizard '
         'llama london lotus lynx madrid mammoth manatee marlin meadow '
         'miami minneapolis mole monkey moose motorcycle mouse mule '
         'newt orlando otter owl oxford panda parakeet parrot peacock '
         'pelican penguin phoenix pigeon pony prague python quail rabbit '
         'raccoon ram rat raven rhino river salmon seagull shark sheep '
         'shrimp skunk sloth snail snake spider squirrel stork swan '
         'tank tiger toad tokyo toronto tortoise tractor trailer truck '
         'trumpet tulip turtle vancouver van vegas vulture wallaby walrus '
         'wasp weasel whale wolverine yak yacht zebra zorilla aardvark '
         'albany alligator alphard amsterdam ant arcadia armadillo atlanta '
         'austin backhoe bagpipe baltimore bangkok bat beaver beijing '
         'beetle beluga bison boar bobcat boston boxcar bridge brisbane '
         'buffalo bulldozer butterfly cab cairo caracas cardinal catfish '
         'chameleon cheetah chicken chinchilla cincinnati cleveland cockroach '
         'columbia corolla crab crane cricket crocodile crow detroit dolphin '
         'dove dragonfly durban eagle echidna edmonton elephant emu falcon '
         'firefly flamingo florida ford fox frog gazelle gecko giraffe '
         'goldfish gorilla grasshopper guppy hamster hawk hedgehog heron '
         'hippopotamus hong kong hornet horse hummingbird hyena ibis '
         'iguana jaguar jellyfish jersey jetta joey kangaroo kapok katydid '
         'kiwi kite koala lamborghini lemur leopard lion lizard llama '
         'lobster london lynx mack truck madrid magpie manatee manta '
         'meerkat miami minivan mole mongoose monkey moose mosquito '
         'motorboat mumbai muskrat mustang myanmar narwhal nebraska '
         'newark newt nightingale octopus okapi orlando ostrich otter owl '
         'oxford panda panther parakeet parrot peacock pelican penguin '
         'perth phoenix pig pigeon platypus pony porcupine porpoise puffin '
         'quail rabbit raccoon ram rat raven reindeer rhinoceros robin '
         'rooster sailboat salamander salmon sandpiper sardine saudi '
         'scorpion seahorse seal seattle shark sheep shrimp silkmoth '
         'skateboard skink skua skunk sloth snail snake sparrow spider '
         'squid squirrel stork swan tank tarantula taxi tiger toad tokyo '
         'toronto tortoise toucan tractor train tram truck tuna turkey '
         'turtle vancouver viper volkswagen vulture wallaby walrus '
         'wasp weasel whale wolverine wombat yak yacht zebra zorilla '
         'albacore arcadian armada austin bison buffalo camry cardinal '
         'caravel cattle caviar chevrolet chopper cityscape cloudscapes '
         'cougar crane crocodile crow dolphin dogfish donkey dragonfly '
         'drum eiffel emu falcon fiat flamingo ford fox frog gamecock '
         'gazelle giraffe goblin goose gopher gorilla grasshopper hawk '
         'hedgehog heron hippo hornbill horse hound hyena ibis impala '
         'jaguar jellyfish kachina kiwi kobra lamb lamborghini lark '
         'lemur lion lizard llama lobster macaw magpie manta meerkat '
         'mink minnow mole mongoose moose mosquito moth narwhal neon '
         'octopus orca owl oxford panda panther parakeet parrot penguin '
         'phoenix pig pigeon platypus porcupine puffin quail rabbit '
         'raccoon ram rat raven reindeer rhino robin rooster salamander '
         'salmon sandpiper sardine saudi scorpion seahorse seal shark '
         'sheep shrimp silkmoth skink skua skunk sloth snail snake '
         'sparrow spider squid squirrel stork swan tarantula tiger '
         'toad tortoise toucan turkey turtle vulture wallaby walrus '
         'wasp weasel whale wolverine yak yacht zebra zorilla adobe '
         'anchor angeles baker beach bonanza bradford bronco cadillac '
         'calypso canyon carly cedar charlotte cincinnati clydesdale '
         'collie corvette daisy denver devon dreamer echo eden eiffel '
         'fiesta flint francisco geneva glacier glory helix honolulu '
         'jasmine jupiter kenwood lancaster legend lexus lincoln lyra '
         'mercedes michigan montana mystic nashville nimbus nova olympia '
         'onyx orlando pegasus phoenix ranger rio roadrunner rover seattle '
         'serenity skyline sonora springfield tahoe tokyo toledo toronto '
         'triton tulsa utopia vanguard venice vespa victory voyager willow '
         'yukon').split()


#This is ascii art for the hangman lives
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#This will split the randomly chosen word into letters
word = [x for x in random.choice(wordsList)]

#This is the progress the User will make
guessingBlanks = []
for i in range(0,len(word)):
    guessingBlanks.append("_")

lives = 7

while lives>0:
    clear()
    print(HANGMANPICS[len(HANGMANPICS)-lives])
    #Printing the Progress
    for i in guessingBlanks:
        print(i, end = '  ')
    print("\n")
    guess = input("Guess a Letter : ").lower()

    # Checking if the guessed letter is in the word to be guessed 
    if not word.count(guess) == 0:
        #if word is in then the progress bar will display it to the user
        for i in range(0,len(word)):
            if word[i] == guess:
                guessingBlanks[i] = word[i]
    else:
        lives-=1
    #Checking if the User Won
    if guessingBlanks.count("_") == 0:
        print("You Won!!! Nice Job!!!")
        break
# Displaying Losing Message
if lives == 0 and guessingBlanks.count("_") > 0:
    print(f"\nYou Lose!!! \nWord was {''.join(word)}")