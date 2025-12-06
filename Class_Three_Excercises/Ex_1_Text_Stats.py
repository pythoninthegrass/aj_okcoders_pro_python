# Create a text analyzer with the following metrics (return a dictionary):

# Word count
# Character count
# Line count
# Average word length
# Most common word
# Longest word
# Sentence count

import os
from Ex_1_Helpers.helpers import get_word_count, get_character_count, get_average_length_of_words, get_most_common_word, get_longest_word, get_sentence_count
from typing import Optional

def get_text_file_path() -> str:
    return os.path.join(os.path.dirname(__file__), 'passage.txt')

def analyze_this(user_option: str, text: Optional[str] = None) -> None:
    words_list: str
    lines_list: str
    total_lines: 0 | str
    
    if user_option == '1':
        words_list = text.split()
    else:
        with open(get_text_file_path(), 'r') as word_file:
          words_list = word_file.read().split()

    if len(words_list) == 0:
        print('No text was entered; nothing to analyze')
        return

    # Get the total word count
    total_words = get_word_count(words_list)

    # Get the character count not counting spaces/whitespace
    total_characters_without_spaces = get_character_count(words_list)

    # Get the total line count
    if user_option == '1':
        total_lines = 'N/A'
    else:
        with open(get_text_file_path(), 'r') as word_file:
            lines_list = word_file.readlines()
            total_lines = len(lines_list)

    # Get the average word length
    average_word_length = get_average_length_of_words(words_list)

    # Get the most common word and its count
    most_common_word, count = get_most_common_word(words_list)

    # Get the longest word
    longest_word, longest_word_length = get_longest_word(words_list)

    # Get the total sentence count
    total_sentences = get_sentence_count(words_list)

    # Add to dictionary
    stats = {
        'Total words': total_words,
        'Total characters (w/o spaces)': total_characters_without_spaces,
        'Total lines': total_lines,
        'Avg. length of words': average_word_length,
        'Most common word': most_common_word,
        'Most common word count': count,
        'Longest word': longest_word,
        'Longest word length': longest_word_length,
        'Sentence count': total_sentences
    }

    # Show all statistics
    print('Showing statistics from the default passage:\n')
    print(f'Total number of words: {stats['Total words']}\n'
          f'Total characters (w/o spaces): {stats['Total characters (w/o spaces)']}\n'
          f'Total number of lines: {stats['Total lines']}\n'
          f'Average length of words: {stats['Avg. length of words']}\n'
          f'Most common word: "{stats['Most common word']}"; its frequency: {stats['Most common word count']}\n'
          f'Longest word: "{stats['Longest word']}", with a length of {stats['Longest word length']} characters\n'
          f'Total sentences: {stats['Sentence count']}\n')

def run_program():
    while True:
        print('Enter "1" to paste your own block of text/passage/paragraph etc, or\n'
        'enter "2" to see an analysis of the pre-built word passage. Enter "q" at any time to quit:\n')

        user_choice = input('> ')

        if user_choice == "q":
            break
        
        if user_choice == '1':
            print('Ok, enter/paste your word passage or the text you wish to have analyzed below:\n')

            user_text = input('> ')

            analyze_this('1', user_text)
        elif user_choice == '2':
            analyze_this('2')
        else:
            print('Sorry, you entered an invalid choice. Please check your entry and try again.')

if __name__ == "__main__":
    run_program()