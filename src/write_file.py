data = dict()
with open("read_sample.txt") as handle:
    for line in handle:
        if line.startswith(">"):
            continue

        for base in line.strip():
            if base not in data:
                data[base] = 0

            data[base] += 1
# {"A": 11, ...}
with open("result.txt", "w") as handle:
    for key, value in data.items():
        # print(f"{key}: {value}")
        handle.write(f"{key}: {value}\n")
