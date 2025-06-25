A, C, G, T = 0, 0, 0, 0
with open("read_sample.txt") as handle:
    for line in handle:
        if line.startswith(">"):
            continue

        A += line.count("A")
        C += line.count("C")
        G += line.count("G")
        T += line.count("T")

print(f"A: {A}, C: {C}, G: {G}, T: {T}")
