import csv, codecs
# CSV 파일 열기
filename = "test.csv"
fp = codecs.open(filename, "r", "euc_kr")
# 한 줄씩 읽어 들이기
reader = csv.reader(fp, delimiter=",", quotechar='"')
print(reader)  # 주소가 나온다.
for cells in reader:
    # print(cells)
    print(cells[1], cells[2])