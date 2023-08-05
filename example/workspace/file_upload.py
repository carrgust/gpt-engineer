import os
from pydub import AudioSegment

class FileUpload:
    def upload_file(self, file_path: str) -> str:
        # Upload the file and return the file path
        return file_path

    def verify_format(self, file_path: str) -> bool:
        # Check if the file format is .mp3, .mov, or .wav
        file_extension = os.path.splitext(file_path)[1]
        return file_extension in ['.mp3', '.mov', '.wav']

    def convert_to_mp3(self, file_path: str) -> str:
        # Convert the file to MP3 format if needed
        file_extension = os.path.splitext(file_path)[1]
        if file_extension != '.mp3':
            audio = AudioSegment.from_file(file_path, file_extension[1:])
            new_file_path = os.path.splitext(file_path)[0] + '.mp3'
            audio.export(new_file_path, format='mp3')
            return new_file_path
        return file_path
