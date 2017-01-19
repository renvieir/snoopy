import pyodbc
from decouple import config

class SnoopyDAO:
    def __init__(self):
        self.connection_string = 'DRIVER={Sql Server};'+ \
                                 'SERVER=localhost;'+ \
                                 'DATABASE=snoopy;'+ \
                                 'UID={};PWD={};'.format(config('UID'),config('PWD'))

        self.connection = pyodbc.connect(self.connection_string)
        self.cursor = self.connection.cursor()
        self.queries = {
            'species':'SELECT speciesid, species, common FROM dbo.species',
            'specie':'SELECT speciesid, species, common FROM dbo.species WHERE speciesid={}',
            'specie_urls': 'SELECT speciesid, url FROM dbo.media WHERE speciesid = {}'
        }

    def get_species(self):
        return self.execute_query(self.queries['species'])

    def get_specie(self, specieid):
        query = self.queries['specie'].format(specieid)
        return self.execute_query(query)

    def get_specie_url_images(self, specieid):
        query = self.queries['specie_urls'].format(specieid)
        return self.execute_query(query)

    def execute_query(self, query):
        result = []
        self.cursor.execute(query)
        for row in self.cursor.fetchall():
            result.append(row)
            print row
        return result


if __name__ == "__main__":
    sndao = SnoopyDAO()
    sndao.get_species()
    sndao.get_specie(9)
    sndao.get_specie_url_images(9)
