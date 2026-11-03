#implement a basic NLP text - processing system for a given paragraph . perform tokenization , sentence segmentation , removal of unnessecary words and basic language / grammar processing , Display the processed output and explain the role of each NLP component used.
import spacy


nlp = spacy.load("en_core_web_sm")


paragraph = (
    "Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence. "
    "It helps computers understand human language easily! "
    "However, raw text often contains unnecessary noise, like stopwords and punctuation."
)


doc = nlp(paragraph)

print("\n" * 2)

print("1. SENTENCE SEGMENTATION")

sentences = list(doc.sents)
for idx, sent in enumerate(sentences, 1):
    print(f"Sentence {idx}: {sent.text}")
print("\n" * 2)

print("2. TOKENIZATION")

tokens = [token.text for token in doc]
print("Tokens:", tokens)

print("\n" * 2)

print("3. REMOVAL OF UNNECESSARY WORDS (Stopwords & Punctuation)")


cleaned_tokens = [
    token.text for token in doc 
    if not token.is_stop and not token.is_punct and not token.is_space
]
print("Filtered Tokens:", cleaned_tokens)

print("\n" * 2)

print("4. BASIC GRAMMAR & LANGUAGE PROCESSING")

print(f"{'Token':<15} | {'Lemma (Base)':<15} | {'POS Tag':<10} | {'Dependency':<12}")

for token in doc:
    
    if not token.is_punct and not token.is_space:
        print(f"{token.text:<15} | {token.lemma_:<15} | {token.pos_:<10} | {token.dep_:<12}")