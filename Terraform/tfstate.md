## tfstate

테라폼은 `terraform.tfstate` 를 통해서 인프라의 원격 상태를 유지한다.
이전 상태는 `terraform.tfstate.backup`에 저장된다.

`apply`를 수행하면 새로운 `tfstate`가 생성되고 이전 상태는 `backup`에 저장된다.
이를 통해서 테라폼이 원격 상태를 추적한다.
원격 상태가 변경되었을때 `apply`를 수행하면 테라폼이 기존의 원격 상태를 유지시킨다.


### tfstate의 관리

`tfstate`는 히스토리를 통해 버전을 관리할 수 있다.  
`tfstate`를 로컬 백엔드가 아닌 원격 백엔드의 저장소에서 관리할 수 있다.

- Git 
- Terraform backend
- S3 (+ Lock 사용이 가능한 AWS DynamoDB)
- Consul
- etc

원격 저장소에서 관리할 때 Lock을 지원하는 저장소를 통해서 충돌이 발생하지 않도록 한다. 

```
terraform {
    backend "consul" {
        address = "" # 저장소 호스트 명
        path = "terraform/project"
    }
}
```
```
terraform {
    backend "s3" {
        bucket = "" # s3 버킷명
        key = "terraform/project"
        region = ""
    }
}
```

`terraform` 블록의 백엔드를 지정할 때 변수를 사용할 수 없다.
```
│ Error: Variables not allowed
│ 
│   on backend.tf line 5, in terraform:
│    5:         region = var.aws_region
│ 
│ Variables may not be used here.
```