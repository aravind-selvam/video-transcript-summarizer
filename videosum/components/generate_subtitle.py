import os
import sys
import tempfile
import warnings
from dataclasses import dataclass
from pathlib import Path
from typing import List

import ffmpeg
import whisper

from videosum.components.utils import write_srt
from videosum.exception import CustomException
from videosum.logger import logger


@dataclass
class Config:
    output_dir: str = 'srt'
    acodec: str = 'pcm_s16le'
    ar: str = '16k'
    audio_channel: int = 1


# It takes a video path, a model path, and a task (transcribe or translate) and returns a subtitle
class VideoToSubtitle:
    def __init__(self, config: Config):
        try:
            self.output_dir = config.output_dir
            self.ar = config.ar
            self.codec = config.acodec
            self.ac = config.audio_channel
        except Exception as e:
            raise CustomException(e, sys)

    def get_audio(self, video_paths):
        """
        It takes a list of video paths, extracts the audio from each video, and returns a dictionary of
        video paths and their corresponding audio paths
        """
        try:
            temp_dir = tempfile.gettempdir()
            audio_paths = {}
            for path in video_paths:
                filename = os.path.basename(path).split('.')[0]
                logger.info(
                    f"Extracting audio from {os.path.basename(path)}...")
                output_path = os.path.join(temp_dir, f"{filename}.wav")

                ffmpeg.input(path).output(
                    output_path,
                    acodec="pcm_s16le", ac=1, ar="16k"
                ).run(quiet=True, overwrite_output=True)
                audio_paths[path] = output_path
            return audio_paths
        except Exception as e:
            raise CustomException(e, sys)

    def create_subtitles(self, audio_path: Path, srt_path: Path, transcribe: callable):
        """
        It takes an audio file, transcribes it, and writes the transcription to a .srt file
        """
        try:
            logger.info(
                f"Generating subtitles for {os.path.basename(audio_path)}... This might take a while.")

            warnings.filterwarnings("ignore")
            result = transcribe(audio_path)
            warnings.filterwarnings("default")

            with open(srt_path, "w", encoding="utf-8") as srt:
                write_srt(result["segments"], file=srt)
            return result
        except Exception as e:
            raise CustomException(e, sys)

    def get_transcript(self, audio_paths: List[Path], transcribe: callable):
        """
        It takes a list of audio paths and a transcribe function as input, and returns a dictionary of video
        paths and their corresponding srt paths, and a result object
        """
        try:
            srt_path = self.output_dir
            subtitles_path = {}

            for path, audio_path in audio_paths.items():
                filename = os.path.basename(path).split('.')[0]
                srt_path = os.path.join(srt_path, f"{filename}.srt")

                result = self.create_subtitles(
                    audio_path, srt_path, transcribe)

                subtitles_path[path] = srt_path

            return subtitles_path, result
        except Exception as e:
            raise CustomException(e, sys)

    def get_subtitle(self, video_path, model, task, verbose=False):
        """
        It takes a video path, a model path, and a task (either "stt" or "asr") and returns a subtitle

        Args:
          video_path: The path to the video file.
          model: The path to the model you want to use.
          task: The task to be performed. It can be either "stt" or "asr".
          verbose: If True, prints the progress of the transcription. Defaults to False

        Returns:
          The subtitle is being returned.
        """
        try:
            os.makedirs(self.output_dir, exist_ok=True)
            if model.endswith(".en"):
                print(f"{model} is a English model")
            model = whisper.load_model(model)
            audio = self.get_audio([video_path])
            subtitle = self.get_transcript(
                audio, lambda audio_path: model.transcribe(audio_path,
                                                           verbose=verbose, task=task))
            return subtitle
        except Exception as e:
            raise CustomException(e, sys)
