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

    import dbutil

    conn = dbutil.connect("mysql://root@localhost/foo_db")

    num_users = conn.getone("SELECT COUNT(*) FROM users")
    print num_users

    user = conn.getrow("SELECT * FROM users WHERE id=%s", (1,))
    print user

    users = conn.getall("SELECT * FROM users")
    print users

    def print_user(user):
        print user
    conn.each(print_user, "SELECT * FROM users")

    emails = conn.map(lambda row: row["email"], "SELECT * FROM users")

    conn.execute("INSERT INTO users VALUES (%s, %s, SHA(%s))", (1, 'me@foo.com', 'password'))

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

