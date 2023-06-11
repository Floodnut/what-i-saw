# 연관 관계

### 양방향 연관 관계
```java
// Member.java
@ManyToOne
@JoinColumn(name = "TEAM_ID")
private Team team;

// Team.java
@OneToMany(mappedBy = "team")
private List<Member> members = new ArrayList<>();
```

우리는 위와 같이  `Member`와 `Team`에 일대다 관계를 양방향으로 선언했다.
그렇다면 어느 객체가 양방향 관계의 주인으로 관리할 수 있는지 확인해야 한다.

```java
team.getMembers().add(member);
```

현재는 FK를 가지는 `Member` 테이블 객체를 양방향 관계의 주인으로 설정했다.
그런데 `Team`의 `Member` 리스트 객체에 값을 넣으면 어떻게 될까?

```bash
Hibernate:
    /* insert jpastudy.association.Team
        */ insert
    into
        Team
        (name, TEAM_ID)
    values
      (?, ?)
Hibernate:
    /* insert jpastudy.association.Member
      */ insert
    into
      Member
      (TEAM_ID, USERNAME, id)
    values
      (?, ?, ?)
```

`Member`, `Team` 생성 쿼리는 두 개가 발생하더라도 `Member`가 관리하는 `Team` FK는 NULL 값이 삽입된다.  
그러니 주인과 주인이 아닌 엔터티 모두 값을 설정해야 한다.

그렇다면 주인이 아닌 속성에 값을 추가해야 하는 이유는 무엇일까?  
영속성 컨텍스트를 초기화하지 않는 경우 1차 캐시에 값이 남아있고 지연로딩이 발생하지 않는다.  

즉, 주인 엔티티는 값을 가지고 있으나 주인이 아닌 엔티티는 값을 가지고 있지 않는다.  
객체지향 관점에서 역방향 탐색하더라도 같은 결과를 주지 않는다는 뜻이다.  

이는 테스트 코드 작성 등에서도 문제를 발생시킬 수 있다.