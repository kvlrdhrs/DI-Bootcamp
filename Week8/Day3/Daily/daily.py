import requests
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

def load_texts(urls):
    corpus = []
    for url in urls:
        response = requests.get(url)
        text = response.text

        # Extract relevant parts of the text
        start_idx = text.find('START')
        end_idx = text.find('*** END')
        if start_idx != -1 and end_idx != -1:
            text = text[start_idx:end_idx]

        # Clean the text
        text = re.sub(r'[^A-Za-z\s]', '', text)
        text = re.sub(r'\s+', ' ', text).strip()

        corpus.append(text)
        print(f"First 200 characters of text from {url}:\n{text[:200]}\n")

    return corpus

# URLs of the texts
urls = [
    "https://www.gutenberg.org/cache/epub/11/pg11.txt",
    "https://www.gutenberg.org/cache/epub/12/pg12.txt",
    "https://www.gutenberg.org/cache/epub/29042/pg29042.txt"
]

# Load and clean the texts
corpus = load_texts(urls)

# Tokenize the texts and print the first 150 tokens of each book
for i, text in enumerate(corpus):
    tokens = word_tokenize(text)
    print(f"First 150 tokens of book {i+1}:\n{tokens[:150]}\n")

# Remove stopwords using NLTK
stop_words = set(stopwords.words('english'))
filtered_texts = []
for i, text in enumerate(corpus):
    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    filtered_texts.append(' '.join(filtered_tokens))
    print(f"Sample filtered tokens from book {i+1} (checking stopword removal):\n{filtered_tokens[:150]}\n")

# Perform stemming using PorterStemmer
ps = PorterStemmer()
stemmed_texts = []
for text in filtered_texts:
    tokens = word_tokenize(text)
    stemmed_tokens = [ps.stem(word) for word in tokens]
    stemmed_texts.append(' '.join(stemmed_tokens))
    print(f"First 50 stemmed tokens:\n{stemmed_tokens[:50]}\n")

# Perform lemmatization using spaCy
lemmatized_texts = []
for text in filtered_texts:
    doc = nlp(text)
    lemmatized_tokens = [token.lemma_ for token in doc]
    lemmatized_texts.append(' '.join(lemmatized_tokens))
    print(f"First 50 lemmatized tokens:\n{lemmatized_tokens[:50]}\n")

# Analyze the difference between stemmed and lemmatized tokens
# Here, we'll simply compare the first 50 tokens for analysis
print("Comparison of stemmed and lemmatized tokens (first 50 tokens):")
print(f"Stemmed tokens: {stemmed_tokens[:50]}")
print(f"Lemmatized tokens: {lemmatized_tokens[:50]}")

# Identify POS tags using NLTK
for i, text in enumerate(filtered_texts):
    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    print(f"Sample POS tags from book {i+1}:\n{pos_tags[:50]}\n")

# Identify named entities using NLTK
for i, text in enumerate(filtered_texts):
    tokens = word_tokenize(text)
    pos_tags = nltk.pos_tag(tokens)
    chunks = nltk.ne_chunk(pos_tags)
    entities = [chunk for chunk in chunks if hasattr(chunk, 'label')]
    print(f"Sample named entities from book {i+1}:\n{entities[:50]}\n")

# Generate and display word clouds for each book
for i, text in enumerate(filtered_texts):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud for Book {i+1}")
    plt.show()

# Bag of Words (BoW) method to check the five most frequent words
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(filtered_texts)
word_counts = X.toarray().sum(axis=0)
words = vectorizer.get_feature_names_out()
word_freq = dict(zip(words, word_counts))
sorted_word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

print("Top 5 most frequent words across all books:")
for word, freq in list(sorted_word_freq.items())[:5]:
    print(f"{word}: {freq}")

# Display a pie plot of the 5 most frequent words in the text
top_words = list(sorted_word_freq.keys())[:5]
top_counts = list(sorted_word_freq.values())[:5]

plt.figure(figsize=(8, 8))
plt.pie(top_counts, labels=[f"{word} ({count})" for word, count in zip(top_words, top_counts)], autopct='%1.1f%%')
plt.title("Top 5 Most Frequent Words")
plt.show()

# Create another BoW using TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(min_df=1, max_df=2)
X_tfidf = tfidf_vectorizer.fit_transform(filtered_texts)
tfidf_word_scores = X_tfidf.toarray().sum(axis=0)
tfidf_words = tfidf_vectorizer.get_feature_names_out()
tfidf_word_freq = dict(zip(tfidf_words, tfidf_word_scores))
sorted_tfidf_word_freq = dict(sorted(tfidf_word_freq.items(), key=lambda item: item[1], reverse=True))

print("Top 5 most relevant words using TF-IDF across all books:")
for word, score in list(sorted_tfidf_word_freq.items())[:5]:
    print(f"{word}: {score}")

# Display a pie plot of the 5 most relevant words in the text using TF-IDF
top_tfidf_words = list(sorted_tfidf_word_freq.keys())[:5]
top_tfidf_scores = list(sorted_tfidf_word_freq.values())[:5]

plt.figure(figsize=(8, 8))
plt.pie(top_tfidf_scores, labels=[f"{word} ({score:.2f})" for word, score in zip(top_tfidf_words, top_tfidf_scores)], autopct='%1.1f%%')
plt.title("Top 5 Most Relevant Words (TF-IDF)")
plt.show()