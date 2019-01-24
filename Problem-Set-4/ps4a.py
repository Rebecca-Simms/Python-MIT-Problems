# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx


def permute(letter, words):
    permutes = []
    for w in words:
        i = 0
        while i <= len(w):
            permutes.append(w[:i] + letter + w[i:])
            i += 1

    return(permutes)

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return([sequence])
    else:
        word = sequence[0]
        for j in range(0,len(sequence)-1):
            letter = sequence[j+1]
            word = permute(letter, word)
    return(word)



if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)


    sequence1 = 'a'
    sequence2 = 'abc'
    sequence3 = 'bust'
    sequence4 = 'words'

    print(get_permutations(sequence1))
    print(get_permutations(sequence2))
    print(get_permutations(sequence3))
    print(get_permutations(sequence4))
