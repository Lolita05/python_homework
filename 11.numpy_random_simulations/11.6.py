#буквы во всех словах кроме первой и последней перемешаны

def word_shaker(string):
    word = string.split()
    f = []
    for word in words:
        if len(word) < 4: # если 3 буквы, то перемешивать нечего
            f.append(word)
            continue
        first = word[0]
        last = word[-1]
        word = list(word[1:-1])
        np.random.shuffle(word)
        word = first + "".join(word) + last
        f.append(word)
    return " ".join(f)

print(word_shaker('You are not entering this world in the usual manner, '
                  'for you are setting forth to be a Dungeon Master. '
                  'Certainly there are stout fighters, mighty magic-users, wily thieves, and courageous clerics who will make their mark in the magical '
                  'lands of D&D adventure. You however, are above even the greatest of these, for as DM you are to become the Shaper of the Cosmos. '
                  'It is you who will give form and content to the all the universe. '
                  'You will breathe life into the stillness, giving meaning and purpose to all the actions which are to follow.'))



