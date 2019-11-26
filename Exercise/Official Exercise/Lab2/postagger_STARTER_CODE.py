"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -l FILE : create OR read lexicon file FILE
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt
# Command line options handling, and help
# For the Command Line format:
'''
     > python postagger_STARTER_CODE.py -l ./POSTAG_DATA/training_data.txt -t ./POSTAG_DATA/test_data.txt
'''

class Training:
    summary_dict = {}
    opts = None
    args = None

    def __init__(self):
        self.opts, self.args = getopt.getopt(sys.argv[1:], 'hd:l:t:')
        # This command 'h' doesn't require the parameters and foe the d,l,
        self.opts = dict(self.opts)
        if '-h' in self.opts:
            self.printHelp()
        if len(self.args)>0:
            print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
            self.printHelp()
        if '-l' not in self.opts:
            print("\n** ERROR: must specify lexicon file name (opt: -l) **", file=sys.stderr)
            self.printHelp()
        # read the file which
        self.read_file(self.opts)
        self.process_dict()

    def printHelp(self):
        help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
        print('-' * 60, help, '-' * 60, file=sys.stderr)
        sys.exit()

    def read_file(self,opts):
        with open(opts['-l'],'r')  as train_file:
            for line in train_file:
                summary_list = []
                # Use the Regex to split the vocabulary
                inter_result = line.split()
                for item in inter_result:
                    result = item.split('/')
                    summary_list.append((result[0], result[1]))
                # Judge all the item in summary
                for (pre,behind) in summary_list:
                    if pre not in self.summary_dict:
                        self.summary_dict[pre] = {}
                    if behind in self.summary_dict[pre]:
                        self.summary_dict[pre][behind] += 1
                    else:
                        self.summary_dict[pre] = 1

    def process_dict(self):
        tagCounts = {}
        ambiguousTypes = 0
        ambiguousTokens = 0
        allTypes = len(self.summary_dict)
        allTokens = 0
        correctTokens = 0

        for sid in self.summary_dict:
            values = self.summary_dict[sid].values()
            # So we need to judge there should be solid item in the dictionary
            if len(values) > 1:
                ambiguousTypes += 1
                ambiguousTokens += sum(values)
            correctTokens += max(values)
            allTokens += sum(values)
            for pre, behind in self.summary_dict[sid].items():
                if pre in tagCounts:
                    tagCounts[pre] += behind
                else:
                    tagCounts[pre] = behind
        print('Proportion of word types that are ambiguous: %5.1f%% (%d / %d)' % \
              ((100.0 * ambiguousTypes) / allTypes, ambiguousTypes, allTypes), file=sys.stderr)

        print('Proportion of tokens that are ambiguous in data: %5.1f%% (%d / %d)' % \
              ((100.0 * ambiguousTokens) / allTokens, ambiguousTokens, allTokens), file=sys.stderr)

        print('Accuracy of naive tagger on training data: %5.1f%% (%d / %d)' % \
              ((100.0 * correctTokens) / allTokens, correctTokens, allTokens), file=sys.stderr)

        tags = sorted(tagCounts, key=lambda x: tagCounts[x], reverse=True)

        print('Top Ten Tags by count:', file=sys.stderr)
        for tag in tags[:10]:
            count = tagCounts[tag]
            print('   %9s %6.2f%% (%5d / %d)' % \
                  (tag, (100.0 * count) / allTokens, count, allTokens), file=sys.stderr)


class Test:
    digitRE = re.compile('\d')
    jj_ends_RE = re.compile('(ed|us|ic|ble|ive|ary|ful|ical|less)$')

    def __init__(self, result_dict, opts):
        maxtag = {}
        for wd in result_dict:
            tags = sorted(result_dict[wd], key=lambda x: result_dict[wd][x], reverse=True)
            maxtag[wd] = tags[0]
        print('<tagging test data ....>', file=sys.stderr)
        # Tag each word of test data, and score
        test = open(opts['-t'], 'r')
        alltest = 0
        correct = 0
        for line in test:
            for wd, truetag in self.split_text(line):
                if wd in maxtag:
                    newtag = maxtag[wd]
                else:
                    newtag = self.tagUnknown(wd)
                alltest += 1
                if newtag == truetag:
                    correct += 1

        print('<done>', file=sys.stderr)

        print("Score on test data: %5.1f%% (%5d / %5d)" % \
              ((100.0 * correct) / alltest, correct, alltest), file=sys.stderr)

    def tagUnknown(self,wd):
        #    return 'UNK'
        #    return 'NN'
        #    return 'NNP'
        if wd[0:1].isupper():
            return 'NNP'
        if '-' in wd:
            return 'JJ'
        if self.digitRE.search(wd):
            return 'CD'
        if self.jj_ends_RE.search(wd):
            return 'JJ'
        if wd.endswith('s'):
            return 'NNS'
        if wd.endswith('ly'):
            return 'RB'
        if wd.endswith('ing'):
            return 'VBG'

    def split_text(self,line):
        wdtags = line.split()
        wdtagpairs = []
        for wdtag in wdtags:
            parts = wdtag.split('/')
            wdtagpairs.append((parts[0], parts[1]))
        return wdtagpairs


if __name__ == '__main__':
    config = Training()
    final = Test(config.summary_dict,config.opts)











