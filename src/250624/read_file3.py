data = {"A": 0, "C": 0, "G": 0, "T": 0}
with open("read_sample.txt") as handle:
    for line in handle:
        if line.startswith(">"):
            continue

        for base in line.strip():
            data[base] += 1

print(data)
