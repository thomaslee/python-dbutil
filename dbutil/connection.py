from .row import row

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

    def one(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            if crs.rowcount == 0:
                return None
            else:
                return crs.fetchone()[0]

    def row(self, query, params=None):
        if params is None:
            params = tuple()
        with self.impl as crs:
            crs.execute(query, params)
            if crs.rowcount == 0:
                return None
            else:
                return row(crs.description, crs.fetchone())

    def all(self, query, params=None):
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

