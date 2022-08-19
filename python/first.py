import sys
import time
from itertools import islice

start = time.time()
words = {}
with open(sys.argv[1]) as file:
  for word in file.read().split():
    word = word.lower()
    words[word] = words.setdefault(word, 0) + 1

top_length = 10
if len(sys.argv) == 3:
  top_length = int(sys.argv[2])
top_words = list(islice(words.items(), top_length))
for word, n in words.items():
  for i, top in enumerate(top_words):
    if n > top[1]:
      tmp = top_words[i:-1]
      top_words[i] = (word, n)
      top_words = top_words[0:i+1] + tmp
      break

print(top_words)
end = time.time()
print('elapsed: ' + str((end-start)*1000) + 'ms')