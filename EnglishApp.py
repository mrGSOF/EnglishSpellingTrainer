import random
import winsound, os

def Dice(Min=1, Max=7):
    x = int(random.uniform(Min,Max))
    return x

def Dice_Exclude(Min=1, Max=7, ExList=[]):
    again = True
    while again==True:
        again = False
        x = Dice(Min, Max)
        for ex in ExList:
            if x == ex:
                again = True
    return x

    
word_path = './Words/'
sound_path = './Sounds/'
word_list = os.listdir(word_path)
again = True
while again == True:
    level = input('Choose difficulty level (A,B): ')
    if ((level.lower() == 'a') or (level.lower() == 'b')):
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

while (words>0):
    word_number = Dice(0,len(word_list))
    if level.lower()=='a':
        x1 = Dice_Exclude(0,len(word_list), ExList=[word_number])
        x2 = Dice_Exclude(0,len(word_list), ExList=[word_number, x1])
        x3 = Dice_Exclude(0,len(word_list), ExList=[word_number, x1, x2])
        options = [word_number, x1,x2,x3]
        options.sort()
        #print options
        for i, op in enumerate(options):
            print('%d. %s'%(i+1, word_list[op].split('.')[0]))
        again = True
        while again == True:
            winsound.PlaySound(word_path+word_list[word_number], winsound.SND_FILENAME)
            user = input('Choose the word (1,2,3,4): ')
            if user.isdigit():
                user = int(user) -1
                if ((user >=0) and (user <4)):
                    again = False

        user_word = word_list[options[user]].split('.')[0]
        if user_word == word_list[word_number].split('.')[0]:
            winsound.PlaySound(sound_path +'Good.wav', winsound.SND_FILENAME)
            print('Excellent!\n')
            words -= 1
        else:
            winsound.PlaySound(sound_path +'Error.wav', winsound.SND_FILENAME)
            print('Try again\n')
    else:
        winsound.PlaySound(word_path+word_list[word_number], winsound.SND_FILENAME)
        user_word = input('What was the word? ')
        if user_word.lower() == (word_list[word_number].split('.')[0]).lower():
            winsound.PlaySound(sound_path +'Good.wav', winsound.SND_FILENAME)
            print('Excellent!\n')
            words -= 1
        else:
            winsound.PlaySound(sound_path +'Error.wav', winsound.SND_FILENAME)
            print('Try again\n')

winsound.PlaySound(sound_path +'Finish.wav', winsound.SND_FILENAME)
