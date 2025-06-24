def read_fasta(filepath: str) -> str:
    """FASTA 파일을 읽어서 문자열로 반환하는 함수

    Args:
        filepath (str): FASTA 파일 경로

    Returns:
        str: FASTA 서열

    Example:
        >>> seq = read_fasta("sample.fasta")
        >>> print(seq)
        AAGGTTCC
    """
    sequence = ""
    with open(filepath) as handle:
        for line in handle:
            if line.startswith(">"):
                continue
            sequence += line.strip()
    return sequence


def count_bases(sequence: str) -> dict[str, int]:
    """서열에서 base의 개수를 세어서 dict로 반환하는 함수

    Args:
        sequence (str): 서열

    Returns:
        dict[str, int]: 서열 문자를 센 데이터

    Example:
        >>> data = count_bases(sequence)
        >>> print(data)
        {"A": 10, "C": 20, "G": 30, "T": 40}
    """
    data: dict[str, int] = dict()
    for base in sequence:
        if base not in data:
            data[base] = 0
        data[base] += 1
    return data


def test_count_bases():
    seq = "AAGT"
    data = count_bases(seq)
    assert {"A": 2, "G": 1, "T": 1} == data
    print("TEST 성공")


def calc_gc_content(sequence: str) -> float:
    """서열의 GC(%)를 계산하는 함수

    Args:
        sequence (str): 서열

    Returns:
        float: GC(%)

    Example:
        >>> gc_content = calc_gc_content(sequence)
        >>> print(gc_content)
        48.5
    """
    count_data = count_bases(sequence)
    gc_content: float = (
        (count_data.get("G", 0) + count_data.get("C", 0)) / len(sequence) * 100
    )  # count_data["G"] -> count_data.get("G", 0)
    return gc_content


def test_calc_gc_content():
    seq = "ACGTT"
    gc_content = calc_gc_content(seq)
    assert 40 == gc_content
    print("TEST 통과")
    seq = "ACACA"
    gc_content = calc_gc_content(seq)
    assert 40 == gc_content
    print("TEST 통과")


def write_result(result_filepath: str, data: dict[str, int], gc_content: float):
    """결과 파일경로를 인자로 받아서 결과를 쓰기.
    GC(%): 40.0
    A: 10
    C: 20
    G: 30
    T: 40

    Args:
        result_filepath (str): 결과 파일 경로
        data (dict[str, int]): base count 데이터
        gc_content (float): GC(%)
    """
    with open(result_filepath, "w") as handle:
        handle.write(f"GC(%): {gc_content}\n")
        for base, base_count in data.items():
            handle.write(f"{base}: {base_count}\n")


if __name__ == "__main__":
    test_count_bases()
    test_calc_gc_content()
