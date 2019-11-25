# TODO: Finish the Assignment Part
import math
import operator
class Retrieve:
    # Define all the usable class variables
    index = None
    termWeighting = None
    doc_len = dict()  # The dictionary to record all the documents' length
    # tr_candidate = dict()  # Retrieval all the documents 
    # tr_candidate_all = dict() # for every doc_id and count
    # tr_candidate_id = list()  # Retrial all the documents ID and store for use binary model candidate
    # tr_query_count = list()  # To store the query count/frequency

    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self, index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting
        # get the length of the each documents and
        self.doc_length()

    # Firstly we should calculate the documents length by number of arisen vocabularly
    def doc_length(self):
        # Extract all the items from the index file and sum the arisen number
        tempor_list = self.index.items()
        for term,combination in tempor_list:
            for doc_id,show_count in combination.items():
                if doc_id in self.doc_len:
                    self.doc_len[doc_id] = self.doc_len[doc_id] + show_count**2
                else:
                    self.doc_len[doc_id] = show_count**2

    # Method performing retrieval for specified query
    def forQuery(self, query):
        # Compare the index and query
        tr_candidate, tr_candidate_all, tr_candidate_id = self.getCandidate(query) 
        output = None
        # Firstly we should judge the function the program operate
        if self.termWeighting == 'binary':
            output =  self.binary_model(tr_candidate_id, query)
        elif self.termWeighting == 'tf':
            output =  self.tf_model(tr_candidate_id, tr_candidate_all, query)
        elif self.termWeighting == 'tfidf':
            output =  self.tfidf_model(tr_candidate, query)
        del tr_candidate, tr_candidate_all, tr_candidate_id
        return output      
        
    # Extract the query from the file and also generate a new corresponding dictionary
    # We delete all the irreverent values and integrate the dictionary into a list(Count all the count)
    def getCandidate(self, query):
        # Get the two list to store the term of query and number of key vocabularly
        queryIterm, qtermCount = zip(*query.items())
        get_candidate = {}
        get_candidate_all = {}
        get_candidate_id = []
        for each_iterm in set(queryIterm):            
            if each_iterm in self.index:   # If the target document includes the query key we should put the id into a document
                temp = self.index[each_iterm] # get all the document data formate: doc_id:count
                get_candidate[each_iterm] = temp
                for doc_id,count in self.index[each_iterm].items():
                    if doc_id in get_candidate_all:
                        get_candidate_all[doc_id][each_iterm] = count
                    else:
                        get_candidate_all[doc_id] = {}
                    get_candidate_id.append(doc_id)
        return get_candidate,get_candidate_all,get_candidate_id
                
    def binary_model(self, list_candidate_id , query):
        Results = dict()
        score = 0
        id_dictionary = {}
        # For binary we just care about the occurance in query and doc or not, every occurance we regard as the same weight
        # So we just care about the occurance of index(doc) and treat every occurance as once
        for id in list_candidate_id:
            if id in id_dictionary:
                id_dictionary[id] += 1
            else:
                id_dictionary[id] = 1
        
        for doc_id, count in id_dictionary.items():
            # Count is all the value for the molecule of formula(sum)
            score = count/math.sqrt(self.doc_len[doc_id])
            Results[doc_id] = score
        topscore = [doc_id for doc_id,value in sorted(Results.items(), key = lambda x:x[1], reverse=True)]
        return topscore
            
     
    def tf_model(self, list_candidate_id, all_candidate, query):
        Results = dict()
        # Calculate all the value from the self.tr_documentid and convert it into the set to improve the efficiency
        # We have built the tr_candidate_id to store all the show index file and number is the occurance of query     
        # We need to calculate the number of occurance of index in set of query
        set_candidate = set(list_candidate_id)
        score = 0        
        for doc_id in set_candidate:
            for each_term,each_value in (query.items()):
                if each_term in all_candidate[doc_id]:
                    score = score + all_candidate[doc_id][each_term] * each_value
                else:
                    continue
            result = score / math.sqrt(self.doc_len[doc_id])
            Results[doc_id] = result
            score = 0
        # return value is a list value
        topscore = [doc_id for doc_id,value in sorted(Results.items(), key = operator.itemgetter(1), reverse = True)]
        return topscore
    
    
    def tfidf_model(self, trcandidate, query):
        # First we need to calculate value of Inverse document frequency(IDF) value
        IDFValue = {}
        for term,collection in self.index.items():
            IDFValue[term] = math.log(len(self.doc_len)/len(collection))
        
        # Next we should create two new data-structure(dic()) to store the IDF and score
        # For the IDF value for each doc_id
        Results = dict()
        doc_idf = dict()
        for term,qterm_frequency in query.items():
            if term in trcandidate:
                for doc_id, count in trcandidate[term].items():
                    frequency = qterm_frequency * count
                    if doc_id in doc_idf:
                        doc_idf[doc_id] += frequency * IDFValue[term]
                    else:
                        doc_idf[doc_id]  = frequency * IDFValue[term]
        for doc_id,value in doc_idf.items():
            Results[doc_id] = value/math.sqrt(self.doc_len[doc_id])       
        topscore = [doc_id for doc_id,value in sorted(Results.items(), key = operator.itemgetter(1), reverse = True)]
        return topscore            