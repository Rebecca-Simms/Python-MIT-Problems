def permute(letter, words):
    permutes = []
    for w in words:
        i = 0
        while i <= len(w):
            permutes.append(w[:i] + letter + w[i:])
            i += 1

    return(permutes)

#new_word = 'a'
#letter = 'b'

#print(permute(letter, new_word))


def get_permutations(sequence):
    permutations = []
    if len(sequence) == 1:
        permutations.append(sequence)
        return(permutations)
    else:
        word = sequence[0]
        for j in range(0,len(sequence)-1):
            letter = sequence[j+1]
            word = permute(letter, word)
    return(word)








#sequence = 'abc'
#print(len(sequence))
#print(get_permutations(sequence))

#letter = 'c'
#new_word = ['ab', 'ba']

#print(permute(letter, new_word))

sequence = 'abc'

print(get_permutations(sequence))

