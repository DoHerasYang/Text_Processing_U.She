import sys, re

#------------------------------
# PART 1: 

   # Key thing is to avoid matching strings that include
   # multiple tags, e.g. treating '<p><b>' as a single
   # tag. Can do this in several ways. Firstly, use
   # non-greedy matching, so get shortest possible match
   # including the two angle brackets:

tag = re.compile('</?(.*?)>') 

   # The above treats the '/' of a close tag as a separate
   # optional component - so that this doesn't turn up as
   # part of the match '.group(1)', which is meant to return
   # the tag label. 
   # Following alternative solution uses a negated character
   # class to explicitly prevent this including '>': 

tag = re.compile('</?([^>]+)>') 

   # Finally, following version separates finding the tag
   # label string from any (optional) parameters that might
   # also appear before the close angle bracket:

tag = re.compile(r'</?(\w+\b)([^>]+)?>') 

   # Note that use of '\b' (as word boundary anchor) here means
   # we must mark the regex string as a 'raw' string (r'..'). 

#------------------------------
# PART 2: 

   # Following closeTag definition requires first first char
   # after the open angle bracket to be '/', while openTag
   # definition excludes this by requiring first char to be
   # a 'word char' (\w):

openTag  = re.compile(r'<(\w[^>]*)>')
closeTag = re.compile(r'</([^>]*)>')

   # Following revised definitions are more carefully stated
   # for correct extraction of tag label (separately from
   # any parameters:

openTag  = re.compile(r'<(\w+\b)([^>]+)?>')
closeTag = re.compile(r'</(\w+\b)\s*>')

#------------------------------
# PART 3: 

   # Above openTag definition will already get the string
   # encompassing any parameters, and return it as
   # m.group(2), i.e. defn: 

openTag  = re.compile(r'<(\w+\b)([^>]+)?>')

   # If assume that parameters are continuous non-whitespace
   # chars separated by whitespace chars, then we can divide
   # them up using split - and that's how we handle them
   # here. (In reality, parameter strings can be a lot more
   # messy than this, but we won't try to deal with that.)

#------------------------------
# PART 4: 

openCloseTagPair = re.compile(r'<(\w+\b)([^>]+)?>(.*?)</\1\s*>')

   # Note use of non-greedy matching for the text falling
   # *between* the open/close tag pair - to avoid false
   # results where have two similar tag pairs on same line.

#------------------------------
# PART 5: URLS

   # This is quite tricky. The URL expressions in the file
   # are of two kinds, of which the first is a string
   # between double quotes ("..") which may include
   # whitespace. For this case we might have a regex: 

url = re.compile('href=("[^">]+")', re.I)

   # The second case does not have quotes, and does not
   # allow whitespace, consisting of a continuous sequence
   # of non-whitespace material (that ends when you reach a
   # space or close bracket '>'). This might be: 

url = re.compile('href=([^">\s]+)', re.I)

   # We can combine these two cases as follows, and still
   # get the expression back as group(1):

url = re.compile(r'href=("[^">]+"|[^">\s]+)', re.I)

   # Note that I've done nothing here to exclude 'mailto:'
   # links as being accepted as URLS. 

#------------------------------

with open('RGX_DATA.html') as infs: 
    linenum = 0
    for line in infs:
        linenum += 1
        if line.strip() == '':
            continue
        print('  ', '-' * 100, '[%d]' % linenum, '\n   TEXT:', line, end='')
    
        # PART 1: find HTML tags
        # (The following uses 'finditer' to find ALL matches
        # within the line)
    
        mm = tag.finditer(line)
        for m in mm:
            print('** TAG:', m.group(1), ' + [%s]' % m.group(2))
    
        # PART 2,3: find open/close tags (+ params of open tags)
    
        mm = openTag.finditer(line)
        for m in mm:
            print('** OPENTAG:', m.group(1))
            if m.group(2):
                for param in m.group(2).split():
                    print('    PARAM:', param)
    
        mm = closeTag.finditer(line)
        for m in mm:
            print('** CLOSETAG:', m.group(1))
    
        # PART 4: find open/close tag pairs appearing on same line
    
        mm = openCloseTagPair.finditer(line)
        for m in mm:
            print("** PAIR [%s]: \"%s\"" % (m.group(1), m.group(3)))
    
        # PART 5: find URLs:
    
        mm = url.finditer(line)
        for m in mm:
            print('** URL:', m.group(1))

        # PART 6: Strip out HTML tags (note that .sub will do all
        # possible substitutions, unless number is limited by count
        # keyword arg - which is fortunately what we want here)

        stripped = tag.sub('', line)
        print('** STRIPPED:', stripped, end = '') 

