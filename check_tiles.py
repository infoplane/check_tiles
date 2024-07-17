import psycopg
from psycopg import sql
from psycopg.pq import Escaping

class CheckPolys:
    def __init__(self, databasename, user,host, password):
        self.connect_str = "dbname='" + databasename +  "' user='" + user +  "' host='" + host + "' password='" + password +  "'"

    def get_schema_tables(self):

        table_name_list = []

        query = sql.SQL('SELECT table_name FROM tiles_present')



        try:
            self.conn = psycopg.connect(self.connect_str)
            self.conn.execute("SET SEARCH_PATH to marxan")
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.conn.commit
            self.cursor.close()
            self.conn.close()


        except Exception as e:
            print("Can't connect")
            print(e)


        for row in results:
            table_name_list.append(row[0])

        return table_name_list




    def get_tile_list(self):

        table_name_list = []

        query = sql.SQL('SELECT table_name FROM habitat_poly_names')



        try:
            self.conn = psycopg.connect(self.connect_str)
            self.conn.execute("SET SEARCH_PATH to marxan")
            self.cursor = self.conn.cursor()
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            self.conn.commit
            self.cursor.close()
            self.conn.close()

            #print(full_query)

        except Exception as e:
            print("Can't connect")
            print(e)


        for row in results:
            table_name_list.append(row[0])

        return table_name_list







def main():

    checkpolys = CheckPolys('lnrs', 'postgres', 'localhost', 'outrider77')
    result1 = checkpolys.get_schema_tables()
    result2 = checkpolys.get_tile_list()


    print("==============================>")
    print(result1)
    print("==============================>")
    print(result2)
    print("==============================>")

    difference = []
    for element in result2:
        if element not in result1:
            difference.append(element)


    print(difference)

if __name__ == '__main__':
    main()

