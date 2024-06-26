
def count_words(file_path):

    with open(file_path, 'r') as file:
        sentences = file.readlines()
    counter={}
    for sentence in sentences:
        sentence = sentence.lower().replace('.', '').replace(',', '')
        words = sentence.split()
        for word in words:
            if word in counter:
                counter[word] += 1
            else:
                counter[word] = 1
    return counter

if __name__ == "__main__":
    file_path = 'C:/Users/DeLL/Desktop/Github/AIO-Exercise/Module1/Week2/P1_data.txt'
    print(count_words(file_path))
