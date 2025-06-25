import gzip


def count_line(vcf_filepath: str) -> int:
    line_num = 0
    with gzip.open(vcf_filepath, "rt") as handle:
        for line in handle:
            if line.startswith("#"):
                continue
            line_num += 1
    return line_num


def count_line_with_qual(vcf_filepath: str, qual: float) -> int:
    # vcf file을 라인마다 읽어서, QUAL의 값이 qual 이상인 라인만 카운트하기
    line_num = 0
    with gzip.open(vcf_filepath, "rt") as handle:
        for line in handle:
            if line.startswith("##"):  # meta 제외
                continue
            if line.startswith("#"):  # header
                header = line.strip().split("\t")
                qual_idx = header.index("QUAL")  # 5
                continue
            row = line.strip().split("\t")
            if float(row[qual_idx]) >= qual:
                line_num += 1
    return line_num


def calc_tstv(vcf_filepath: str) -> float:
    # TODO: tstv 를 계산하여 소수점 4째 자리에서 반환
    # Purine: A, G
    # Pyrimidine: C, T
    # Transition: Pu <-> Pu, Py <-> Py
    # Transversion: Pu <-> Py
    ts_num, tv_num = 0, 0
    purine = {"A", "G"}
    pyrimidine = {"C", "T"}
    with gzip.open(vcf_filepath, "rt") as handle:
        for line in handle:
            if line.startswith("##"):  # meta 제외
                continue
            if line.startswith("#"):  # header
                header = line.strip().split("\t")
                ref_idx = header.index("REF")
                alt_idx = header.index("ALT")
                continue
            row = line.strip().split("\t")
            ref = row[ref_idx]
            alt = row[alt_idx]
            if ref in purine and alt in purine:
                ts_num += 1
            elif ref in pyrimidine and alt in pyrimidine:
                ts_num += 1
            elif ref in purine and alt in pyrimidine:
                tv_num += 1
            elif ref in pyrimidine and alt in purine:
                tv_num += 1
    return round(ts_num / tv_num, 4)


if __name__ == "__main__":
    vcf_filepath = "data/sample.ann.vcf.gz"
    # line_num = count_line(vcf_filepath)
    # line_num = count_line_with_qual(vcf_filepath, 1000.0)
    # print(line_num)
    tstv_ratio = calc_tstv(vcf_filepath)
    print(tstv_ratio)
