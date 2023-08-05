import noisereduce as nr
from pydub import AudioSegment, effects

class AudioProcessing:
    def noise_reduction(self, file_path: str) -> str:
        audio = AudioSegment.from_file(file_path, format="mp3")
        reduced_noise = nr.reduce_noise(audio_array=audio.get_array_of_samples(), sr=audio.frame_rate)
        return AudioSegment(reduced_noise, frame_rate=audio.frame_rate, sample_width=audio.sample_width, channels=audio.channels)

    def remove_silence(self, file_path: str, silence_threshold: int = -50, min_silence_len: int = 1000) -> str:
        audio = AudioSegment.from_file(file_path, format="mp3")
        return audio.strip_silence(silence_threshold, min_silence_len)

    def normalize_audio(self, file_path: str, target_lufs: int = -16) -> str:
        audio = AudioSegment.from_file(file_path, format="mp3")
        return effects.normalize_lufs(audio, target_lufs)
