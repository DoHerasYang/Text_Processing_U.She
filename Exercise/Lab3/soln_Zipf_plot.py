"""
USE: python <PROGNAME> (options) datafile1 ... datafileN
OPTIONS:
    -h : print this help message and exit
"""
################################################################

import sys, re, getopt
import pylab as p

opts, args = getopt.getopt(sys.argv[1:], 'h')
opts = dict(opts)
filenames = args

if '-h' in opts:
    progname = sys.argv[0]
    progname = progname.split('/')[-1] # strip out extended path
    help = __doc__.replace('<PROGNAME>', progname, 1)
    print('-' * 60, help, '-' * 60, file = sys.stderr)
    sys.exit()

################################################################
# Count words in data file(s)

wordRE = re.compile('\w+')
wdcounts = {}

for filename in filenames:
    with open(filename) as infs:
        for line in infs:
            for wd in wordRE.findall(line.lower()):
                if wd not in wdcounts:
                    wdcounts[wd] = 0
                wdcounts[wd] += 1

################################################################
# Sort words / print top N

words = sorted(wdcounts, reverse = True, key = lambda v:wdcounts[v])
# words = words[:2000] # Truncate (freq sorted) word list
freqs = [wdcounts[w] for w in words]

print()
print('TYPES: ', len(words))
print('TOKENS:', sum(freqs))
print()

topN = 20
for wd in words[:topN]:
    print(wd, ':', wdcounts[wd])

################################################################
# Plot freq vs. rank

ranks = range(1, len(freqs)+1)

p.figure()
p.plot(ranks, freqs)
p.title('freq vs rank')

################################################################
# Plot cumulative freq vs. rank

cumulative = list(freqs) # makes copy of freqs list

for i in range(len(cumulative) - 1):
    cumulative[i + 1] += cumulative[i]

p.figure()
p.plot(ranks, cumulative)
p.title('cumulative freq vs rank')

################################################################
# Plot log-freq vs. log-rank

logfreqs = [p.log(freq) for freq in freqs]
logranks = [p.log(rank) for rank in ranks]

p.figure()
p.plot(logranks, logfreqs)
p.title('log-freq vs log-rank')
p.savefig('log1.png')

################################################################
# Display figures

p.show()

################################################################
