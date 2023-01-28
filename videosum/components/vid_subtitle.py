import os
import sys

import ffmpeg

from videosum.exception import CustomException
from videosum.logger import logger

# It takes a dictionary of video paths and srt paths, and adds the subtitles to the videos


class VideoSubtitler:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def add_subtitles(self, path: str, subtitles_path: str):
        """
        It takes a video file and a subtitle file, and outputs a video file with the subtitles embedded

        Args:
          path (str): The path to the video file.
          subtitles_path (str): The path to the subtitles file.
        """
        try:
            filename = os.path.basename(path).split('.')[0]
            out_path = os.path.join(self.output_dir, f"{filename}.mp4")

            logger.info(f"Adding subtitles to {os.path.basename(path)}...")

            video = ffmpeg.input(path)
            audio = video.audio

            ffmpeg.concat(
                video.filter('subtitles', subtitles_path, force_style="OutlineColour=&H40000000,BorderStyle=3"), audio, v=1, a=1
            ).output(out_path).run(quiet=True, overwrite_output=True)

            logger.info(
                f"Saved subtitled video to {os.path.abspath(out_path)}.")
        except Exception as e:
            raise CustomException(e, sys)

    def process_videos(self, subtitles: dict):
        """
        It takes a dictionary of video paths and srt paths, and adds the subtitles to the videos

        Args:
          subtitles (dict): dict
        """
        try:
            for path, srt_path in subtitles.items():
                self.add_subtitles(path, srt_path)
        except Exception as e:
            raise CustomException(e, sys)
