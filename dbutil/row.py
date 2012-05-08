from pprint import saferepr

class row(object):
    def __init__(self, desc, data):
        self.__rawdata = data
        self.__data = dict(zip([x[0] for x in desc], data))
        object.__init__(self)

    def __getitem__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            try:
                return self.__rawdata[key]
            except KeyError:
                raise KeyError, key

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __getattr__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            raise AttributeError
        
    def __iter__(self):
        return self.__data.iteritems()

    def __repr__(self):
        return "row(%s)" % saferepr(self.__data)

