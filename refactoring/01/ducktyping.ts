// Javascript/Typescript 는 클래스 내부의 프로퍼티나 메서드가 동일하면 같은 타입으로 간주한다.
// 이를 Duck Typing 이라고 한다.

interface IDuckTyping {
  property1: number;
  method1(): void;
}

class DuckTyping implements IDuckTyping {
  property1: number;

  method1() {
    console.log("method1");
  }
}

class DuckTyping2 {
  property1: number;

  method1() {
    console.log("method1");
  }
}
