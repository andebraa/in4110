# IN3110-andebraa

# move:
  moves files from one directory to another. can be limited to certain types
  ###### Args:
    *source* (str): source directory the files are moved from
    *destination* (str): directory the files are moved to
    *type* (str): file extension of files you wish to move
  ###### Returns:
    none

# wordcount.py:
  prints the number of lines, words and characters in given file or all files in directory.

  ###### Args:
    *filename* (str, optional): file that is to be counted  
    '*' (str, optional): all files in directory are counted
    *extension* (str, optional): limit the types of files that are counted

  ###### Returns:
    none

  ###### Raises:
    *IndexError*: If no command line arguments are given

  ###### Example:
    >>> wordcount.py * ".txt"
    >5 11 48 test_file2.txt
    >7 16 69 test_file.txt
