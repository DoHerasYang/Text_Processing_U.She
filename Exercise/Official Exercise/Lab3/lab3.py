"""
USE: python <PROGNAME> (options) datafile1 ... datafileN
OPTIONS:
    -h : print this help message and exit
"""
################################################################

import sys, re, getopt
import matplotlib.pylab as p
import numpy as np

##### We can get the filename and information of command line
opts, args = getopt.getopt(sys.argv[1:], 'h')
opts = dict(opts)
filenames = args

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help, '-' * 60, file = sys.stderr)
    sys.exit()

class Textprocessing:

    sotre_dict = {}
    seq_wordlist = None
    seq_wordcount = None

    def __init__(self):
        self.open_file()
        self.sort_vocabulary()
        self.plot_picture()
        self.plot_cumulative()
        self.plot_log()

    def open_file(self):
        with open(filenames[0],'r') as text:
            for line in text:
                for item in re.findall(r"\w+",line.lower()):
                    if item in self.sotre_dict:
                        self.sotre_dict[item] += 1
                    else:
                        self.sotre_dict[item] = 1
    # Now we should select the top frequency of vocabulary
    def sort_vocabulary(self):
        self.seq_wordlist = sorted(
            self.sotre_dict,
            key=lambda item: self.sotre_dict[item],
            reverse=True
        )
        # Now we get the number of items in the dictionary
        self.seq_wordcount = [self.sotre_dict[w] for w in self.seq_wordlist]
        topN = 20
        for single in self.seq_wordlist[:topN]:
            print(single,':',self.sotre_dict[single])

    def plot_picture(self):
        # now we should plot the picture
        x_axle = np.arange(1,len(self.seq_wordcount)+1,1)
        p.figure()
        p.plot(x_axle, self.seq_wordcount)
        p.minorticks_on()
        p.title("Rank Vs frequency")
        p.savefig('./pic1.png')

    def plot_cumulative(self):
        cumulative = list(self.seq_wordcount)
        for i in range(len(cumulative) - 1):
            cumulative[i + 1] += cumulative[i]
        x_axle = np.arange(1,len(self.seq_wordcount)+1,1)
        p.figure()
        p.plot(x_axle, cumulative)
        p.title('cumulative freq vs rank')
        p.savefig('./pic2.png')

    def plot_log(self):
        x_axle = np.arange(1, len(self.seq_wordcount) + 1, 1)
        logcount = [p.log(y) for y in self.seq_wordcount]
        logx_axle = [p.log(x) for x in x_axle]
        p.figure()
        p.plot(logx_axle,logcount)
        p.title("logcount Vs logrange")
        p.savefig('./pic3.png')



if __name__ == '__main__':
    test = Textprocessing()