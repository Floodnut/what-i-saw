# Commands for key-managing

## 키 관련 명령

키의 존재 여부를 파악하는 `EXISTS`
```bash
EXISTS key [key ...]
(integer) 1 # 없으면 0
```

저장된 모든 키를 조회하는 `KEYS`
- h`?`llo -> 길이 1의 문자
- h`*`llo -> 여러 길이의 문자
- h`[]`llo -> [] 안의 문자
- h`[^]`llo -> [] 안에서 ^를 제외한 문자
- h`[-]`llo -> [] - 범위 문자
```bash
KEYS pattern # 패턴은 GLOB 패턴 스타일로 동작한다.
```
특정 범위의 키를 조회하는 `SCAN`
- 커서 기반으로 조회한다.
```bash
SCAN cursor
```

## 키 자동 생성/삭제