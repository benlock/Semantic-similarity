import spacy
nlp = spacy.load('en_core_web_sm')

word1 = nlp('cat')
word2 = nlp('monkey')
word3 = nlp('banana')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#Cat and monkey are similar because they are animals. Monkey and banana are more similar than cat and banana, because monkeys eat bananas. 

word4 = nlp('fish')
word5 = nlp('chips')
word6 = nlp('shark')

print(word4.similarity(word5))
print(word5.similarity(word6))
print(word6.similarity(word4))

#Fish and chips are similar, so are fish and shark, but shark and chips are not similar. 

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = 'Why is my car on the car'

sentences = ["Where did my dog go", "Hello, there is my car", "I\'ve lost my car in my car", "I\'d like my boat back", 'I will namy my dog Diana']

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#When using the simpler model, only the sentences can be compared, not individual words. 

