outfile = open('topics.txt', 'w') # 복수 실행하면 파일 덮어쓰기
outfile.write('Web-Python')
outfile.close()

outfile = open('topics.txt', 'a') # data 추가
outfile.write('software')
outfile.close()