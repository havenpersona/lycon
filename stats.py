import numpy as np
import glob
import re
from collections import Counter
pattern = r"[^a-zA-Z0-9''-]"
word_counts = []
line_counts = []
section_counts = []
unigrams = []
bigrams = []
trigrams = []
path_list = glob.glob("./dataset/*.txt")
for file_path in path_list:
    with open(file_path, 'r') as file:
        file_content = file.read()
        sections = file_content.split("\n\n")
        section_counts.append(len(sections))
        this_line_counts = []
        this_word_counts = []
        for section in sections:
            lines = section.split("\n")
            lines = [line for line in lines if len(line)]
            
            lines = [line for line in lines if line[0] != '(' or line[-1] != ')']
            
            this_line_counts.append(len(lines))
            line_word_counts = np.sum(np.array([len(line.split(" ")) for line in lines]))
            this_word_counts.append(line_word_counts)
            for line in lines:
                words = line.split(" ")
                word = [re.sub(pattern, '', word.lower()) for word in words]
                unigrams.extend(word)
                bigrams.extend([(word[i], word[i+1])for i in range(len(word) - 1)])
                trigrams.extend([(word[i], word[i+1], word[i+2])for i in range(len(word) - 2)])
        
        line_counts.append(np.sum(np.array(this_line_counts)))
        word_counts.append(np.sum(np.array(this_word_counts)))

print("the average word count is ", np.average(np.array(word_counts)))
print("the average line count is ", np.average(np.array(line_counts)))
print("the average section count is ", np.average(np.array(section_counts)))
print("the total unique unigram count is ", len(Counter(unigrams)))
print("the total unique bigram count is ", len(Counter(bigrams)))
print("the total unique trigram count is ", len(Counter(trigrams)))