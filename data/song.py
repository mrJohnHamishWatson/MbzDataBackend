from dataclasses import dataclass


@dataclass(frozen=True)
class SongModel:
    song_name: str
    artist: str
    album: str

    def to_json(self):
        return {
            "song_name": self.song_name,
            "artist": self.artist,
            "album": self.album,
        }
