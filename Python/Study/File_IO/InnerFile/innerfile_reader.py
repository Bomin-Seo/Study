# import os
# os.getcwd() 현재 python이 실행되고 있는 current working dir을 반환
# os.chdir("address"), working dir 수정

file = open('File_example.txt', 'r')
# parameter = file name, mode(default = 'r'), ...
# file name으로 파일의 절대 경로를 사용할 때, /를 사용하거나 \\로 수정한다.

# 상대 경로 사용시 subfolder 라면 subfolder/filename을 사용하고,
# 상위 폴더의 파일을 사용한다면 ../../filename으로 사용한다.

contents = file.read()
# file cursor는 항상 파일의 제일 처음에 위치하며, 정방향으로만 동작한다.
# read()의 parameter로 정수 n을 입력하면 처음부터 n개까지의 text를 읽는다.
# 불러들인 data는 str type으로 저장
print(contents)
file.close()
print()

# 자동으로 file.close() 수행
# realine는 list형태로 저장, sorted나 reversed 형태로 data를 다룰 때 유용
with open('File_example.txt', 'r') as file:
    contents = file.readlines()
for line in contents:
    print(line)
print()
for line in contents:
    print(line.strip()) # \n도 여백으로 인식, strip()을 통해 제거