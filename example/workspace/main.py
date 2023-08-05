from file_upload import FileUpload
from transcription_service import TranscriptionService
from sentiment_analysis import SentimentAnalysis
from soundtrack_creation import SoundtrackCreation
from audio_processing import AudioProcessing
from final_audio_file import FinalAudioFile

def main():
    # Instantiate classes
    file_upload = FileUpload()
    transcription_service = TranscriptionService()
    sentiment_analysis = SentimentAnalysis()
    soundtrack_creation = SoundtrackCreation()
    audio_processing = AudioProcessing()
    final_audio_file = FinalAudioFile()

    # Upload and process the audio file
    file_path = file_upload.upload_file("example.mp3")
    if file_upload.verify_format(file_path):
        file_path = file_upload.convert_to_mp3(file_path)
        text = transcription_service.transcribe_audio(file_path)
        sentiment = sentiment_analysis.analyze_sentiment(text)
        soundtrack = soundtrack_creation.generate_soundtrack(sentiment)

        # Process the audio
        file_path = audio_processing.noise_reduction(file_path)
        file_path = audio_processing.remove_silence(file_path)
        file_path = audio_processing.normalize_audio(file_path)

        # Compile the final audio file
        final_file_path = final_audio_file.compile_segments([file_path, soundtrack])
        print(f"Final podcast file: {final_file_path}")

if __name__ == "__main__":
    main()
