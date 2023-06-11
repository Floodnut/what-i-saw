## 조건문 (`if-else`)
```go
Condition ? <True> : <False>
```
삼항연산자의 형태로 사용한다. 

```go
resource "aws_instance" "example" {
    ...
    count = "$(var.env == "prod") ? 2 : 1"
} 
```

위의 예시에서 개발 환경, 운영 환경을 나누고 운영 환경에서 사용되는 인스턴스 수를 늘리는 용도로 사용할 수 있다.  

사용할 수 있는 연산자는 다음과 같다.  
- `==`, `!=`, `>`, `<`, `>=`, `<=`, `&&`, `||`, `!`

## 환경변수 전달
```go
variable "ENV" {
  default = "prod"
}
```
위와 같은 변수의 값을 통해서 개발 환경, 운영 환경을 구분한다고 가정하자.

```
terraform apply -var ENV=dev
```
이때 환경 변경을 위해서 `apply` 시점에서 `-var` 옵션으로 환경변수를 전달할 수 있다.