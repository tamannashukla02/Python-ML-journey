from textblob import TextBlob

print("=== Sentiment Analyzer ===")

text = input("Enter your text: ")

analysis = TextBlob(text)

polarity = analysis.sentiment.polarity

if polarity > 0:
    sentiment = "Positive 😊"
elif polarity < 0:
    sentiment = "Negative 😢"
else:
    sentiment = "Neutral 😐"

print("\nResult:")
print("Sentiment:", sentiment)
print("Score:", polarity) 