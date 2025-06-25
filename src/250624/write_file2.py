filename = "write_sample.txt"

data = [">A_Strain", "ATGCGGAAG", "TCGGGATAG"]

with open(filename, "w") as handle:
    handle.write("\n".join(data))

with open(filename + "2", "w") as handle:
    handle.write(">A_Strain\nATGCGGAAG\nTCGGGATAG")
