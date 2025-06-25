import sys

if len(sys.argv) != 2:
    print(f"#Usage: python {sys.argv[0]} [GENE]")
    sys.exit()

gene = sys.argv[1]
print(f"GENE: {gene}")
