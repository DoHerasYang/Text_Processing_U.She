"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt

################################################################
# Command line options handling, and help

opts, args = getopt.getopt(sys.argv[1:], 'hd:t:')
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
    print("\n** ERROR: must specify training data file (opt: -d FILE) **", file=sys.stderr)
    printHelp()

################################################################

# Function to split up a line of "Brill format" data into a list
# of word/tag pairs. 

def parseLine(line):
    wdtags = line.split()
    wdtagpairs = []
    for wdtag in wdtags:
        parts = wdtag.split('/')
        wdtagpairs.append((parts[0], parts[1]))
    return wdtagpairs

####################

wordTagCounts = {}
    # This is main data structure of lexicon - a two-level
    # dictionary, mapping {words->{tags->counts}}

print('<reading data for new lexicon ....>', file=sys.stderr)
with open(opts['-d']) as data_in:
    for line in data_in:
        for (wd, tag) in parseLine(line):
            if wd not in wordTagCounts:
                wordTagCounts[wd] = {}
            if tag in wordTagCounts[wd]:
                wordTagCounts[wd][tag] += 1
            else:
                wordTagCounts[wd][tag] = 1
print('<done>', file=sys.stderr)

################################################
# ANALYSE word-tag-count dictionary, to compute:
# -- proportion of types that have more than one tag
# -- accuracy naive tagger would have on the training data
# -- most common tags globally

tagCounts = {}
ambiguousTypes = 0
ambiguousTokens = 0
allTypes = len(wordTagCounts)
allTokens = 0
correctTokens = 0

for wd in wordTagCounts:
    values = wordTagCounts[wd].values()
    if len(values) > 1:
        ambiguousTypes += 1
        ambiguousTokens += sum(values)
    correctTokens += max(values)
    allTokens += sum(values)
    for t, c in wordTagCounts[wd].items():
        if t in tagCounts:
            tagCounts[t] += c
        else:
            tagCounts[t] = c

print('Proportion of word types that are ambiguous: %5.1f%% (%d / %d)' % \
        ((100.0 * ambiguousTypes) / allTypes, ambiguousTypes, allTypes), file=sys.stderr)

print('Proportion of tokens that are ambiguous in data: %5.1f%% (%d / %d)' % \
        ((100.0 * ambiguousTokens) / allTokens, ambiguousTokens, allTokens), file=sys.stderr)

print('Accuracy of naive tagger on training data: %5.1f%% (%d / %d)' % \
        ((100.0 * correctTokens) / allTokens, correctTokens, allTokens), file=sys.stderr)

tags = sorted(tagCounts, key=lambda x:tagCounts[x], reverse=True)

print('Top Ten Tags by count:', file=sys.stderr)
for tag in tags[:10]:
    count = tagCounts[tag]
    print('   %9s %6.2f%% (%5d / %d)' % \
          (tag, (100.0 * count) / allTokens, count, allTokens), file=sys.stderr)

################################################
# Function to 'guess' tag for unknown words

digitRE = re.compile('\d')
jj_ends_RE = re.compile('(ed|us|ic|ble|ive|ary|ful|ical|less)$')
        
# NOTE: if you uncomment the 'return' at the start of the following 
# definition, the score achieved will be that where all unknown words 
# are tagged *incorrectly* (as UNK). Uncommenting instead the third 
# 'return', will yield the score where the default tag for unknown
# words is NNP. Otherwise, the definition attempts to guess the 
# correct tags for unknown words based on their suffix or other 
# characteristics. 

def tagUnknown(wd):
#    return 'UNK'
#    return 'NN'
#    return 'NNP'
    if wd[0:1].isupper():
        return 'NNP'
    if '-' in wd:
        return 'JJ'
    if digitRE.search(wd):
        return 'CD'
    if jj_ends_RE.search(wd):
        return 'JJ'
    if wd.endswith('s'):
        return 'NNS'
    if wd.endswith('ly'):
        return 'RB'
    if wd.endswith('ing'):
        return 'VBG'

################################################
# Apply naive tagging method to test data, and score performance

if '-t' in opts:
    
    # Compute 'most common' tag for each known word - store in maxtag dictionary
    maxtag = {}
    for wd in wordTagCounts:
        tags = sorted(wordTagCounts[wd], key=lambda x:wordTagCounts[wd][x], reverse=True)
        maxtag[wd] = tags[0]

    print('<tagging test data ....>', file=sys.stderr)

    # Tag each word of test data, and score
    test = open(opts['-t'], 'r')
    alltest = 0
    correct = 0
    for line in test:
        for wd, truetag in parseLine(line):
            if wd in maxtag:
                newtag = maxtag[wd]
            else:
                newtag = tagUnknown(wd)
            alltest += 1
            if newtag == truetag:
                correct += 1

    print('<done>', file=sys.stderr)
            
    print("Score on test data: %5.1f%% (%5d / %5d)" % \
          ((100.0*correct)/alltest, correct, alltest), file=sys.stderr)
    
################################################

