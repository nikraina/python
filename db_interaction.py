__author__ = 'nikhil'

import sqlite3

def Main():
    try:
        con = sqlite3.connect("test_python.db")
        cur = con.cursor()
        cur.execute("SELECT SQLITE_VERSION()")

        data = cur.fetchone()

        print "The current DB version is :: " + str(data)
    except sqlite3.Error, e:
        if con:
            con.rollback()
    finally:
        if con:
            con.close()

if __name__ == "__main__":
    Main()
