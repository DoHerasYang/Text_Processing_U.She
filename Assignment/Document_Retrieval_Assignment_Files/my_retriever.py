'''
 As we know, we should use the binary,
'''
class Retrieve:
    # Define all the usable class variables
    index = None
    termWeighting = None
    IDF_value = dict()  # IDF values for each documents
    doc_len = dict()  # The dictionary to record all the documents' length
    tr_document = dict()  # Retrieval all the documents and the
    tr_document_id = list()  # Retrial all the documents ID and store for use binary model
    tr_query_count = list()  # To store the query count

    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        # get the length of the each documents and
        self.doc_length()

    # Firstly we should calculate the documents length
    def doc_length(self):
        # Extract all the items from the index
        tempor_list = self.index.items()
        for term,combination in tempor_list:
            for doc_id,show_count in combination:
                if doc_id in self.doc_len:
                    self.doc_len[doc_id] = self.doc_len[doc_id] + show_count
                else:
                    self.doc_len[doc_id] = show_count

    # Method performing retrieval for specified query
    def forQuery(self, query):
        # Firstly we should judge the function the program operaate
        if self.termWeighting is 'binary':
            self.binary_model(query,self.tr_document_id)
        # elif self.termWeighting is 'tfidf':

    # Extract the query from the file and also generate a new corresponding dictionary
    # We delete all the irreverent values and integrate the dictionary into a list(Count all the count)
    def getCandidate(self,index,query):
        queryIterm, qtermCount = zip(*query.items())   # Get the two list to store the term of query and number of key vocabularly
        for each_iterm in set(queryIterm):
            if each_iterm in index:   # If the target document includes the key vocabulary
                self.tr_document[each_iterm] = index[each_iterm]
                doc_id,count = zip(*index[each_iterm].iterms())
                self.tr_document_id.extend(doc_id)
        self.tr_query_count.extend(qtermCount)

    def binary_model(self,query,documentid):
        file_len = self.doc_len
        Scores = dict()
        sum_top = 0
        sum_bot_left = 0
        sum_bot_right = 0
        # Calculate all the value from the self.tr_documentid and convert it into the set to improve the efficiency
        

















