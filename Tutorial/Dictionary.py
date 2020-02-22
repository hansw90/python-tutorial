"""
딕셔너리 타입은 immutable 한 키오 mutable 한 값으로 맵핑되어 있는 순서가 없느 ㄴ집합이다.
REPL에서 확인합니다
일반적인 딕셔너리 타입의 모습입니다. 중괄호로 되어있고 키와 값이 있습니다.

"""

{"A" : 1, "B" : 2}

# 키로는 immutable 한 값은 사용할 수 있지만, mutable 한 객체는 사용할 수 없습니다.

# immutable 예

a = {1:5,2:3}
a

a={(1,5) : 5, (3,3) : 3} #tuple 사용


a={3.6:5, "abc":3} #float 사용
a

a={True :5, "abc" : 3} #bool 사용
a

# 값은 중복될 수 있지만, 키가 중복되면 마지막 값으로 덮어씌워진다
a = {"a" : 1, "a":2}
a #{'a': 2}

# 순서가 없기 떄문에 인덱스로는 접근할 수 없고, 키로 접근 할 수 있다.
"""
>>> d = {'abc' : 1, 'def' : 2}
>>> d[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 0
>>> d['abc']
1

"""

## dictionary (딕셔너리)선언
#딕셔너리 선언할때는 빈 중괄호를 사용한다. (set 중괄호를 이용하지만 빈중괄호로 선언하면 type 이 dict가 된다)
#딕셔너리로 명시적으로 선언 할 수도 있습니다.

"""
>>> e = {}
>>> type(e)
<class 'dict'>
>>> f = dict()
>>> type(f)
<class 'dict'>
"""

# dict constructor를 통해서 아래와 같이 바로 키와 값을 할당하며 선언할 수 있습니다.
newdict = dict(alice =5, bob = 20, tony = 15, suzy= 30)
newdict

"""
얕은 복사(shallow copy) 1
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b =a.copy()
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
얕은 복사(shallow copy) 2
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = dict(a)
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> id(a)
4334645680
>>> id(b)
4334648920


깊은 복사(deep copy)
>>> import copy
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> b = copy.deepcopy(a)
>>> b['alice'].append(5)
>>> b
{'alice': [1, 2, 3, 5], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> a
{'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
"""



"""
6. dictionary(딕셔너리) for문
for문을 통해 딕셔너리를 for문을 돌리면 key값이 할당됩니다.
순서는 임의적이다.같은 순서를 보장할 수 없다.
>>> a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}
>>> for key in a:
...     print(key)
... 
alice
bob
tony
suzy
value값으로 for문을 반복하기 위해서는 values() 를 사용해야합니다.
>>> for val in a.values():
...     print(val)
... 
[1, 2, 3]
20
15
30    
key와 value를 한꺼번에 for문을 반복하려면 items() 를 사용합니다.
>>> for key, val in a.items():
...     print("key = {key}, value={value}".format(key=key,value=val))
... 
key = alice, value=[1, 2, 3]
key = bob, value=20
key = tony, value=15
key = suzy, value=30
"""
