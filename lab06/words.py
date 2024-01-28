import os
import string

def read_words(text_file):
    list_of_words = []
    filepath = os.path.join(os.path.dirname(__file__), text_file)
    for line in open(filepath, encoding='utf-8'):
        word = line
        word2 =  word.strip(string.punctuation + string.whitespace)
        word3 = word2.lower()
        list_of_words.extend(word3.split())
    

    new_list = [word.replace(',','').replace('.','') for word in list_of_words]

    return new_list


def count_only(word_list, provinces):
    provinces_set = set(provinces)
    my_dict = {}

    for word in word_list:
        if word in provinces_set:
            if word in my_dict:
                my_dict[word] = my_dict.get(word) + 1
            else:
                my_dict[word] = 1 

    return my_dict

##lista av ord
def count_all_except(word_list, provinces):
    provinces_set = set(provinces)
    my_dict = {}
    
    for word in word_list:
        if word not in provinces_set:
            if word in my_dict:
                my_dict[word] = my_dict.get(word, 1) + 1
            else:
                my_dict[word] = 1
    

    my_list = list(my_dict.items())

    sorted_list = sorted(my_list, key=lambda x: x[1], reverse=True)


    return sorted_list
    
     








words = read_words('nilsholg.txt')
stopwords = read_words('undantagsord.txt')

hist = count_all_except(words,stopwords)
##provinces = read_words('landskap.txt')
##hist = count_only(words, provinces)
##print(hist)

print(hist[0:21])