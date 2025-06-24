import argparse

import dna_utils

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
# 결과 파일을 --output으로 받고 결과파일에 결과를 쓰는 것 구현
args = parser.parse_args()

input_fasta_filepath = args.input  # sample.fasta
result_filepath = args.output  # result.txt
sequence = dna_utils.read_fasta(input_fasta_filepath)
base_count_data = dna_utils.count_bases(sequence)
gc_data = dna_utils.calc_gc_content(sequence)
dna_utils.write_result(result_filepath, base_count_data, gc_data)

# 결과 출력
print(base_count_data)
print(gc_data)
