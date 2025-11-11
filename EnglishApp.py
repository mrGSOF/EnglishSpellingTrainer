### Cute English exercise software to train kids and teach procedural programming.
### By: Guy Soffer (GSOF) 2019

import os, random
try:
    import winsound
    def playFile(filename) -> None:
        winsound.PlaySound(filename, winsound.SND_FILENAME)
except:
    try:
        import playsound
        def playFile(filename) -> None:
            playsound.playsound(filename)
    except:
        raise ("No sound support\nPlease <pip install playsound>\nand retry\n")
            

def Dice(Min=1, Max=6) -> int:
    x = int(random.randint(Min, Max))
    return int(x)

def Dice_Exclude(Min=1, Max=6, ExList=[]) -> int:
    again = True
    while again==True:
        again = False
        x = Dice(Min, Max)
        for ex in ExList:
            if x == ex:
                again = True
    return int(x)

def getListOfDecoyWords(wordList, excludeWord) -> list:
    N = len(wordList) -1
    x1 = Dice_Exclude(0, N, ExList=[excludeWord])
    x2 = Dice_Exclude(0, N, ExList=[excludeWord, x1])
    x3 = Dice_Exclude(0, N, ExList=[excludeWord, x1, x2])
    options = [excludeWord, x1,x2,x3]
    options.sort()
    return options
    
def checkSpelling(word1, word2) -> int:
    if word1.lower() == word2.lower():
        playGood()
        return 1
    else:
        playError()
        return 0

def playGood() -> None:
    playFile(sound_path +'Good.wav')
    print('Excellent!\n')
    
def playError() -> None:
    playFile(sound_path +'Error.wav')
    print('Try again\n')

    
word_path = './Words/'
sound_path = './Sounds/'
word_list = os.listdir(word_path)

try:
    import pysole
    ps = True
except:
    ps = False
    print("****************************************************")
    print("* For better visuals use <pip install liveconsole> *")
    print("****************************************************")

if ps:
    ### For better visuals
    pysole.probe(runRemainingCode=True,
                 printStartupCode=False,
                 primaryPrompt='eng>> ',
                 font='Consolas',
                 fontSize=20,
                 )

again = True
while again == True:
    level = input('Choose difficulty level (A,B,C): ')
    level = level.lower()
    if ((level == 'a') or (level == 'b') or (level == 'c')):
        again = False
    else:
        print('\n')

again = True
while again == True:
    words = input('How many words? ')
    if words.isdigit():
        words = int(words)
        again = False
    else:
        print('\n')

while words > 0:
    word_number = Dice(0, len(word_list)-1) #< Randomly choose a new word 
    if level == 'a':
        ### Print list of options
        options = getListOfDecoyWords(word_list, word_number)
        for i, op in enumerate(options):
            print('%d. %s'%(i+1, word_list[op].split('.')[0]))

        again = True
        while again == True:
            playFile(word_path+word_list[word_number])
            user = input('Choose the word (1,2,3,4): ')
            if user.isdigit():
                user = int(user) -1
                if ((user >=0) and (user <4)):
                    again = False

        user_word = word_list[options[user]].split('.')[0]
        words -= checkSpelling(user_word, word_list[word_number].split('.')[0])

    elif level == 'b':
        ### Print list of options
        options = getListOfDecoyWords(word_list, word_number)
        for i, op in enumerate(options):
            print('- %s'%(word_list[op].split('.')[0]))
        
        again = True
        while again == True:
            playFile(word_path+word_list[word_number])
            user_word = input('What was the word? ')
            words_Z1 = words
            words -= checkSpelling(user_word, word_list[word_number].split('.')[0])
            if words != words_Z1:
                again = False #< Repeat the same word if an error

    else:
        playFile(word_path+word_list[word_number])
        user_word = input('Type the word? ')
        words -= checkSpelling(user_word, word_list[word_number].split('.')[0])

playFile(sound_path +'Finish.wav')
