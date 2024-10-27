from typing import Any


def get_value(data, path, default=None) -> Any:
    """
    Get value from nested dictionary using dot notation.

    Parameters:
        data: Nested dictionary.
        path: Dot separated path to the value.
        default: Default value if key is not found.

    Returns:
        Value from the nested dictionary.
    """

    keys = path.split(".")
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key, default)
        else:
            return default
    return data


def parse_song_data(song_data: dict) -> dict:
    song_name = get_value(song_data, "item.name")
    artists = get_value(song_data, "item.artists")
    artist_name = artists[0]["name"] if artists else "Unknown Artist"
    explicit = get_value(song_data, "item.explicit")
    progress_ms = get_value(song_data, "progress_ms")
    total_ms = get_value(song_data, "item.duration_ms")

    return {
        "song_name": song_name,
        "artist_name": artist_name,
        "explicit": explicit,
        "progress_ms": progress_ms,
        "total_ms": total_ms,
    }
