__author__ = 'nikhil'

import sqlite3

def Main():
    try:
        con = sqlite3.connect("test_python.db")
        cur = con.cursor()
        # cur.execute("CREATE TABLE Pets(Id INT, Name TEXT, Price INT)")
        # cur.execute("""INSERT INTO Pets VALUES(1,"Dog",400)""")
        # cur.execute("""INSERT INTO Pets VALUES(2,"Cat",200)""")
        # con.commit()

        cur.execute("SELECT * FROM Pets")

        data = cur.fetchall()

        for row in data:
            print row

    except sqlite3.Error, e:
        if con:
            con.rollback()
            print "something wrong happend with sqlite3"
    finally:
        if con:
            con.close()


if __name__ == "__main__":
    Main()
