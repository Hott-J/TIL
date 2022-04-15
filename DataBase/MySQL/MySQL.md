# MySQL



## 데이터베이스는 뭐고 MySQL은 뭔가요?

**가장 널리 쓰이는 관계형 데이터베이스**



**데이터베이스**

- 정보의 집합 저장소
- DBMS
  - 데이터베이스 관리형 시스템
- Sql
  - 데이터를 관리

- RDBMS
  - 컬럼들을 나눠 관계를 맺음
    - join을 이용해 분리된 테이블들을 연결하여 한 테이블에서 본 것처럼 조회할 수 있음
  - 데이터 중복 제거를 위함



*실습사이트*

- https://www.w3schools.com/mysql/trymysql.asp?filename=trysql_select_all



## SELECT

**테이블의 모든 내용 보기**

```sql
SELECT * FROM Customers;
-- 이와 같이 주석을 달 수 있습니다.
```



**원하는 column만 골라서 보기**

```sql
SELECT CustomerName FROM Customers;

SELECT CustomerName, ContactName, Country
FROM Customers;

-- 테이블의 컬럼이 아닌 값도 선택할 수 있다
SELECT
  CustomerName, 1, 'Hello', NULL
FROM Customers;
```



**원하는 조건의 row만 걸러서 보기**

```sql
SELECT * FROM Orders
WHERE EmployeeID = 3;

SELECT * FROM OrderDetails 
WHERE Quantity < 5;
```



**원하는 순서로 데이터 가져오기**

```sql
SELECT * FROM Customers
ORDER BY ContactName;

SELECT * FROM OrderDetails
ORDER BY ProductID ASC, Quantity DESC;
```



**원하는 만큼만 데이터 가져오기**

```sql
SELECT * FROM Customers
LIMIT 10;

SELECT * FROM Customers
LIMIT 0, 10;

-- 30번째 부터 10개
-- 페이징
SELECT * FROM Customers
LIMIT 30, 10;
```



**원하는 별명으로 데이터 가져오기**

```sql
SELECT
  CustomerId AS ID,
  CustomerName AS NAME,
  Address AS ADDR
FROM Customers;

SELECT
  CustomerId AS '아이디',
  CustomerName AS '고객명',
  Address AS '주소'
FROM Customers;
```



**활용**

```sql
SELECT
  CustomerID AS '아이디',
  CustomerName AS '고객명',
  City AS '도시',
  Country AS '국가'
FROM Customers
WHERE
  City = 'London' OR Country = 'Mexico'
ORDER BY CustomerName
LIMIT 0, 5;
```



## 각종 연산자들

![image](https://user-images.githubusercontent.com/47052106/163506693-4e512cb2-10fe-4a7d-9cb0-03854e9a5f44.png)



**사칙연산**

```sql
SELECT 1 + 2;
SELECT 5 - 2.5 AS DIFFERENCE;
SELECT 3 * (2 + 4) / 2, 'Hello';
SELECT 10 % 3;

-- 문자열에 사칙연산을 가하면 0으로 인식
SELECT 'ABC' + 3;
SELECT 'ABC' * 3;
SELECT '1' + '002' * 3;
-- 숫자로 구성된 문자열은 숫자로 자동인식

SELECT
  OrderID + ProductID
FROM OrderDetails;

SELECT
  ProductName,
  Price / 2 AS HalfPrice
FROM Products;
```



**참/거짓 관련 연산자**

```sql
SELECT TRUE, FALSE;
SELECT !TRUE, NOT 1, !FALSE, NOT FALSE;

-- MySQL에서는 TRUE는 1, FALSE는 0으로 저장됩니다
SELECT 0 = TRUE, 1 = TRUE, 0 = FALSE, 1 = FALSE;
SELECT * FROM Customers WHERE TRUE;
SELECT * FROM Customers WHERE FALSE;

SELECT TRUE IS TRUE;
SELECT TRUE IS NOT FALSE;
SELECT (TRUE IS FALSE) IS NOT TRUE;

SELECT TRUE AND FALSE, TRUE OR FALSE;
SELECT 2 + 3 = 6 OR 2 * 3 = 6;

SELECT * FROM Orders
WHERE
  CustomerId = 15 AND EmployeeId = 4;
  
SELECT * FROM Products 
WHERE
  ProductName = 'Tofu' OR CategoryId = 8;
  
SELECT * FROM OrderDetails
WHERE
  ProductId = 20
  AND (OrderId = 10514 OR Quantity = 50);
  
SELECT 1 = 1, !(1 <> 1), NOT (1 < 2), 1 > 0 IS NOT FALSE;
SELECT 'A' = 'A', 'A' != 'B', 'A' < 'B', 'A' > 'B';
SELECT 'Apple' > 'Banana' OR 1 < 2 IS TRUE;
  
-- MySQL의 기본 사칙연산자는 대소문자 구분을 하지 않습니다.
SELECT 'A' = 'a';

SELECT
  ProductName, Price,
  Price > 20 AS EXPENSIVE 
FROM Products;

-- 테이블의 컬럼이 아닌 값으로 선택하기
SELECT
  ProductName, Price,
  NOT Price > 20 AS CHEAP 
FROM Products;

SELECT 5 BETWEEN 1 AND 10;
SELECT 'banana' NOT BETWEEN 'Apple' AND 'camera';

SELECT * FROM OrderDetails
WHERE ProductID BETWEEN 1 AND 4;

SELECT * FROM Customers
WHERE CustomerName BETWEEN 'b' AND 'c';

SELECT 1 + 2 IN (2, 3, 4) 
SELECT 'Hello' IN (1, TRUE, 'hello') 
SELECT * FROM Customers
WHERE City IN ('Torino', 'Paris', 'Portland', 'Madrid') 

SELECT
  'HELLO' LIKE 'hel%', -- hel뒤에 무엇이든 온다
  'HELLO' LIKE 'H%',
  'HELLO' LIKE 'H%O',
  'HELLO' LIKE '%O',
  'HELLO' LIKE '%HELLO%', -- %는 공백이 와도 된다
  'HELLO' LIKE '%H', -- H로 끝
  'HELLO' LIKE 'L%' -- L로 시작
  
SELECT
  'HELLO' LIKE 'HEL__', -- HEL 뒤에 2글자만 와야한다
  'HELLO' LIKE 'h___O',
  'HELLO' LIKE 'HE_LO',
  'HELLO' LIKE '_____',
  'HELLO' LIKE '_HELLO',
  'HELLO' LIKE 'HEL_',
  'HELLO' LIKE 'H_O'
  
SELECT * FROM Employees
WHERE Notes LIKE '%economics%'

SELECT * FROM OrderDetails
WHERE OrderID LIKE '1025_'
```









**참고**

- https://www.yalco.kr/@sql