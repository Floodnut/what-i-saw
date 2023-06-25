## GCP 웹 콘솔
- GCP 자원에 대해 웹 대시보드에서 터미널로 관리할 수 있다.
- 터미널, 웹 IDE를 지원한다.
- 터미널에 연결된 인스턴스로 파일 업로드/다운로드 가능

### gcloud CLI
- Google Cloud CLI는 Google Cloud 리소스를 관리하기 위한 도구 모음
- Compute Engine과 Google Kubernetes Engine(GKE), 여러 Google Cloud 서비스 작업에 사용


영역(zone) 목록 확인하기
```bash
gcloud compute zones list
```

구성 값 설정하기
```bash
# 영역 설정
gcloud config set compute/zone $ZONE
## Updated property [compute/zone].
```

GCP가 지원하는 이미지 목록 확인
```bash
gcloud compute images list

## NAME                    PROJECT         FAMILY      DEPRECATED  STATUS
## centos-6-v20160718      centos-cloud    centos-6                READY
## ...
```

vm 인스턴스 생성하기
```bash
gcloud compute instances create $VMNAME \
    --machine-type "e2-standard-2" \  # 머신 타입
    --image-project "debian-cloud" \  # 이미지 프로젝트
    --image-family "debian-11" \      # 이미지 패밀리
    --subnet "default"                # 서브넷 설정

## Created [https://www.googleapis.com/compute/v1/projects/##__프로젝트_id__/zones/__영역__/instances/__VM명__].
## NAME: __VM명__
## ZONE: 영역 (us-central1-c 깉은 AZ)
## MACHINE_TYPE: e2-standard-2
## PREEMPTIBLE: 
## INTERNAL_IP: 내부 사설 ip
## EXTERNAL_IP: 외부 공공 ip
## STATUS: RUNNING
```

### gsutil
- gsutil은 명령줄에서 Cloud Storage에 액세스하는 데 사용할 수 있는 Python 애플리케이션
- https://cloud.google.com/storage/docs/gsutil?hl=ko


버킷 생성하기
```bash
UNIQUE_BUCKET_NAME=unique_bucket_name #(소문자여야 함)
gsutil mb gs://$UNIQUE_BUCKET_NAME

## Creating gs://bucket_global_2__aafdsfasdf/...
```

