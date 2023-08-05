from textblob import TextBlob

class SentimentAnalysis:
    def analyze_sentiment(self, text: str) -> float:
        # Analyze the sentiment of the transcribed text using TextBlob
        analysis = TextBlob(text)
        return analysis.sentiment.polarity
