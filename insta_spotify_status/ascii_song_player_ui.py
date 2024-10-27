class ASCIISongPlayerUI:
    SONG_PROGRESS_CHAR = "━"
    SONG_REMAINING_CHAR = "─"
    CURSOR_CHAR = "❍"
    SONG_BAR_LEN = 10
    EXPLICIT_CHAR = "𝐄"

    @staticmethod
    def get_progress_bar(progress_ms: int, total_ms: int) -> str:
        """
        Parameters:
            progress_ms: Song progress in ms.
            total_ms: Song duration in ms.

        Returns:
            ASCII progress bar with timestamps.

        Example:
            ```py
            > ASCIISongPlayerUI.get_progress_bar(100413, 142839)
            > 1:40 ━━━━━━━❍─── 2:22
            ```
        """

        progress_bar = ""
        progress_per = (progress_ms / total_ms) * 100

        visible_progress_per = (
            progress_per * (ASCIISongPlayerUI.SONG_BAR_LEN - 1)
        ) / 100
        visible_progress_len = int(visible_progress_per)

        progress_duration_str = "{:.2f}".format(progress_ms / 1000 / 60).replace(
            ".", ":"
        )
        total_duration_str = "{:.2f}".format(total_ms / 1000 / 60).replace(".", ":")

        for i in range(ASCIISongPlayerUI.SONG_BAR_LEN):
            if i < visible_progress_len:
                progress_bar += ASCIISongPlayerUI.SONG_PROGRESS_CHAR

            elif i == visible_progress_len:
                progress_bar += ASCIISongPlayerUI.CURSOR_CHAR

            else:
                progress_bar += ASCIISongPlayerUI.SONG_REMAINING_CHAR

        return f"{progress_duration_str} {progress_bar} {total_duration_str}"

    @staticmethod
    def get_ui(
        song_name: str,
        artist_name: str,
        progress_ms: int,
        total_ms: int,
        explicit: bool = False,
    ) -> str:
        """
        Parameters:
            song_name: Name of the song.
            artist_name: Name of the artist.
            explicit: Explicit content.
            progress_ms: Song progress in ms.
            total_ms: Song duration in ms.

        Returns:
            ASCII UI with song details.

        Example:
            ```py
            > ASCIISongPlayerUI.get_ui("METAMORPHOSIS", "INTERWORLD", True, 100413, 142839)
            > METAMORPHOSIS
              𝙀 INTERWORLD
              1:40 ━━━━━━━❍─── 2:22
            ```
        """

        explicit_str = ASCIISongPlayerUI.EXPLICIT_CHAR + " " if explicit else ""
        progress_bar = ASCIISongPlayerUI.get_progress_bar(progress_ms, total_ms)

        return f"{song_name}\n{explicit_str}{artist_name}\n{progress_bar}"
