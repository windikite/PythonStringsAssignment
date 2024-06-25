#Task 1
reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it.",
        "Average bAd, excELLent. Good."
    ]

words = ["good", "bad", "average", "excellent", "poor"]

def findAndCapitalize(string, words):
    string = str(string).lower()
    for word in words:
        found = string.find(word)
        while found != -1:
            word_length = len(word)
            first = string[0:found]
            second = string[found+word_length:]
            caps_word = str(word).upper()
            string = first + caps_word + second
            found = string.find(word)
    return string

for review in reviews:
    print(findAndCapitalize(review, words))


#Task 2
def tallyWords(string):
    string = str(string).lower()
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
    words = positive_words + negative_words
    positive = []
    negative = []
    for word in words:
        found = string.find(word)
        while found != -1:
            word_length = len(word)
            first = string[0:found]
            second = string[found+word_length:]
            string = first + second
            if word in positive_words:
                positive.append(word)
            elif word in negative_words:
                negative.append(word)
            found = string.find(word)
    return len(positive), len(negative)

counter = 1
for review in reviews:
    tally = tallyWords(review)
    print(f"There were {tally[0]} positive words and {tally[1]} negative words in review {counter}")
    counter += 1

#Task 3
def shorten(string):
    new_string_list = str(string).split(" ")
    joiner = " "

    while len(joiner.join(new_string_list)) > 30:
        new_string_list.pop()

    new_string = joiner.join(new_string_list)
    unwanted_characters = " ,.-'!?"

    while new_string[-1] in unwanted_characters:
        new_string = new_string[:-1]

    new_string = new_string + "..."
    return new_string

for review in reviews:
    print(shorten(review))