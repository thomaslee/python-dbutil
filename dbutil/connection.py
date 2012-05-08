from .row import row

class cursor(object):
    def __init__(self, impl):
        object.__init__(self)
        self.impl = impl

    def __getattr__(self, key):
        return getattr(self.impl, key)
    
    def one(self, query, params):
        if params is None:
            params = tuple()
        self.impl.execute(query, params)
        if self.impl.rowcount == 0:
            return None
        return self.impl.fetchone()[0]

    def row(self, query, params):
        if params is None:
            params = tuple()
        self.impl.execute(query, params)
        if self.impl.rowcount == 0:
            return None
        return row(self.impl.description, self.impl.fetchone())
    
    def all(self, query, params):
        if params is None:
            params = tuple()
        self.impl.execute(query, params)
        result = []
        for r in self.impl:
            result.append(row(self.impl.description, r))
        return result

class connection(object):
    def __init__(self, impl):
        object.__init__(self)
        self.impl = impl

    def __getattr__(self, key):
        return getattr(self.impl, key)

    def __enter__(self, *args):
        return self

    def __exit__(self, *args):
        self.impl.close()

    def cursor(self):
        return cursor(self.impl.cursor())

    def one(self, query, params=None):
        with self.impl as crs:
            return cursor(crs).one(query, params)

    def row(self, query, params=None):
        with self.impl as crs:
            return cursor(crs).row(query, params)

    def all(self, query, params=None):
        with self.impl as crs:
            return cursor(crs).all(query, params)

    def execute(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)

    def iter(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            for rec in crs:
                yield row(crs.description, rec)

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

