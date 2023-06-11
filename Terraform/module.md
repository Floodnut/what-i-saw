## 모듈
Terraform 코드를 재사용 가능하게 만들어준다.  
아래와 같이 저장소를 활용하거나 로컬 경로에서 모듈을 불러올 수 있다.  
원격 저장소를 활용하는 경우 `terraform get`으로 먼저 모듈을 불러오자.

```go
module "example" {
    source = "github.com/user/modules"
}

module "example2" {
    source = "./modules"
}
```

`output` 을 통해서 코드의 일부를 모듈 출력으로 사용할 수 있다.

```go
output "output-example" {
    value = "${module.example2.<...>}"
}
```