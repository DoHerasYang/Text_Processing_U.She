
class Retrieve:
    # Create new Retrieve object storing index and termWeighting scheme
    def __init__(self,index, termWeighting):
        self.index = index
        self.termWeighting = termWeighting

    # Method performing retrieval for specified query
    def forQuery(self, query):
        return range(1,11)

