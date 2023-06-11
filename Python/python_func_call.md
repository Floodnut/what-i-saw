## 파이썬 함수 호출

일반적으로 함수를 호출할 때, `def`로 선언한 함수를 직접 호출하게 된다.

```python
def func(a:int):
    print(a)

# ...

func(1)
```

하지만 다음과 같은 경우를 생각해보자. `root`함수는 조건에 맞게 `func1`부터 `func3`을 호출하고 실행시킨다.   
이 경우 조건에 따른 함수의 호출 자체는 명확하나 `root` 내부의 적합한 조건에 맞도록 `if-elif-else`를 모두 순회해야 한다.


```python
def func1(a:int):
    print(a)

def func2(a:int):
    print(a * 2)

def func3(a:int):
    print(a + 2)

# ...

def root(a:int):

    if a == 1:
        func1(a)
    
    elif a == 2:
        func2(a)

    else:
        func3(a)

# ...

root(3)
```

그렇기에 우리는 함수를 `dict`로 관리할 수 있고 해시테이블과 같이 조건에 맞는 함수를 바로 접근할 수 있다.  
필요한 경우 인자를 추가로 넘길 수 있다.


```python
def func1(a:int):
    print(a)

def func2(a:int):
    print(a * 2)

def func3(a:int):
    print(a + 2)

# ...

func_calls = {1: func1, 2: func2, 3: func3 }

# ...

def root(a:int):

    # 또는 func_calls.get()
    func_calls[a]()
# ...

root(3)
```

