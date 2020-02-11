"""
USE: python <PROGNAME> (options)
OPTIONS:
    -h : print this help message and exit
    -d FILE : use dictionary file FILE
    -i FILE : process text from input file FILE
    -o FILE : write results to output file FILE
"""
################################################################

import sys, getopt

################################################################

MAXWORDLEN = 5

################################################################
# Command line options handling, and help

opts, args = getopt.getopt(sys.argv[1:], 'hd:i:o:')
opts = dict(opts)

def printHelp():
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit()
    
if '-h' in opts:
    printHelp()

if len(args) > 0:
    print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
    printHelp()

if '-d' not in opts:
    print("\n** ERROR: must specify dictionary (opt: -d)! **", file=sys.stderr)
    printHelp()

if '-i' not in opts:
    print("\n** ERROR: must specify input text file (opt: -i)! **", file=sys.stderr)
    printHelp()

if '-o' not in opts:
    print("\n** ERROR: must specify output text file (opt: -o)! **", file=sys.stderr)
    printHelp()

################################################################
# Read dictionary

word_set = set()

with open(opts['-d'], encoding = "utf8") as words_in:
    for line in words_in:
        word_set.add(line.strip())

################################################################
# Process one sentence

#def segment(sent, wordset):
#    return list(sent)

def segment(sent, wordset):
    words = []
    sentlen = len(sent)
    current = 0
    while current < sentlen:
        maxlen = min(sentlen - current, MAXWORDLEN)
        for i in range(maxlen, 0, -1):
            candidate = sent[current:current + i]
            if i == 1 or candidate in wordset:
                words.append(candidate)
                current += i
                break
    return words

################################################################
# Process input sentences and output results

with open(opts['-i'], encoding = "utf8") as text_in, \
     open(opts['-o'], "w", encoding = "utf8") as text_out:
    for line in text_in:
        words = segment(line.strip(), word_set)
        print(' '.join(words), file = text_out)

################################################################

