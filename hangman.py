class hangman:
    def __init__(self,word):
        self.word = list(word)
        self.Guess = []
        self.Guess.extend(['_' for i in self.word])
        self.score = 0
    
    def check(self, letter):
        if letter in self.word:
            j = []
            for index, item in enumerate(self.word):
                if item == letter:
                    j.append(index)
            for i in j:
                self.Guess[i] = letter
            return self.ShowGuess()
        else:
            wrongGuess = 'there is no \'{}\' in the word'
            self.score += 1
            return wrongGuess.format(letter) + '\n' + self.ShowGuess()
        
    def points(self):
        return self.score < 7

    def ShowGuess(self):
        x = ''.join(self.Guess)
        return x


Hangman = hangman(input('choose the word: ',))


while Hangman.word != Hangman.Guess:
    if Hangman.score():
        print('you lose')
        break
    print(Hangman.check(input("choose a letter:")))
else:
    print('correct! the word was: '+ Hangman.ShowGuess())


'''
[
    ---------------,
      ____         ,
     |/  |         ,
     |  (_)        ,
     |  /|\        ,
     |   |         ,
     |  / \        ,
     |_____        ,
     /     \       ,
     --------------
]

Man = ["  ____         "," |/  |         "," |  (_)       "," |  /|\        "," |   |         "," |  / \        "," |_____        "," /     \       "]

'''