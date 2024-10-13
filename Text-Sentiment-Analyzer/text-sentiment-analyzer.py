from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from textblob import TextBlob

def analyze_text_sentiment(text):
    # Split text
    tokenized_text = text.split(' ')

    # Remove stop words from text
    stop_words = set(stopwords.words('english'))
    tokenized_text = [word for word in tokenized_text if word not in stop_words]

    # Stem text
    porter_stemmer = PorterStemmer()
    tokenized_text = [porter_stemmer.stem(word) for word in tokenized_text]

    # Generate sentiment
    print("\nText Analysis Result:")
    result = TextBlob(' '.join(tokenized_text))
    text_polarity = result.polarity
    text_subjectivity = result.subjectivity

    # Output sentiment analysis result
    print(f"- Polarity: {text_polarity}")
    print(f"- Subjectivity: {text_subjectivity}")

def main():
    print(":: WELCOME TO TEXT SENTIMENT ANALYZER APP ::\n")
    text_to_analyze = input("|> Enter text to analyze: ")
    analyze_text_sentiment(text_to_analyze)

if __name__ == "__main__":
    main()