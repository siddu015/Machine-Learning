import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download stopwords data
nltk.download('stopwords')

# Input text
text = "NLTK is a leading platform for building Python programs to work with human language data."

# Tokenize the text
words = word_tokenize(text)

# Set of stopwords in English
stop_words = set(stopwords.words('english'))

# Remove stopwords
filtered_words = [word for word in words if word.lower() not in stop_words]

# Print filtered words
print(filtered_words)