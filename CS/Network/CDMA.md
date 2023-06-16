## CDMA, Code Division Multiple Access

### CDMA 란?
고유 코드가 각 유저에게 할당되고 그 코드로 파티셔닝을 결정한다.
- 모든 유저는 동일한 주파수 대역을 공유한다.
- 각 유저는 각각의 데이터 인코딩을 위한 Chipping Sequence(ex : 코드)를 가진다.
- 적은 간섭으로 여러 유저가 동시에 접속하고 전송하게 한다. (코드가 직교한다면)

채널 파티셔닝
- 이동 통신에서는 Channel을 사용하에서 인원을 제한하고 품질을 보장한다.
- taking turn, random access 등은 문제가 있음

### CDMA 인코딩, 디코딩
인코딩 
- 인코딩 출력 = `원본 데이터(Data-bits)` x `Chipping Seq`

디코딩
- inner-product of `encoded signal` and `chipping seq`
- 인코딩 신호와 Chipping Seq의 내적

Two-sender interference
- 두 명 이상의 송신자가 있을 경우를 가정한다.
- 인코딩 출력을 합하여 채널 출력으로 전달한다.