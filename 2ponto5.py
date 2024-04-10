import nltk
from nltk.tokenize import word_tokenize

#Este produto é excelente e atendeu todas as minhas expectativas.
sentence = "Este produto é ok, porém a entrega foi ótima e o preço ruim."
tokens = word_tokenize(sentence)
print(tokens)

# Cria uma lista de palavras positivas, negativas e neutras

positive_words = ["excelente", "ótimo", "maravilhoso"]
negative_words = ["ruim", "péssimo", "desapontador"]
neutral_words = ["ok", "regular", "normal"]

positive_count = sum(token in positive_words for token in tokens)
negative_count = sum(token in negative_words for token in tokens)
neutral_count = sum(token in neutral_words for token in tokens)

if positive_count > negative_count and positive_count > neutral_count:
    print("Opinião positiva")
elif negative_count > positive_count and negative_count > neutral_count:
    print("Opinião negativa")
else:
    print("Opinião neutra")



# O sistema de classificação baseado apenas na contagem de palavras pode ser insuficiente para determinar a polaridade geral da opinião, pois as palavras positivas, negativas e neutras estão presentes em contextos contraditórios na mesma frase. 