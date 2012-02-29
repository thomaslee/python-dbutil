from urlparse import urlparse
from .connection import connection

version = (0, 4, 0)

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

