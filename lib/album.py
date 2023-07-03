
class Album:

    def __init__(self, title, release_year, artist_id):
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Album
    def __repr__(self):
        return f"Album({self.title}, {self.release_year}, {self.artist_id})"
