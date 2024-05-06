# importing 
import pandas as pd
import nltk
from nltk import pos_tag, ne_chunk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import spacy
import string

# Download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
nlp = spacy.load('en_core_web_sm')


# Exercise 1: Exploring Text Preprocessing Usage, NER And POS Tags
# 1. Create a function preprocess_text() wich will receive the data as argumentץ

# convert all the text in lower case and tokanize it

def preprocess_text(data):
    stop_words = set(stopwords.words('english'))

    preprocessed_text = []

    for review in data['Review']:
        # Convert all the text to lowercase and tokenize it
        lower_review = review.lower()
        tokens = word_tokenize(lower_review)

        # Remove punctuation
        tokens = [token for token in tokens if token not in string.punctuation]

        # Remove stopwords
        tokens = [token for token in tokens if token not in stop_words]

        # Convert tokens back to string
        processed_review = ' '.join(tokens)

        # Apply a lemmatizer (if needed)
        doc = nlp(processed_review)
        lemmatized_tokens = [token.lemma_ for token in doc]

        # Join lemmatized tokens back to string
        processed_review = ' '.join(lemmatized_tokens)

        preprocessed_text.append(processed_review)

    return preprocessed_text


# 2. Create a new dataset with the cleaned text

def create_cleaned_dataset(raw_data, preprocessed_text):
    cleaned_data = raw_data.copy()
    cleaned_data['Cleaned_Review'] = preprocessed_text
    return cleaned_data



# 3. Create a function perform_ner() that will receive the text as argument and perform NER tagging on it. Use spacy en_core_web_sm

def perform_ner(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities
    

# 4. Create a function perform_pos_tagging() that will receive the text as argument and perform POS tagging on it.

def perform_pos_tagging(text):
    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)
    return tagged



data = {
    'Review': [
        'At McDonald\'s the food was ok and the service was bad.',
        'I would not recommend this Japanese restaurant to anyone.',
        'I loved this restaurant when I traveled to Thailand last summer.',
        'The menu of Loving has a wide variety of options.',
        'The staff was friendly and helpful at Google\'s employees restaurant.',
        'The ambiance at Bella Italia is amazing, and the pasta dishes are delicious.',
        'I had a terrible experience at Pizza Hut. The pizza was burnt, and the service was slow.',
        'The sushi at Sushi Express is always fresh and flavorful.',
        'The steakhouse on Main Street has a cozy atmosphere and excellent steaks.',
        'The dessert selection at Sweet Treats is to die for!'
    ]
}


preprocessed_text = preprocess_text(data)
# print(preprocessed_text)

cleaned_dataset = create_cleaned_dataset(data, preprocessed_text)
# print("Cleaned Dataset:")
# print(cleaned_dataset)

# Perform NER/POS on a sample review
sample_review = cleaned_dataset['Cleaned_Review'][0]
entities = perform_ner(sample_review)
entities2 = perform_pos_tagging(sample_review)


# for entity in entities:
#     print(entity)

# for word, tag in entities2:
#     print(f'Word: {word}, POS: {tag}')