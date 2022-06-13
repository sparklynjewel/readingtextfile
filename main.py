import string


def read_file_content():
    with open(file_name) as file:
        file_content = file.read()
    return file_content


def count_words():
    text = read_file_content()
    text = text.translate(str.maketrans("", "", string.punctuation))
    word_count = {}
    spilt_text = text.split()

    for word in spilt_text:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count


file_name = input("enter the name of the file: ")
print(count_words())


