import matplotlib.pyplot as plt
'''suits = ["C", "S", "H", "D"]
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
cards = []
for suit in suits:
    for rank in ranks:
        cards.append(rank+suit)'''
origCards = [i for i in range(1, 13)]
cards = [i for i in range(1, 13)]

def leftShuffle(cards):
    leftCut = cards[:int(len(cards)/2)]
    rightCut = cards[int(len(cards)/2):]
    #print(leftCut, rightCut)
    final = []
    for i in range(int(len(cards)/2)):
        final.append(leftCut[i])
        final.append(rightCut[i])
    return final
    
def rightShuffle(cards):
    leftCut = cards[:int(len(cards)/2)]
    rightCut = cards[int(len(cards)/2):]
    #print(leftCut, rightCut)
    final = []
    for i in range(int(len(cards)/2)):
        final.append(rightCut[i])
        final.append(leftCut[i])
    return final


'''
for i in range(19):
    print(str(i) + ": " + str(cards))
    cards = leftShuffle(cards)
    '''

print("LEFTSHUFFLE")
leftNums = []
for i in range(2, 63, 2):
    origCards = [i for i in range(1, i+1)]
    cards = [i for i in range(1, i+1)]
    shuffleCount = 1
    cards = leftShuffle(cards)
    while cards != origCards:
        cards = leftShuffle(cards)
        shuffleCount += 1
    print(str(i) + " cards: " + str(shuffleCount))
    leftNums.append(shuffleCount)


print("RIGHTSHUFFLE")
rightNums = []
for i in range(2, 63, 2):
    origCards = [i for i in range(1, i+1)]
    cards = [i for i in range(1, i+1)]
    shuffleCount = 1
    cards = rightShuffle(cards)
    while cards != origCards:
        cards = rightShuffle(cards)
        shuffleCount += 1
    print(str(i) + " cards: " + str(shuffleCount))
    rightNums.append(shuffleCount)


x_values = [i for i in range(2,63,2)]

# Create the line plot
plt.plot(x_values, leftNums)

# Add labels and title for clarity
plt.xlabel('Number of Cards')
plt.ylabel('Shuffles')
plt.title(' Line Graph')

# Display the plot
plt.show()