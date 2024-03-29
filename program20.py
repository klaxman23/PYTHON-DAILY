# spelling correction with python 

from textblob import TextBlob

blob = TextBlob("i havv a guud ideea")

corrected_blob = blob.correct()

print("original text:", blob)

print("corrected text:", corrected_blob)


