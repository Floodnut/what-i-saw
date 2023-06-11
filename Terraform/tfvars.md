## tfvars로 변수 넘기기

특정 비밀 값이나 변수를 별도로 관리하기 위해서 `tfvars` 파일을 이용한다.

`variable=value` 형태로 변수를 저장하며 이 값을 테라폼의 변수 블록에서 끌어다 사용한다.

해당 파일은 `.gitignore` 에 추가하고 저장소에 업로드하지 않도록 주의한다.

```go
// variables.tf

variable "AWS_ACCESS_KEY" {}

variable "AWS_SECRET_KEY" {}

variable "AWS_REGION" {}
```

```go
// terraform.tfvars

AWS_ACCESS_KEY = ""
AWS_SECRET_KEY= ""
AWS_REGION="ap-northeast-2"
```