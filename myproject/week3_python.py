name = 'bob' # let 없고 ; 없고 주석은 #
num = 12 # 똑같음
is_number = True # js에서는 true (대소문자 주의)

a_list = [] # 빈 리스트
a_list.append(1) # js에서는 push
a_list[0] # 호출하는 것은 똑같음
print(a_list)

a_dict = {}
a_dict = {'name': 'bob', 'age': 21}
a_dict['height'] = 178 # 새로 추가
print(a_dict['name']) # 값 가져오기 똑같음
print(a_dict)

people = [{'name': 'bob', 'age': 20}, {'name': 'carry', 'age': 25}]
print(people[0]['name']) # bob

def make_card(image):
    # 파이썬은 들여쓰기를 강제한다! 대신 {} 쓰지 않는다. 
    print(image)

make_card('hello')

# 조건문
def oddeven(num):
    if num % 2 == 0: # if 다음에 () 없음 : 들여쓰기로 구분
        return True
    else:
        return False

print(oddeven(10))

# 반복문

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

for fruit in fruits: # fruits 에서 하나씩 꺼내다가 fruit에 저장해서 쓴다
    print(fruits)

count = 0 # 사과 개수 저장하는 변수
for fruit in fruits:
    if fruit == '사과':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

def get_age(myname):
    # myname에 들어온 이름의 나이를 출력하는 함수
    for person in people:
        # people 리스트를 하나씩 person에 담아둠 
        if person['name'] == myname:
            print(person['age'])

get_age('bob')