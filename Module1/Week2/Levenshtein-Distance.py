def levenshtein_distance(str1, str2):

   # Construct a storage matrix with len(str1)+1 rows and len(str2)+1 columns, initialize all elements to 0
    distances = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]

    '''create the value for the first column/first row,
     which is the number of steps required to turn the string str1/str2 into an empty string
      by deleting/inserting all characters.'''
    for s1 in range(len(str1)+1):
        distances[s1][0] = s1
    for s2 in range(len(str2)+1):
        distances[0][s2] = s2

   # Calculate the Levenshtein distance

    for s1 in range(1, len(str1)+1):
        for s2 in range(1, len(str2)+1):
            if str1[s1-1] == str2[s2-1]:
                distances[s1][s2] = distances[s1-1][s2-1]

            else:

                a = distances[s1-1][s2-1]  # replace
                b = distances[s1][s2-1]  # insert
                c = distances[s1-1][s2]  # delete
                distances[s1][s2] = 1 + min(a, b, c)

    return distances[len(str1)][len(str2)]


print(levenshtein_distance(" hola ", " hello "))
