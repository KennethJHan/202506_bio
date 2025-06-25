class DNA:  # 틀
    def __init__(self, seq: str, sample_id: str):  # self는 객체 그 자신
        self.seq = seq
        self.sample_id = sample_id

    def get_length(self):
        return len(self.seq)

    def get_gc_content(self) -> float:
        num_c = self.seq.count("C")
        num_g = self.seq.count("G")
        return (num_c + num_g) / self.get_length() * 100

    def is_palindrome(self) -> bool:
        return self.seq[::-1] == self.seq

    def get_transcribed(self) -> str:
        return self.seq.replace("T", "U")

    def __eq__(self, other) -> bool:
        return self.seq == other.seq

    def __str__(self) -> str:  # print()
        return f">{self.sample_id}\n{self.seq}"

    def __add__(self, other) -> str:  # +
        return self.seq + other.seq


# import 할 때 수행 x
# python dna.py 할 때는 수행 o
if __name__ == "__main__":
    dna1 = DNA("ACGT", "test_sample")  # dna1은 object
    dna2 = DNA("ACGT", "test2_sample")
    print(dna1 + dna2)
    print(dna1.get_gc_content(), dna2.get_gc_content())
    print(dna1.is_palindrome(), dna2.is_palindrome())
    print(dna1.get_transcribed(), dna2.get_transcribed())
    print(dna1 == dna2)  # print(dna1.seq == dna2.seq)
