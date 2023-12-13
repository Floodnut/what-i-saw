# Redis Data-structures / Commands
## String
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
## List
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
## Hash
필드-값 쌍을 가진 아이템의 집합.  
하나의 Hash 자료 구조 안에서 아이템들이 문자열로 필드-값 쌍에 저장된다.
```python
# 아래와 같은 구조다.
KEY : {
    Field1 : Value1,
    Field2 : Value2,
    ...
}
```

RDBMS와 다르게 필드를 동적으로 추가함에 있어서 유연함을 가진다.
- 즉, 각 아이템마다 다른 필드를 가질 수 있다.

```bash
HSET key:1 id "id_test"
(integer) 1

HSET key:1 type a
(integer) 1

HSET key:3 id "id_2" type 1
(integer) 2
```

```bash
HGET key:1 id
"id_test"

# 여러 필드를 가져오기 위해서는 HMGET을 사용한다.
HMGET key:1 id type
1) "id_test"
2) "a"

# 모든 필드와 값을 가져오기 위해서는 HGETALL을 사용한다.
HGETALL key:1
1) "id"
2) "id_test"
3) "type"
4) "a"
```

## Set
집합 자료 구조이며 여러 아이템을 저장할 수 있다.  
중복을 허용하지 않으며 실제 저장되는 아이템 수를 반환한다.
```bash
SADD set1 a
(integer) 1
SADD set1 a a a b b c
(integer) 2 # 이전에 set1에 a가 이미 저장되었으므로 b, c 2개만 저장
SADD set2 a a a b b c
(integer) 3
```

`SMEMBERS`는 집합(Set)에 저장되어 있는 전체 아이템을 순서와 상관없이 출력한다.
```bash
SMEMBERS set1
1) "a"
2) "b"
3) "c"
```

`SREM`은 특정 데이터를 집합에서 삭제한다.
```bash
SREM set1 a
(integer) 1

SMEMBERS set1
1) "b"
2) "c"
```

`SPOP`은 집합 내 무작위 데이터를 반환하고 삭제한다.
```bash
SPOP set1
"b"
SMEMBERS set1
1) "c"
```

집합에서 합집합, 교집합, 차집합을 수행할 수 있다.
```bash
SADD set3 a
(integer) 1

# 합집합
SUNION set1 set3
1) "c"
2) "a"

# 교집합
SINTER set1 set3
(empty array)
SINTER set1 set2
1) "c"

# 차집합
SDIFF set2 set1
1) "a"
2) "b"
```

## Sorted Set
스코어 값에 따라 정렬되는 고유 문자열 집합.  
- 값이 저장될 때 스코어 값에 따라 정렬된다.
- 같은 스코어를 가진다면 사전 순으로 정렬된다.  

`ZADD`에 대한 공식 설명은 다음과 같다.
> 각 아이템 추가에 대해서 O(log(N))의 시간복잡도를 가지며, N은 sorted-set의 요소 수 이다.  
> O(log(N)) for each item added, where N is the number of elements in the sorted set.

```c
// src/server.h
#define ZADD_IN_NONE 0
```
```c
// src/t_zset.c

void zaddCommand(client *c) {
    zaddGenericCommand(c,ZADD_IN_NONE); // zaddGenericCommand(c, 0)와 같다.
}

void zaddGenericCommand(client *c, int flags) {
    static char *nanerr = "resulting score is not a number (NaN)";
    robj *key = c->argv[1];
    robj *zobj;
    sds ele;
    double score = 0, *scores = NULL;
    int j, elements, ch = 0;
    int scoreidx = 0;
    /* The following vars are used in order to track what the command actually
     * did during the execution, to reply to the client and to trigger the
     * notification of keyspace change. */
    int added = 0;      /* Number of new elements added. */
    int updated = 0;    /* Number of elements with updated score. */
    int processed = 0;  /* Number of elements processed, may remain zero with
                           options like XX. */

    /* Parse options. At the end 'scoreidx' is set to the argument position
     * of the score of the first score-element pair. */
    scoreidx = 2;
    
    /*
        커맨드 옵션 파싱 로직
    */

    /* Start parsing all the scores, we need to emit any syntax error
     * before executing additions to the sorted set, as the command should
     * either execute fully or nothing at all. */
    scores = zmalloc(sizeof(double)*elements);
    for (j = 0; j < elements; j++) {
        if (getDoubleFromObjectOrReply(c,c->argv[scoreidx+j*2],&scores[j],NULL)
            != C_OK) goto cleanup;
    }

    /* Lookup the key and create the sorted set if does not exist. */
    zobj = lookupKeyWrite(c->db,key);
    if (checkType(c,zobj,OBJ_ZSET)) goto cleanup;
    if (zobj == NULL) {
        if (xx) goto reply_to_client; /* No key + XX option: nothing to do. */
        zobj = zsetTypeCreate(elements, sdslen(c->argv[scoreidx+1]->ptr));
        dbAdd(c->db,key,zobj);
    } else {
        zsetTypeMaybeConvert(zobj, elements);
    }

    for (j = 0; j < elements; j++) {
        double newscore;
        score = scores[j];
        int retflags = 0;

        ele = c->argv[scoreidx+1+j*2]->ptr;
        int retval = zsetAdd(zobj, score, ele, flags, &retflags, &newscore);
        if (retval == 0) {
            addReplyError(c,nanerr);
            goto cleanup;
        }
        if (retflags & ZADD_OUT_ADDED) added++;
        if (retflags & ZADD_OUT_UPDATED) updated++;
        if (!(retflags & ZADD_OUT_NOP)) processed++;
        score = newscore;
    }
    server.dirty += (added+updated);

reply_to_client:
    if (incr) { /* ZINCRBY or INCR option. */
        if (processed)
            addReplyDouble(c,score);
        else
            addReplyNull(c);
    } else { /* ZADD. */
        addReplyLongLong(c,ch ? added+updated : added);
    }

cleanup:
    zfree(scores);
    if (added || updated) {
        signalModifiedKey(c,c->db,key);
        notifyKeyspaceEvent(NOTIFY_ZSET,
            incr ? "zincr" : "zadd", key, c->db->id);
    }
}
```


```c
// src/t_zset.c

int zsetAdd(robj *zobj, double score, sds ele, int in_flags, int *out_flags, double *newscore) {
    /* Turn options into simple to check vars. */
    int incr = (in_flags & ZADD_IN_INCR) != 0;
    int nx = (in_flags & ZADD_IN_NX) != 0;
    int xx = (in_flags & ZADD_IN_XX) != 0;
    int gt = (in_flags & ZADD_IN_GT) != 0;
    int lt = (in_flags & ZADD_IN_LT) != 0;
    *out_flags = 0; /* We'll return our response flags. */
    double curscore;

    /* NaN as input is an error regardless of all the other parameters. */
    if (isnan(score)) {
        *out_flags = ZADD_OUT_NAN;
        return 0;
    }

    /* Update the sorted set according to its encoding. */
    if (zobj->encoding == OBJ_ENCODING_LISTPACK) {
        unsigned char *eptr;

        if ((eptr = zzlFind(zobj->ptr,ele,&curscore)) != NULL) {
            /* NX? Return, same element already exists. */
            if (nx) {
                *out_flags |= ZADD_OUT_NOP;
                return 1;
            }

            /* Prepare the score for the increment if needed. */
            if (incr) {
                score += curscore;
                if (isnan(score)) {
                    *out_flags |= ZADD_OUT_NAN;
                    return 0;
                }
            }

            /* GT/LT? Only update if score is greater/less than current. */
            if ((lt && score >= curscore) || (gt && score <= curscore)) {
                *out_flags |= ZADD_OUT_NOP;
                return 1;
            }

            if (newscore) *newscore = score;

            /* Remove and re-insert when score changed. */
            if (score != curscore) {
                zobj->ptr = zzlDelete(zobj->ptr,eptr);
                zobj->ptr = zzlInsert(zobj->ptr,ele,score);
                *out_flags |= ZADD_OUT_UPDATED;
            }
            return 1;
        } else if (!xx) {
            /* check if the element is too large or the list
             * becomes too long *before* executing zzlInsert. */
            if (zzlLength(zobj->ptr)+1 > server.zset_max_listpack_entries ||
                sdslen(ele) > server.zset_max_listpack_value ||
                !lpSafeToAdd(zobj->ptr, sdslen(ele)))
            {
                zsetConvertAndExpand(zobj, OBJ_ENCODING_SKIPLIST, zsetLength(zobj) + 1);
            } else {
                zobj->ptr = zzlInsert(zobj->ptr,ele,score);
                if (newscore) *newscore = score;
                *out_flags |= ZADD_OUT_ADDED;
                return 1;
            }
        } else {
            *out_flags |= ZADD_OUT_NOP;
            return 1;
        }
    }

    /* Note that the above block handling listpack would have either returned or
     * converted the key to skiplist. */
    if (zobj->encoding == OBJ_ENCODING_SKIPLIST) {
        zset *zs = zobj->ptr;
        zskiplistNode *znode;
        dictEntry *de;

        de = dictFind(zs->dict,ele);
        if (de != NULL) {
            /* NX? Return, same element already exists. */
            if (nx) {
                *out_flags |= ZADD_OUT_NOP;
                return 1;
            }

            curscore = *(double*)dictGetVal(de);

            /* Prepare the score for the increment if needed. */
            if (incr) {
                score += curscore;
                if (isnan(score)) {
                    *out_flags |= ZADD_OUT_NAN;
                    return 0;
                }
            }

            /* GT/LT? Only update if score is greater/less than current. */
            if ((lt && score >= curscore) || (gt && score <= curscore)) {
                *out_flags |= ZADD_OUT_NOP;
                return 1;
            }

            if (newscore) *newscore = score;

            /* Remove and re-insert when score changes. */
            if (score != curscore) {
                znode = zslUpdateScore(zs->zsl,curscore,ele,score);
                /* Note that we did not removed the original element from
                 * the hash table representing the sorted set, so we just
                 * update the score. */
                dictSetVal(zs->dict, de, &znode->score); /* Update score ptr. */
                *out_flags |= ZADD_OUT_UPDATED;
            }
            return 1;
        } else if (!xx) {
            ele = sdsdup(ele);
            znode = zslInsert(zs->zsl,score,ele);
            serverAssert(dictAdd(zs->dict,ele,&znode->score) == DICT_OK);
            *out_flags |= ZADD_OUT_ADDED;
            if (newscore) *newscore = score;
            return 1;
        } else {
            *out_flags |= ZADD_OUT_NOP;
            return 1;
        }
    } else {
        serverPanic("Unknown sorted set encoding");
    }
    return 0; /* Never reached. */
}
```

위 소스코드가 `ZADD`에 대한 동작이다.  
Sorted-Set은 Set, Hash, List의 특징을 조금씩 모두 가진다.  
인덱스를 통해서 데이터에 접근해야 한다면 데이터 양에 따라서 list보다 sorted-set을 고려해볼 수 있다.  
List는 O(n)의 시간복잡도를 가지지만 Sorted-Set은 앞서 말한 것과 같이 O(log(n))의 시간복잡도를 가지기 때문이다.  


`ZADD` 커맨드를 통해서 스코어를 가지는 값을 추가할 수 있다.  
이미 값이 존재한다면 스코어만 업데이트한다.

`ZADD`는 여러 옵션을 지원한다.
- `XX`: 아이템이 존재하는 경우에만 업데이트
- `NX`: 아이템이 존재하지 않는 경우에만 신규로 저장, 기존 값을 업데이트하지 않음.
- `LT`: 업데이트하려는 스코어가 기존 스코어보다 작을 경우 업데이트. 값이 존재하지 않으면 추가.
- `GT`: 업데이트하려는 스코어가 기존 스코어보다 클 경우 업데이트. 값이 존재하지 않으면 추가.

```bash
ZADD score:1 100 value:b
(integer) 1

ZADD score:2 100 value:100 200 value:200
(integer) 2
```

`ZRANGE`는 Sorted-Set에 저장된 데이터를 조회한다.
- start/stop의 범위를 지정해야 한다.
- 기본적으로 인덱스를 기반으로 데이터를 조회한다.
- 인덱스를 벗어나면 출력하지 않는다.
- 스코어 검색 시 `-inf`, `+inf`를 사용할 수 있다.

```bash
ZRANGE key start stop [BYSCORE|BYLEX] [REV] [LIMIT offset count] [WITHSCORES]

ZRANGE score:2 0 2 WITHSCORES # WITHSCORES 옵션은 스코어도 함께 출력한다.
1) "value:100"
2) "100"
3) "value:200"
4) "200"

ZRANGE score:2 0 1 REV WITHSCORES # REV 옵션은 아이템을 역순으로 출력한다.
1) "value:200"
2) "200"
3) "value:100"
4) "100"

ZRANGE score:2 0 -1 # stop이 -1이면 start부터 끝까지 모든 인덱스를 조회한다.
1) "value:100"
2) "value:200"

ZRANGE score:2 0 -2
1) "value:100"

ZRANGE score:2 100 150 BYSCORE WITHSCORES # BYSCORE는 start/stop으로 스코어의 범위를 지정한다.
1) "value:100"
2) "100"

# ( 기호는 해당 스코어를 제외하고 탐색한다.
ZRANGE score:2 (100 200 BYSCORE WITHSCORES
1) "value:200"
2) "200"

ZRANGE score:2 100 (200 BYSCORE WITHSCORES
1) "value:100"
2) "100"

# 스코어가 같으면 사전순 정렬된다.
ZRANGE score:2 100 +inf BYSCORE WITHSCORES
1) "a:100"
2) "100"
3) "value:100"
4) "100"
5) "value:200"
6) "200"

# 사전순 정렬 조회를 위해서는 '(' 기호와 함께 사용한다.
ZRANGE score:2 (a (v BYLEX
1) "a:100"
2) "aa"
3) "ab"
4) "b"
```