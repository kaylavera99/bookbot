import string
def main():
    book_path = "books/frankenstein.txt"
    
    file_contents = getText(book_path)
    start_mark = "Letter 1"
    end_mark = "lost in darkness and distance"
    start_index = file_contents.find(start_mark)
    end_index = file_contents.find(end_mark) + len(end_mark)
    
    raw_text = file_contents[start_index:end_index].strip()


    num_words = wordCount(raw_text)
    print("\nWord count:", num_words)

    word_freq = getNumCount(file_contents.strip())
    #print("Word Freq", word_freq)

    char_count = getCharCount(file_contents.strip())
    print("Char count", char_count)

    x = formatReport(book_path, num_words, char_count)

        

def getText(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    


def wordCount(word_file):
    words = word_file.split()
    return len(words)

def getNumCount(text):

     for punct in string.punctuation:
          text = text.replace(punct, " ")
     text = text.split()

     word_dict = {}
     word_dict_keys = word_dict.keys()

     for word in text:
        word = word.lower()
        if word in word_dict_keys:
            word_dict[word] = word_dict[word] + 1
        else:
            word_dict[word] = 1
     return word_dict
        

def getCharCount(text):
    for punct in string.punctuation:
        text = text.replace(punct, " ")
    text = text.split()


    char_dict = {}
    char_dict_keys = char_dict.keys()

    for word in text:
        word = word.lower()
        for char in word:
            if char in char_dict_keys:
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1

    sorted_char_dict = dict(sorted(char_dict.items()))
    return sorted_char_dict


def formatReport(book_path, word_count, char_count):
    print("--- Begin report of", book_path, "---")
    print(word_count, " words found in the document")
    print()
    print()

    for key in char_count:
        if key.isalpha():

            print("The '{0}' character was found {1} times".format(key,char_count[key]))
        else:
            continue

    print("--- End report ---")

main()

