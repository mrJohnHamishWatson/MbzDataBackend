from typing import Union

from data.song import SongModel
from db.postgres_client import PostgresClient


class Postgres:
    def __init__(self):
        self.client = PostgresClient()

    def find_song(self, prompt: str) -> Union[SongModel, bool]:
        """
        Find song by name. If song doesn't exist = return false
        :param prompt:
        :return:
        """
        sql_select = (
            "select artist_name, album_title, song_title "
            "from artist "
            "inner join albums on artist.artist_id = albums.id "
            "inner join songs on songs.album_id = albums.album_id "
            #f"where #artist_name LIKE '%{prompt}%' "
           # f"or album_name LIKE '%{prompt}%' "
            f"where song_title LIKE '%{prompt}%'"
            f"LIMIT 1;"
        )

        self.client.cursor.execute(sql_select)
        try:
            result_value = self.client.cursor.fetchall()[0]
            return SongModel(song_name=result_value[2],
                         artist=result_value[0],
                         album=result_value[1])
        except IndexError as err:  # if song dont exist
            return False
