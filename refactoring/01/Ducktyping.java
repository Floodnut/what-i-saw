// Java는 타입을 클래스 명으로 선언한다.
// 내부 프로퍼티나 메서드가 동일하더라도 클래스가 다르면 다른 타입으로 인식한다.

public class Ducktyping {

  private int property1;

  public void method1() {
    System.out.println("method1");
  }
}

public class Ducktyping2 {

  private int property1;

  public void method1() {
    System.out.println("method1");
  }
}
