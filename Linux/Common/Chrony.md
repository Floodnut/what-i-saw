### Chrony

**Chrony란?**

- chrony는 NTP로 구현한 서버 네트워크 시간 동기화 서비스
- 시스템 클럭을 NTP 서버와 동기화할 수 있다.

```bash
apt install chrony
```

`/etc/chrony/chrony.conf`

```bash
## chrony 설정파일 경로
confdir /etc/chrony/conf.d

## server NTP_SERVER iburst
pool ntp.ubuntu.com        iburst maxsources 4
pool 0.ubuntu.pool.ntp.org iburst maxsources 1
pool 1.ubuntu.pool.ntp.org iburst maxsources 1
pool 2.ubuntu.pool.ntp.org iburst maxsources 2

## DHCP 시간 출처
sourcedir /run/chrony-dhcp

## NTP 출처 저장 경로
sourcedir /etc/chrony/sources.d
## server 192.0.2.1 iburst

## NTP 인증 키(쌍) 위치
keyfile /etc/chrony/chrony.keys

## chronyd의 rate
## 주파수 편차의 단위 - PPM(Parts per million)
## rate : 동기화 기준 클럭 주파수 대비 현재 시스템이 가지는 주파수 편차를 나타낸다. (100만 클럭 당)
driftfile /var/lib/chrony/chrony.drift

## NTS 키, 쿠키 저장
ntsdumpdir /var/lib/chrony

## 로그 활성화 옵션
log tracking measurements statistics

# 로그파일 저장 위치
logdir /var/log/chrony

# chrony가 시스템 시계의 업데이트를 위한 시간(클럭) 차이를 100.0 ppm으로 제한
maxupdateskew 100.0

## 11분마다 커널 동기화를 실행함
rtcsync

## makestep a b
## 시간차가 b회 동안 업데이트가 없고 조정 값이 a초보다 클 경우, 강제 동기화 
makestep 1 3

leapsectz right/UTC
```

타임서버 설정

```bash
# server NTP_SERVER iburst
pool ntp.ubuntu.com        iburst maxsources 4
pool 0.ubuntu.pool.ntp.org iburst maxsources 1
pool 1.ubuntu.pool.ntp.org iburst maxsources 1
pool 2.ubuntu.pool.ntp.org iburst maxsources 2
```

`server <NTP_SERVER> <옵션>` 형태로 구성파일에 등록

- NTP_SERVER: ip, 호스트 명이 될 수 있다.

옵션

- `burst`
    - private NTP 서버를 대상으로 사용
    - 서버로부터 시간정보를 가져올 때마다 8개의 패킷을 보냄
    - 기본 값은 1개의 패킷
- `iburst`
    - NTP서버에서 unreachable가 발생하면 8개의 패킷을 보냄
    - 기본 값은 1개의 패킷
    - `calldelay`를 통해서 요청의 간격을 설정할 수 있다.
- `minpoll` / `maxpoll`
- `prefer`
    - NTP 서버의 우선순위를 지정

### NTP(Network Time Protocol)

**NTP란?**

- 네트워크 환경의 시스템들 간의 시간 동기화를 위한 프로토콜
- UDP 기반으로 동작한다.

**동작 방식**

- 브로드캐스팅 방식으로 시간 정보를 전달한다.
- 서버-클라이언트 계층 표현을 위해서 Stratum을 사용한다.
- Stratum
    - 계층적 토폴로지 구조로 이루어져 있으며 계층이 존재한다.
    - 최상위 계층은 Stratum 0이다. `(원자 시계)`
    - 마찬가지로 하위 계층은 1, 2, 3… 으로 존재한다.
- 교차 알고리즘을 통해서 타임서버를 선택하고 네트워크 지연시간의 영향을 줄인다.


**NTP 타임서버 상태 확인**

```bash
chronyc sourcestats -v
                             .- Number of sample points in measurement set.
                            /    .- Number of residual runs with same sign.
                           |    /    .- Length of measurement set (time).
                           |   |    /      .- Est. clock freq error (ppm).
                           |   |   |      /           .- Est. error in freq.
                           |   |   |     |           /         .- Est. offset.
                           |   |   |     |          |          |   On the -.
                           |   |   |     |          |          |   samples. \
                           |   |   |     |          |          |             |
Name/IP Address            NP  NR  Span  Frequency  Freq Skew  Offset  Std Dev
==============================================================================
pugot.canonical.com        30  14  499m     +0.003      0.030  +3217us   395us
prod-ntp-3.ntp4.ps5.cano>  27  13  447m     +0.032      0.132  +1028us  1592us
prod-ntp-5.ntp1.ps5.cano>  37  23   10h     +0.002      0.112   +820us  2061us
alphyn.canonical.com       41  23   12h     +0.044      0.036   -691us   840us
...
```

**NTP의 장점**

- 데이터 손실 방지
    - 서로 다른 시스템에서 파일을 수정할 때 시간 동기화가 되지 않으면 손실이나 오류가 발생할 수 있다. (?)
- 로그 분석의 용이성-신뢰성 상승
    - 시간 동기화가 되지 않는 시스템의 로그를 신뢰할 수 있는가?
- 예약된 작업이 정상적으로 동작하게 함
    - 배치 작업이나 백업 등이 발생할 때 시스템 간 작업의 오류를 완화한다.

**NTP의 단점**

- 서버-클라이언트 간 연결이 동기화에 필수적임.
- 외부 NTP 서버를 참조할 경우 연결 과정에서 보안상 취약점이 발생할 수 있다.
    - `크립토-NAK` 라는 패킷을 다루는 경우, 네트워크 상 시간을 변경해 인증을 우회할 수 있다.
    - 이로 인해 DDoS, 메모리 오염이 발생할 수 있다.
- 따라서, 외부 NTP 서버를 직접 참조하지 않도록 별도의 타임서버를 구축하는 경우가 있다.

### 참고

[Network Time Protocol](https://en.wikipedia.org/wiki/Network_Time_Protocol)

[chrony – Introduction](https://chrony.tuxfamily.org/)

[ntp 보안 취약점](https://zdnet.co.kr/view/?no=20151023110205)