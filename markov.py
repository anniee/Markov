# !/usr/bin/env python

from sys import argv

def unpack_file(input_file):
    file_object = open(input_file)

    word_bank_list = []
    for line in file_object:
        line = line.rstrip()
        line = line.split()
        word_bank_list += line
    return word_bank_list


def make_chains(word_bank_list):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""


    markov_chain_dict = {}

    for i in range(len(word_bank_list)):
        if word_bank_list[i] == word_bank_list[-1]:
            continue
        else:
            tupled = tuple([word_bank_list[i],word_bank_list[i+1]])
            if tupled in markov_chain_dict:
                markov_chain_dict[tupled] = markov_chain_dict[tupled] + [word_bank_list[i+2]]
                #this is where we'll add value after it to the list value of the existing one
            else:
                if word_bank_list[i+1] == word_bank_list[-1]:
                    continue
                else:
                    markov_chain_dict[tupled] = [word_bank_list[i+2]]

    return markov_chain_dict


    


#     return {}

# def make_text(chains):
#     """Takes a dictionary of markov chains and returns random text
#     based off an original text."""
#     return "Here's some random text."

def main(input_file):
    word_bank_list = unpack_file(input_file)
    place_holder = make_chains(word_bank_list)
    print place_holder
#     # args = sys.argv

#     # Change this to read input_text from a file
#     input_text = "Some text"

#     chain_dict = make_chains(input_text)
#     random_text = make_text(chain_dict)
#     print random_text

if __name__ == "__main__":
    input_file = argv[1]
    main(input_file)