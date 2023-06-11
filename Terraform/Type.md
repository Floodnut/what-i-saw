## 변수 타입

Terraform이 자동으로 타입을 할당할 수도 있지만 명시적으로 지정할 수도 있다.

```go
/* main.tf */
variable "myvar" { //terraform plan, apply 없이 테스트 할 수 있음.
  //type = "string" //deprecated
  type = string
  default = "hello terraform"
}

variable "mymap" { //terraform plan, apply 없이 테스트 할 수 있음.
  type = map(string)
  default = {
    mykey = "value"
  }
}

variable "mylist"{
    type = list
    default = [1,2,3]
}
```

`type` 으로 지정할 수 있는 기본 타입은 다음과 같다.

- string
- number
- bool

`type` 으로 지정할 수 있는 복합 타입은 다음과 같다.

- List
    - `[ … ]` 형태
    - ordered
    - 각 원소가 모두 같은 타입을 가진다.
- Set
    - `[ … ]` 형태
    - unordered & unque
    - 출력 시 정렬함.
- Map
    - `{ “key” = “value” }` 형태
    - 모든 속성이 같은 타입을 가진다.
- Object
    - `{ “key” = “value”, … }` 형태
    - 각 속성이 서로 다른 타입을 가질 수 있다.
- Tuple
    - `[ … ]` 형태
    - 각 원소가 서로 다른 타입을 가질 수 있다.