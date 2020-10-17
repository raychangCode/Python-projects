"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
DIC_NAMES = []                # This list has all the name from the FILE
ANAGRAMS = []                 # This list stores all the anagrams
count = 0
TMP = []                      # This list stores the temporary sub_string combination of the given word


def main():

    print('Welcome to stanCode \"Anagram Generator\" (or -1 to exit)')

    while True:
        target_str = input("Find anagrams for:")
        target_str = target_str.lower().strip()
        read_dictionary(target_str)

        if target_str == EXIT:
            return -1
        else:
            print('Searching...')
            find_anagrams(target_str)

        if len(ANAGRAMS) > 0:
            print(f'{len(ANAGRAMS)} ANAGRAMS: {ANAGRAMS}')
        else:
            print('No anagrams found')
        print(count)
        empty(ANAGRAMS)
        empty(TMP)
        empty(DIC_NAMES)


def empty(lst):
    """
    Clear the list
    :param lst: target lst
    :return:
    """
    global count
    count = 0
    for i in range(len(lst)):
        lst.pop()


def read_dictionary(s):
    """
    Get the word from dictionary as long as the word is long as the target string.
    :param s: The target string
    :return:
    """
    global DIC_NAMES
    with open(FILE) as f:
        for line in f:
            name = line.strip()
            if len(name) == len(s):
                for ch in s:
                    if name.find(ch) != -1:
                        DIC_NAMES.append(name)


def find_anagrams(s):
    """
    :param s: The target string
    :return:
    """
    global ANAGRAMS

    if s in DIC_NAMES:
        ANAGRAMS.append(s)
        print(f'Found: {s}')
        print('Searching...')
        find_anagrams_helper(s, '')
    else:
        pass


def find_anagrams_helper(s, curr_s):
    """
    Find the target string's anagrams
    :param s:  The target string
    :param curr_s: Temporary sub_sting
    :return:
    """
    global ANAGRAMS
    global count
    global TMP
    count += 1

    if curr_s in DIC_NAMES:
        # if curr_s not in ANAGRAMS:
        ANAGRAMS.append(curr_s)
        print(f'Found: {ANAGRAMS[len(ANAGRAMS)-1]}')
        print('Searching...')
    else:
        for ch in s:
            # Check duplicate alphabet
            c = s.count(ch)
            if curr_s.find(ch) == -1:
                # Choose
                curr_s += ch
                if has_prefix(curr_s) and curr_s not in ANAGRAMS and not_checked_before(curr_s):
                    if len(curr_s) < len(s) and curr_s not in TMP:
                        TMP.append(curr_s)
                    # Explore
                    find_anagrams_helper(s, curr_s)
                # Un-choose
                curr_s = curr_s[:-1]
            else:
                if c >= 2:
                    curr_s += ch
                    if curr_s.count(ch) <= c and has_prefix(curr_s) and curr_s not in ANAGRAMS and not_checked_before(curr_s):
                        if len(curr_s) < len(s) and curr_s not in TMP:
                            TMP.append(curr_s)
                        find_anagrams_helper(s, curr_s)
                    curr_s = curr_s[:-1]


def not_checked_before(s):
    """
    This function will check the sub_string has been in the recursive case or not
    :param s: The sub_string in recursive case
    :return:
    """
    global TMP
    if s in TMP:
        return False
    else:
        return True


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    for name in DIC_NAMES:
        if name.startswith(sub_s):
            return True


if __name__ == '__main__':
    main()
