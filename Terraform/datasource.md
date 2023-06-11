## Data sources

AWS와 같은 특정 CSP에 대해 테라폼이 데이터 소스라는 동적 정보를 제공한다.
이를 API를 통해서 사용할 수 있다.

AMI나 가용영역(AZ), IP 주소 등에 대한 정보는 동적으로 변할 수 있으므로 사용자가 직접 입력하지 않고 이를 사용할 수 있다.

```go
data "aws_ip_ranges" "northeast_ec2" {
  regions  = ["ap-northeast-2"]
  services = ["ec2"]
}
```