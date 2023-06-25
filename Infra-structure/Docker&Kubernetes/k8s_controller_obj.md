## 컨트롤러 객체

### Kubernetes 컨트롤러 객체
- ReplicaSets 컨트롤러
- Replica 컨트롤러
- Jobs 컨트롤러
- StatefulSet
- DaemonSet
- 배포

### ReplicaSet 컨트롤러
서로 동일한 Pod 들이 모두 동시에 실행되도록 함.   
ReplicaSet 및 Pod에 선언적 업데이트를 수행하도록 함. 

### Replica 컨트롤러
복제 컨트롤러는 ReplicaSet와 배포를 조합한 것과 유사.  
이 객체의 사용은 더 이상 권장하지 않음. 

### Job 컨트롤러
Job 컨트롤러는 태스크 실행에 필요한 하나 이상의 Pod를 생성.   
태스크가 완료되면 작업이 모든 Pod를 종료.  
CronJob은 시간 기반에 따라 Pod를 실행.

### StatefulSet
로컬 상태를 유지하는 애플리케이션을 배포해야 하는 경우에 적합.  

StatefulSet는 Pod가 동일한 컨테이너 사양을 사용한다는 점에서 배포와 유사. 
- 배포를 통해 생성된 Pod에는 영구 ID가 주어지지 않음. 
- StatefulSet를 사용하여 생성된 Pod는 고유한 영구 ID와 안정적인 네트워크 ID, 영구 디스크 스토리지를 가짐.

### DaemonSet
특정 Pod를 클러스터 내의 모든 노드 또는 여러 노드에서 실행하기 위해 사용.
- DaemonSet은 특정 Pod가 모든 노드 또는 노드의 일부 하위 집합에서 항상 실행되도록 관리. 
- 새 노드가 추가되면 DaemonSet가 자동으로 해당 노드의 Pod를 필수 사양으로 설정. 
- Kubernetes 클러스터는 DaemonSet을 통해 Logging 에이전트가 클러스터 내의 모든 노드에서 실행되도록 할 수 있습니다.
    - fluentd, ...

### 배포
사용자가 필요한 만큼의 ReplicaSet를 사용해 Pod를 관리할 수 있도록 지원. 
-  Create, Update, Rollback, Extend

사용자가 배포의 순차적 업그레이드를 수행할 경우
1. 배포 객체는 두  번째 ReplicaSet를 생성.
2. 새 ReplicaSet에서 Pod의 수를 늘림. 
3. 원본 ReplicaSet의 Pod 수는 줄임.