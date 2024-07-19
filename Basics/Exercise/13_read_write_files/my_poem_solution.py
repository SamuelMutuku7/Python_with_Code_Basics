import string

word_stats = {}

with open("poem.txt", "r") as poem:
    for line in poem:
        # Remove punctuation and convert to lowercase
        line = line.translate(str.maketrans("", "", string.punctuation)).lower()
        words = line.split()
        for word in words:
            if word in word_stats:
                word_stats[word] += 1
            else:
                word_stats[word] = 1

print(word_stats)

max_count = max(word_stats.values())
print("The maximum occurrences of any word is:", max_count)

print("The words with the maximum occurrences are: ")
for word, count in word_stats.items():
    if count == max_count:
        print(f"{word}: {count}")
