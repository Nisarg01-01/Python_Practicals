# Taking input of size of score array
size = int(input('\nEnter the total of scores wished to be input::'))

# Taking input of scores
Scores = list(int(score) for score in input('\nEnter the Scores separated by spaces::').strip().split())[:size]

# Finding Runner-up Score
Scores.sort()

index = size -1
max=Scores[index]

num = Scores.count(max)

runnerupIndex = index - num
print('\nRunner-Up score:: '+str(Scores[runnerupIndex]))