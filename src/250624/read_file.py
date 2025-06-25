handle = open("read_sample.txt")
# data = handle.readline()  # 파일 객체에서 파일을 한 줄 읽음
data = handle.readlines()  # 파일 객체에서 파일의 내용을 읽어 리스트로 반환
# data2 = handle.readline()
print(data)
# print(data2)

handle.close()
