from collections import defaultdict

data = defaultdict(int)
s = "ATTAAAGGTTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTAGATCTGTTCTCTAAA"
for base in s:
    data[base] += 1

print(data)
