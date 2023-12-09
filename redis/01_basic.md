## Redis DS
### string
- 한 문자열은 512mb까지 지정할 수 있다.
- 문자열은 binary-safe 하기에 jpeg와 같은 바이트 값이나 http 응답 값 역시 저장할 수 있다.

```bash
GET key 
SET key value

# NX 옵션은 지정한 키가 없을 때에만 새로운 키-값을 저장한다.
SET key value NX

# XX 옵션은 지정한 키가 있을 때에만 새로운 키-값을 저장한다.
SET key value XX
```

숫자 역시 저장할 수 있다.
```bash
# 숫자의 경우 INCR, INCRBY / DECR, DECRBY로 atomic하게 값을 조작할 수 있다.
SET key 1
INCR key # 2
INCRBY key 3 
```

여러 값을 동시에 조작하기 위해서는 `MGET`, `MSET`을 사용한다.
```bash
MSET a 10 b 20
MGET a b
# 1) "10"
# b) "20"
```
### list
한 리스트에는 최대 42억여 개의 아이템을 저장할 수 있다.
- 인덱스를 통해서 접근할 수 있다.
- 스택/큐로 사용할 수 있다.

```bash
LPUSH list_key a
RPUSH list_key b
LPOP list_key
RPOP list_key
LRANGE list_key 0 -1
# 1) ...
# 2) ...
# ...
# 마지막 인덱스
```