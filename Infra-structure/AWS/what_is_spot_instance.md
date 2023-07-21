## 개요

스팟 인스턴스는 AWS 클라우드에서 미사용 중인 EC2 자원을 활용하는 인스턴스다.

온디맨드 인스턴스 대비 최대 90% 비용적 이점을 보인다.

### 자원 중심 입찰

스팟 인스턴스에 소비할 가격을 입찰할 수 있다.

- 입찰가 보다 스팟 가격이 증가하면 인스턴스가 종료된다.

### 가용 용량에 따른 인스턴스 중단

EC2 가용 용량이 부족한 경우 스팟은 2분 이내에 회수된다.

- 따라서 장애가 허용되는 내결함성 강한 컴포넌트를 동작시킬 때 유리하다.

### 오토 스케일링

EC2 오토 스케일링을 통해서 스팟 인스턴스를 확장하고 관리할 수 있다.

## 스팟 인스턴스 구분

### 스팟 플릿

인스턴스는 가격, 용량 문제 등으로 중단될 수 있다.

- 종료 2분 전 경고 공지가 발생하며 이에 따라 상태를 모니터링해야 한다.
- 이를 통해 인스턴스 종료에 대비한 중요 데이터 등을 별도로 저장할 수 있도록 한다.

### 스팟 블록

특정 시간 (1~6h) 동안 인스턴스를 사용한다.

### 스팟 집합

스팟 인스턴스가 가격이나 용량 변경에 영향을 받아 중단될 경우?

- 목표 용량 집합 유지를 시도한다.

Lowest Price (최저 가격 전략)

- 최저 가격 풀에서 인스턴스를 가져와 사용한다. (default)
- 최저가 입찰이 가능하다.

Diversified (다각화)

- 모든 풀에 분산해서 인스턴스를 가져와 사용한다.
- 가용성, 하나의 풀의 가격 상승에 대해 장점을 가진다.
- 온디맨드 가격보다 높은 가격 풀에서는 시작하지 않는다.

## 생성 예시

### EC2

![스팟 인스턴스.png](./static/spot1.png)

### EC2 오토 스케일링 그룹

## 관련 자료

https://aws.amazon.com/ko/ec2/spot/

[https://tech.scatterlab.co.kr/spot-karpenter/#:~:text=🤔,이내에 인스턴스가 회수돼요](https://tech.scatterlab.co.kr/spot-karpenter/#:~:text=%F0%9F%A4%94,%EC%9D%B4%EB%82%B4%EC%97%90%20%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4%EA%B0%80%20%ED%9A%8C%EC%88%98%EB%8F%BC%EC%9A%94).

https://aws.amazon.com/ko/blogs/korea/new-resource-oriented-bidding-for-ec2-spot-instances/

[https://aws.amazon.com/ko/blogs/korea/powering-your-amazon-ecs-cluster-with-amazon-ec2-spot-instances/#:~:text=스팟 인스턴스에서 실행되는 ECS 클러스터 만들기](https://aws.amazon.com/ko/blogs/korea/powering-your-amazon-ecs-cluster-with-amazon-ec2-spot-instances/#:~:text=%EC%8A%A4%ED%8C%9F%20%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4%EC%97%90%EC%84%9C%20%EC%8B%A4%ED%96%89%EB%90%98%EB%8A%94%20ECS%20%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0%20%EB%A7%8C%EB%93%A4%EA%B8%B0)

https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/using-spot-instances.html
