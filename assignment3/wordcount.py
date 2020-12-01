import sys
import os

def wordcount(filename):
    """
    count number of lines, words and characters in file argument
    Args:
        filename: Name of file to be read and counted (include file extention)
    Returns:
        int: line_cnt; number of lines in file
        int: word_cnt; number of words in file
        int: char_cnt; number of characters in file
        str: filename; name of file given in argument
    Examples:
        >>> wordcount.py [filename.txt] * ".txt"
        5 11 48 filename.txt
    """
    infile = open(str(filename), 'r')
    line_cnt = 0
    word_cnt = 0
    char_cnt = 0
    for line in infile:
        line_cnt += 1
        words = line.split()
        for elem in words:
            word_cnt += 1
            char_cnt += len(elem)

    print(f"{line_cnt} {word_cnt} {char_cnt} {filename}")
    infile.close()
    return line_cnt, word_cnt, char_cnt

if len(sys.argv) < 2:
    raise IndexError('\n usage: wordcount.py [filename] \n or wordcount.py * [file extention]"')

file_ext = [".txt", ".py", ".pdf", ".dat"]
if any(i for i in file_ext if i in sys.argv):
    for root, dirs, files in os.walk("."):
        for elem in files:
            if elem.endswith(str(sys.argv[-1])):
                wordcount(str(elem))


elif len(sys.argv) > 2: #asumes input "WC.py *", this is a bash command that passes
                        #all files in directory as arguments
    for f in [f for f in os.listdir('.') if os.path.isfile(f)]:
        wordcount(str(f))
else:
    wordcount(str(sys.argv[1]))
