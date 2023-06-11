## JPA란?
Java App과 JDBC 사이에서 동작하는 인터페이스.  
구현체로 Hibernate를 사용할 수 있다.

### EntityManagerFactory
- 로딩 시점에 하나만 생성한다.

### EntityManager
- 매 요청마다 불러와서 트랜잭션 단위로 동작 후 닫아야함.
- 스레드 밖으로 공유하지 말기

### 트랜잭션 단위
- JPA는 엔티티 매니저에서 트랜잭션을 불러와 트랜잭션 단위로 수행함.
- 한 DB 접근이 `commit()`을 통해 트랜잭션을 닫거나 `rollback()`.
- 한 요청이 끝나면 `close()`를 통해 `EntityManager`와 `EntityManagerFactory`를 닫아야 함.

### @Entity
- `@Entity` 어노테이션을 엔티티 객체에 지정하면서 JPA가 관리할 수 있게 한다.

### CRUD
- 생성/조회/삭제는 각각 `persist()`/`find()`/`remove()`를 통해 동작.
- 수정은 불러온 객체의 속성 값을 변경하는 것만으로도 적용할 수 있다.


