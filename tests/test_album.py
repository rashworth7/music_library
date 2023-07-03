from lib.album import Album

"""
Test input for one album
"""
def test_input_for_one_album():
    album = Album("title", 2023, 1)
    assert album.title == "title"
    assert album.release_year == 2023
    assert album.artist_id == 1
