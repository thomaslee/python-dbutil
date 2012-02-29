# python-dbutil

A very thin wrapper around Python's DB API 2.0 standard.

## Status

Alpha

## Overview

Just a couple of little wrappers & helper methods for manipulating databases
with Python.

## Prerequisites

* Python 2.6+
* A DB API 2.0 compatible database driver

## Installation

    pip install dbutil

## Usage

### connect() ... close()

    import dbutil

    conn = dbutil.connect("mysql://root@localhost/foo_db")
    # ... do stuff ...
    conn.close()

### Context Manager

    import dbutil

    with dbutil.connect(...) as conn:
        # ... do stuff ...
        
### Get a single value

    num_users = conn.one("SELECT COUNT(*) FROM users")
    print num_users

### Get the first row from a result set

    user = conn.row("SELECT * FROM users WHERE id=%s", (1,))
    print user

### Get all rows from a result set

    users = conn.all("SELECT * FROM users")
    print users

### Efficiently iterate over a result set

    for user in conn.iter("SELECT * FROM users"):
        print user

### Efficiently apply a function to each row returned by a query

    def print_user(user):
        print user
    conn.each(print_user, "SELECT * FROM users")

### Efficiently apply a map function to each row returned by a query

    emails = conn.map(lambda row: row["email"], "SELECT * FROM users")

    conn.execute("INSERT INTO users VALUES (%s, %s, SHA(%s))", (1, 'me@foo.com', 'password'))

### Fall-through to Python DB API 2.0

    # standard DB API stuff works too
    crs = conn.cursor()
    # ...

## License

This software is licensed under the terms of the [MIT License](http://github.com/thomaslee/python-dbutil/blob/master/LICENSE).

## Support

Please log defects and feature requests using the issue tracker on [github](http://github.com/thomaslee/python-dbutil).

## About

python-dbutil was written by [Tom Lee](http://tomlee.co).

Follow me on [Twitter](http://www.twitter.com/tglee) or
[LinkedIn](http://au.linkedin.com/pub/thomas-lee/2/386/629).

