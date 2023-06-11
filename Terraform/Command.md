## 명령

`terraform console`
- `terraform` 콘솔을 사용할 수 있다.

`terraform init`
- provider를 초기화하고 플러그인을 다운로드 한다.

`terraform plan`
- 실제 인프라에 테라폼 파일을 적용하지 않고도 사전 계획을 확인할 수 있다.
- `terraform plan -out <out.terraform>` 을 통해 출력값을 확인하고 이용할 수 있다.

`terraform apply`
- 테라폼 파일을 실제 인프라에 반영함 (상태를 적용)
- `terraform apply out.terraform` 으로 이전 `plan` 단계에서 출력한 값 만을 반영할 수도 있다.
- `plan` 단계를 거치지 않는 것이 분명히 빠르다.
- 하지만 실제 프로덕션 단계에서는 `plan` 을 통한 검증을 꼭 수행하자.

`terraform destroy`
- 프로덕션 환경에서 `destroy` 를 사용하면 전체 인프라를 삭제할 수 있으니 사용하지 않도록 주의하기.

`terraform fmt`
- 테라폼 구성 파일을 표준 형식으로 재 작성한다.
- 인프라 변경사항을 적용하기 전 형식이 올바른지 확인하기 위해 사용한다.

`terraform get`
- 원격 저장소 등에 존재하는 모듈을 다운로드하거나 업데이트할 때 사용한다.

`terraform graph`
- 설정이나 실행 계획을 시각적으로 표현할 수 있다.
```
terraform graph
digraph {
        compound = "true"
        newrank = "true"
        subgraph "root" {
                "[root] aws_instance.example (expand)" [label = "aws_instance.example", shape = "box"]
                "[root] provider[\"registry.terraform.io/hashicorp/aws\"]" [label = "provider[\"registry.terraform.io/hashicorp/aws\"]", shape = "diamond"]
                "[root] var.AWS_ACCESS_KEY" [label = "var.AWS_ACCESS_KEY", shape = "note"]
                "[root] var.AWS_AMIS" [label = "var.AWS_AMIS", shape = "note"]
                "[root] var.AWS_REGION" [label = "var.AWS_REGION", shape = "note"]
                "[root] var.AWS_SECRET_KEY" [label = "var.AWS_SECRET_KEY", shape = "note"]
                "[root] var.aws_deployment_role" [label = "var.aws_deployment_role", shape = "note"]
                "[root] var.mylist" [label = "var.mylist", shape = "note"]
                "[root] var.mymap" [label = "var.mymap", shape = "note"]
                "[root] var.myvar" [label = "var.myvar", shape = "note"]
                "[root] aws_instance.example (expand)" -> "[root] provider[\"registry.terraform.io/hashicorp/aws\"]"
                "[root] aws_instance.example (expand)" -> "[root] var.AWS_AMIS"
                "[root] output.example_instance (expand)" -> "[root] aws_instance.example (expand)"
                "[root] provider[\"registry.terraform.io/hashicorp/aws\"] (close)" -> "[root] aws_instance.example (expand)"
                "[root] provider[\"registry.terraform.io/hashicorp/aws\"]" -> "[root] var.AWS_ACCESS_KEY"
                "[root] provider[\"registry.terraform.io/hashicorp/aws\"]" -> "[root] var.AWS_REGION"
                "[root] provider[\"registry.terraform.io/hashicorp/aws\"]" -> "[root] var.AWS_SECRET_KEY"
                "[root] root" -> "[root] output.example_instance (expand)"
                "[root] root" -> "[root] provider[\"registry.terraform.io/hashicorp/aws\"] (close)"
                "[root] root" -> "[root] var.aws_deployment_role"
                "[root] root" -> "[root] var.mylist"
                "[root] root" -> "[root] var.mymap"
                "[root] root" -> "[root] var.myvar"
        }
}
```

`terraform import [options] address id` (address: 리소스가 정의될 주소)
- 'id'로 식별된 인프라 리소스를 찾고 그 주소를 `terraform.state`로 불러온다.
- 실행 중인 기존 인스턴스가 있지만 테라폼에 작성되지 않은 경우 이 명령을 통해 state로 불러올 수 있다.
- 리소스를 수동으로 정의해야 하는 단점이 있다.

`terraform push`
- 중앙 집중형 서버에서 테라폼을 자동으로 수행할 수 있다.
- 아틀라스라는 엔터프라이즈 도구를 사용한다.

`terraform refresh`
- 테라폼 상태 파일과 인프라 원격 상태를 식별하고 상태를 확인한다.

`terraform remote`
- S3 등 원격 상태 저장소를 구성한다.

`terraform show`
- 사람이 읽을 수 있는 출력을 상태나 계획에서 불러와 보여준다.

`terraform state`
- 상태 관리를 할 수 있다.
- 리소스 명 변경 등을 수행할 수 있다.

`terraform taint`
- 문제가 있는 리소스를 수동으로 표시하고 다음 적용 시 파괴 후 재생성한다.

`terraform untaint`
- `taint` 명령을 취소한다.
- 인프라 변경이 적용되지 않는다.

`terraform validate`
- 테라폼 문법을 검증한다.

