## 함수를 안전하고 간결하게 작성하기



### SOLID

- SPR
  - 한 클래스는 하나의 책임만 가져야 한다
- OCP
  - 소프트웨어 요소는 확장에는 열려 있으나 변경에는 닫혀 있어야 한다
  - 객체지향의 추상화와 다형성을 활용
- LSP
  - 서브 타입은 언제나 기반 타입으로 교체할 수 있어야 한다
  - 자식 클래스가 부모 클래스의 역할을 할 수 있어야함
- ISP
  - 자신이 사용하지 않는 인터페이스는 구현하지 말아야 한다
  - 기능별로 인터페이스를 분리해서 필요한 기능만 구현한다
  - 인터페이스를 뚱뚱하게 만들지 말고 나눠서 만들자
  - SRP가 클래스의 단일 책임이라면, ISP는 인터페이스의 단일 책임
- DIP
  - 상위 모델은 하위 모델에 의존하면 안된다. 둘 다 추상화에 의존해야 한다. 추상화는 세부 사항에 의존해서는 안된다. 세부 사항은 추상화에 따라 달라진다

```java
class PaymentController {
    @RequestMapping(value = "/api/payment", method = RequestMethod.POST)
    public void pay(@RequestBody ShinhanCardDto.PaymentRequest req) {
        shinhanCardPaymentService.pay(req);
    }
}

class ShinhanCardPaymentService {
    public void pay(ShinhanCardDto.paymentRequest req) {
        shinhanCardApi.pay(req);
    }
}

// 새로운 카드가 추가된다면?

// 확장에 유연하진 않다
@RequestMapping(value = "/api/payment", method = RequestMethod.POST)
public void pay(@RequestBody CardPaymentDto.PaymentRequest req) {
    if(req.getType() == CardType.SHINHAN) {
        shinhanCardPaymentService.pay(req);
    } else if(req.getType() == CardType.WOORI) {
        wooriCardPaymentService.pay(req);
    }
}

// 추상화된 인터페이스에 의존하도록 한다

class PaymentController {
    @RequestMapping(value = "/api/payment", method = RequestMethod.POST)
    public void pay(@RequestBody CardPaymentDto.PaymentRequest req) {
        final CardPaymentService cardPaymentService =
            cardPaymentFactory.getType(req.getType());
        cardPaymentService.pay(req);
    }
}

public interface CardPaymentService {
    void pay(CardPaymentDto.PaymentRequest req);
}

public class ShinhanCardPaymentService implements CardPaymentService {
    @Override
    public void pay(CardPaymentDto.PaymentRequest req) {
        shinhanCardApi.pay(req);
    }
}
```



### 간결한 함수 작성하기

```java
 public static String renderPageWithSetupsAndTeardowns(PageData pageData, boolean isSuite) throws Exception {
        
     boolean isTestPage = pageData.hasAtributte("Test");
     
     if(isTestPage) {
        WikiPage testPage = pageData.getWikiPage();
        StringBuffer newPageContent = new StringBuffer();
        includeSetupPages(testPage, newPageContent, isSuite);
        newPageContent.append(pageData.getContent());
        includeTeardownPages(testPage, newPageContent, isSuite);
        pageData.setContent(newPageContent.toString());
     }
     return pageData.getHtml();
 }
```

함수가 길고, 여러가지 기능이 섞여있다...



작게 쪼갠다. 함수 내 추상화 수준을 동일하게 맞춘다.

```java
 public static String renderPageWithSetupsAndTearDowns(PageData pageData, boolean isSuite) throws Exception {

   if(isTestPage(pageData)) {
      includeSetupAndTeardownPages(pageData, isSuite);
       return pageData.getHtml();
    }
 }
```



한가지만 하기 (SRP), 변경에 닫게 만들기(OCP)

```java
public Money calculatePay(Employee employee) throws Exception {

     switch (employee.type) {
        case COMMISSIONED:
            calculateCommissionedPay(employee);
        case HOURLY:
            calculateHourlyPay(employee);
        case SALARIED:
            calculateSalariedPay(employee);
        default:
            throw new Exception(String.valueOf(employee.type));
    }
}
```

계산도 하고, Money도 생성한다... 두 가지 기능이 보임. 새로운 직원 타입이 추가 된다면?



계산과 타입 관리를 분리

타입에 대한 처리는 최대한 Factory에서만

```java
public abstract class Employee {
    public abstract boolean isPayday();
    public abstract Money calculatePay();
    public abstract void deliverPay(Money pay);
}

public interface EmployeeFactory {
        public Employee makeEmployee(EmployeeRecord record) throws Exception;
    }

public class EmployeeFactoryImpl implements EmployeeFactory {

    @Override
    public Employee makeEmployee(EmployeeRecord record) throws Exception {
        switch (record.type) {
            case COMMISSIONED:
                return new CommissionedEmployee(record);
            case HOURLY:
                return new HourlyEmployee(record);
            case SALARIED:
                return new HourlEmployee(record);
            default:
                throw new Exception("Error");
        }
    }
}
```



### 함수 인수

- 인수의 갯수는 0~2개가 적당
- 3개 이상인 경우에는?
  - 객체를 인자로 넘기기
  - 가변 인자를 넘기기 (잘 사용하지 않음)



### 안전한 함수 작성하기

부수 효과 없는 함수

- 값을 반환하는 함수가 외부 상태를 변경하는 경우



### 함수 리팩터링

순서

- 기능을 구현하는 서투른 함수를 작성한다
  - 길고 복잡하고 중복도 있다
- 테스트 코드를 작성한다
  - 함수 내부의 분기와 엣지값마다 빠짐없이 테스트하는 코드를 짠다
- 리팩터링 한다
  - 코드를 다듬고 함수를 쪼개고 이름을 바꾸고 중복을 제거한다