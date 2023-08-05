from pydub import AudioSegment

class FinalAudioFile:
    def compile_segments(self, segments: list) -> str:
        final_audio = AudioSegment.empty()
        for segment in segments:
            final_audio += AudioSegment.from_file(segment, format="mp3")
        final_audio.export("final_podcast.mp3", format="mp3")
        return "final_podcast.mp3"
