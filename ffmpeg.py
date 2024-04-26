import os

class Ffmpeg:
    """
    Класс для распознования аудио через Vosk и преобразования его в текст.
    Поддерживаются форматы аудио: wav, ogg
    """
    default_init = {
        "ffmpeg_path": "ffmpeg"  # путь к ffmpeg
    }

    def __init__(self,
                 ffmpeg_path=None
                 ) -> None:
        """
        Настройка ffmpeg_path.

        :arg ffmpeg_path: str  путь к ffmpeg
        """
        self.ffmpeg_path = ffmpeg_path if ffmpeg_path else Ffmpeg.default_init["ffmpeg_path"]
        self._check_model()

    def _check_model(self):
        """
        Проверка наличия кодировщика ffmpeg.exe
        """

        isffmpeg_here = False
        for file in os.listdir(self.ffmpeg_path):
            if file.startswith('ffmpeg'):
                isffmpeg_here = True

        if not isffmpeg_here:
            raise Exception(
                "Ffmpeg: сохраните ffmpeg.exe в папку ffmpeg\n"
                "Скачайте ffmpeg.exe по ссылке https://ffmpeg.org/download.html"
                            )
        self.ffmpeg_path = self.ffmpeg_path + '/ffmpeg'

