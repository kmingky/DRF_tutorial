##  1. args, kwargs를 사용하는 예제 코드 짜보기
```python
def my_name(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"key:{key}, val:{value}")

my_name('kim', 'minki', lastname='kim', firstname='minki')
```
<br>

## 2. mutable과 immutable은 어떤 특성이 있고, 어떤 자료형이 어디에 해당하는지 서술하기
### 2.1 mutable : 리스트(list), 딕셔너리(dictionary), NumPy의 배열(ndarray)
값을 변경할 수 있는 객체
### 2.2 immutable : 숫자(number), 문자열(string), 튜플(tuple)
값을 변경할 수 없는 객체
### 2.3 복사를 통한 비교
```python
import copy

x = [1,2]
y = x
z = x[:]
deep_copy = copy.deepcopy(x)

print(x,":",id(x))
print(y,":",id(y))
print(z,":",id(z))
print(deep_copy,":",id(deep_copy))

# 눈에 보이는 결과 값은 같으나 주소값은 다르다.
```
속성에 따라 변수가 함수의 매개변수로 전달될 때 원래 입력 변수값이 변경되는지 안되는지 결정된다.   

<br>

## 3. DB Field에서 사용되는 Key 종류와 특징 서술하기
### 3.1 Primary Key
테이블당 하나의 PK만 존재가 가능하며 키값을 지정하지 않는 경우 id값이 자동 생성
### 3.2 Foreign Key
다른 테이블의 PK를 참조하여 관계를 연결하는 키(onetoone, onetomany, manytomany)
### 3.3 Unique Key
테이블 내 중복된 값을 가질수 없게끔 지정하는 키(id, email)   

<br>

## 4. django에서 queryset과 object는 어떻게 다른지 서술하기
### 4.1 queryset
DB에서 전달받은 model의 object list로 Django ORM에서 발생한 자료형이다.
Python으로 작성한 코드가 SQL로 mapping되어 QuerySet이라는 자료 형태로 값이 넘어온다.
### 4.2 object
dictionary로 구성된 데이터 객체이다.
### 4.3 비교
```python
User.objects.all()
<QuerySet[<User: User object (1)>]>  # User의 object를 모두 불러오면 queryset으로 반환한다.

User.objects.get(username='minki')  # User의 username이 minki인 object를 반환한다.

User.objects.creat(username='new') # User에 new로 새로운 object가 생성되면
User.objects.all()
 <QuerySet[<User: User object (2)>]> # queryset이 2가 된다.
```
