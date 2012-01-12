from urlparse import urlparse
from pprint import saferepr

version = (0, 2, 0)

class row(object):
    def __init__(self, desc, data):
        object.__init__(self)
        self.__data = dict(zip([x[0] for x in desc], data))

    def __getitem__(self, key):
        return self.__data[key]

    def __getattr__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            raise AttributeError

    def __repr__(self):
        return "row(%s)" % saferepr(self.__data)

class connection(object):
    def __init__(self, impl):
        object.__init__(self)
        self.impl = impl

    def __getattr__(self, key):
        return getattr(self.impl, key)

    def getone(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            if crs.rowcount == 0:
                return None
            else:
                return crs.fetchone()[0]

    def getrow(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            if crs.rowcount == 0:
                return None
            else:
                return row(crs.description, crs.fetchone())

    def getall(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            result = []
            for rec in crs:
                result.append(row(crs.description, rec))
            return result

    def execute(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)

    def each(self, cb, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            for rec in crs:
                cb(row(crs.description, rec))

    def map(self, cb, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            result = []
            for rec in crs:
                result.append(cb(row(crs.description, rec)))
            return result

def _connect_mysql(url):
    import MySQLdb as db
    params = {}
    if url.username:
        params["user"] = url.username
    else:
        params["user"] = "root"
    if url.password:
        params["passwd"] = url.password
    if url.hostname:
        params["host"] = url.hostname
    if url.port:
        params["port"] = url.port
    if url.path:
        params["db"] = url.path[1:]
    return connection(db.connect(**params))

DEFAULT_LOOKUP = {
    "mysql": _connect_mysql
}

def connect(url, lookup=None):
    url = urlparse(url)
    if lookup is None:
        lookup = DEFAULT_LOOKUP
    return lookup[url.scheme](url)

