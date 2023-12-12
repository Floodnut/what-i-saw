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
LPUSH list_key a # 리스트 왼쪽에 값 a 추가
RPUSH list_key b # 리스트 오른쪽에 값 b 추가
LPOP list_key # 리스트 왼쪽 값 제거 및 반환
RPOP list_key # 리스트 오른쪽 값 제거 및 반환
LRANGE list_key 0 -1 # 리스트의 0번 인덱스부터 -1(오른쪽 끝) 인덱스까지 출력
# 1) ...
# 2) ...
# ...
# 마지막 인덱스
```

`LTRIM`은 시작과 끝 인덱스를 전달받아 범위 밖을 삭제한다.  
`LPOP`과 같이 삭제하는 값을 반환하지는 않는다.  
`LPUSH`와 `LTRIM`을 조합해 고정된 길이의 큐를 유지할 수 있다. (`PUSH` -> `TRIM`)
- 리스트의 tail 데이터 처리는 O(1)으로 동작하기에 배치로 일괄 삭제하는 것보다 효율적으로 작업을 수행할 수 있다.
- `LPUSH`, `RPUSH`, `LPOP`, `RPOP` 등이 그 대상이다.
- 리스트의 중간 인덱스에 대한 접근은 O(n)으로 동작한다.
```bash
LTRIM list_key 0 1 # 0 ~ 1 인덱스 이후 모두 삭제
```

`LINSERT`는 원하는 데이터의 앞/뒤에 데이터를 추가한다.  
`LSET`은 특정 인덱스의 값을 덮어쓴다.
```bash
LINSERT list_key BEFORE A B # A앞에 B를 추가하고 리스트 크기 반환
LSET 1 A # 1번 인덱스에 A를 덮어쓴다. 범위를 벗어나면 에러를 반환한다.
LINDEX 3 # 3번 인덱스의 값을 확인한다.
```