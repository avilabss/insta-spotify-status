import requests


class SpotifyAPI:
    def __init__(self, base_url, email):
        self.base_url = base_url
        self.email = email

    def get_currently_playing(self) -> dict | None:
        """
        Get currently playing track data.

        Returns:
            Currently playing track data if available, else None.
        """

        url = f"{self.base_url}/tracks/playing?email={self.email}"
        response = requests.get(url)
        if response.status_code == 200 and "application/json" in response.headers.get(
            "content-type", ""
        ):
            return response.json()
        return None
