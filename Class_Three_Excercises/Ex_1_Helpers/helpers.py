import math, string, nltk
from nltk.tokenize import sent_tokenize

# This is called inside get_sentence_count, so I am putting it here by itself
def check_punkt_is_used():
    ''' Check to see that punkt is being used for tokenizing '''
    try:
        nltk.data.find("tokenizers/punkt")
    except LookupError:
        nltk.download("punkt")

    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        nltk.download("punkt_tab")

# --------------------------------------------------

def get_word_count(words_list) -> None:
    count = 0
    
    for word in words_list:
        count += 1

    return count

def get_character_count(words_list):

    # Get all of the words from the the list passed in into one, long continuous string, removing all spaces
    characters_string = ''.join(words_list)

    return len(characters_string)

def get_average_length_of_words(words_list):
    total_words = len(words_list)
    total_length = 0

    # Get the length of each word in the list of words that is passed in, then divide that total by the number of words in the list
    for word in words_list:
        total_length += len(word)

    average_word_length = math.floor(total_length / total_words)

    return average_word_length

def get_most_common_word(words_list):
    word_frequency = {}

    for word in words_list:
        # Remove punctuation from each word and convert to lower case for accurate counting
        cleaned_word = word.strip(string.punctuation).lower()

        if cleaned_word in word_frequency:
            word_frequency[cleaned_word] += 1
        else:
            word_frequency[cleaned_word] = 1

    # Get the most common word by using the max function available in Python.
    # Here, we are telling Python to get the key that has the maximum value
    most_common_word = max(word_frequency, key = word_frequency.get)

    # Now get the actual count of the most common word
    most_common_word_count = word_frequency[most_common_word]

    return most_common_word, most_common_word_count

def get_longest_word(words_list):
    word_lengths = {}

    # First, clean up all words so they are without any puntuation attached to them
    for word in words_list:
        cleaned_word = word.strip(string.punctuation).lower()

        # Now add each cleaned-up word to a dictionary as the key, registering its value as the length of each word
        if cleaned_word in word_lengths:
            continue
        else:
            word_lengths[cleaned_word] = len(cleaned_word)

    # Get the largest value of all the values - this is the longest word
    longest_word = max(word_lengths, key = word_lengths.get)

    # Since we have converted all words to lowercase previously, would be good to re-capitalize the first letter of the longest word, especially if there proper nouns
    longest_word_with_first_capital = str.capitalize(longest_word)

    # Additionally, get the legnth (value) of the longest word
    longest_word_value = word_lengths[longest_word]

    # Return both
    return longest_word_with_first_capital, longest_word_value

def get_sentence_count(words_list):
    # Ensure punkt is available and being used to tokenize text
    check_punkt_is_used()

    # Join words into a single string
    text = ' '.join(words_list)

    # Split text into sentences
    sentences = sent_tokenize(text)

    # Return the number of sentences
    return len(sentences)