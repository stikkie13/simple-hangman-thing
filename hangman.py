class hangman:
    def __init__(self,word):
        self.word = list(word)
        self.Guess = ['_' for i in self.word]
        self.score = 0
    
    def check(self, letter):
        if letter in self.word:
            j = []
            for index, item in enumerate(self.word):
                if item == letter:
                    j.append(index)
            for i in j:
                self.Guess[i] = letter
        else:
            self.score += 1
        
    def points(self):
        return self.score > 5

    def ShowGuess(self):
        x = ''.join(self.Guess)
        return x



'''
while Hangman.word != Hangman.Guess:
    if Hangman.points():
        print('you lose')
        break
    print(Hangman.check(input("choose a letter:")))
else:
    print('correct! the word was: '+ Hangman.ShowGuess())
'''