"""\
------------------------------------------------------------
USE: python <PROGNAME> (options) file1...fileN
OPTIONS:
    -h : print this help message
    -b : use BINARY weights (default: count weighting)
    -s FILE : use stoplist file FILE
    -I PATT : identify input files using pattern PATT, 
              (otherwise uses files listed on command line)
------------------------------------------------------------
"""
# Read the file and select the different
import sys, re, getopt, glob
opts, args = getopt.getopt(sys.argv[1:], 'hs:bI:')
opts = dict(opts)
filenames = args
##############################
# HELP option
if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print(help, file=sys.stderr)
    sys.exit()
##############################
# Identify input files, when "-I" option used
# TODO：Finish the TEST file and go to calculate the each worlds' counts which are seperated from the STOP_LIST
if '-I' in opts:
    filenames = glob.glob(opts['-I'])

# STOPLIST Section
# The set for the all vocabulary
stops = set()
if '-s' in opts:
    with open(opts['-s'], 'r') as stop_fs:
        for line in stop_fs :
            stops.add(line.strip())

def main_function(num):
    dataset = {}
    all_character= set()
    input_value = list()
    with open(filenames[num], 'r') as test_file:
        for line in test_file:
            if line == '\n' or line == '\r': # if the line is a single character the next function will not work
                continue
            # use the regex to delete the not necessary character
            line = line.replace("\n", ' ').replace("\r", ' ').strip()
            line = re.sub(r"[,]|[.]|[:]|[-]|[0-9]{1,4}|[(|)]", '', str.lower(line))
            result = re.findall(r"\w+(?:\'s)?(?:\'t)?(?:\'ve)?", line)
            for character in result:
                if character not in stops:
                    all_character.add(character)
                    if character in dataset:
                        dataset[character] += 1
                    else:
                        dataset[character] = 1
    return dataset, all_character

dataset_0 = {}
dataset_1 = {}
result_set0 = set()
result_set1 = set()
for i in range(len(filenames)):
    globals()["dataset_" + str(i)], globals()["result_set"+str(i)] = main_function(i)
# Now we should calculate the Jaccard Coefficient(NOT INCLUDE THE )
in_set = result_set0 & result_set1
union_set = result_set0 | result_set1
print("For the count of set:",filenames[0], "<>", filenames[1],'=', (len(in_set)/len(union_set)))

# Now we should get the value for each w in union of result_set0 and result_set1
count_top = 0
count_below = 0
# Because there is some missing value for each data so we should build a function
def getvalue(dst,key):
    if key in dst:
        return dst[key]
    else:
        return 0

for w in (result_set0|result_set1):
    count_top += min(getvalue(dataset_0,w),getvalue(dataset_1,w))
    count_below += max(getvalue(dataset_0,w),getvalue(dataset_1,w))
print("For the value of set:",filenames[0], "<>", filenames[1],'=', (count_top/count_below))




