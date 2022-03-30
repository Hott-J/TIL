# Elastic_Stack_Study
## version 
- elasticsearch-7.13.3
- kibana-7.13.3

## ELK 장점
- 무료 오픈 소스
- 쉽고 빠른 설치
- 유연성 있는 커스터마이징 가능한 실시간 데이터 수집 플랫폼
- 아주 깔끔하고 세련된 키바나 대시보드 제공
- 수 억, 수십억 건까지 커버 가능한 월등한 성능
- 간단한 분산 네트워크 환경
- 함께 사용 가능한 다양한 제품군

## ELK 단점
- 사용자를 테스터로 하는 버전 업데이트

```json
GET _search
{
  "query": {
    "match_all": {}
  }
}

GET /_cat/health?v

PUT /customer?pretty

GET _cat/indices?v

POST customer/type1/1
{
  "name": "hottj",
  "age": "29"
}

GET customer/type1/1

DELETE customer/type1/1

DELETE /customer

POST customer/type1/1/_update
{
  "script":{
    "inline":"if(ctx._source.age == 123){ctx._source.age++}"
  }
}

POST customer/type1/1
{
  "name": "hottj1"
}
```
## Quiz
- TourCompany의 오신 것을 환영합니다! 이 여행사는 여러분이 고객명단을 잘 관리해주리라 믿고의뢰합니다. 다음 시나리오에 따라 여러분들의 작업을 진행하시면 됩니다! 이 회사에는 엘라스틱서치가 새로 도입돼 아무런 데이터도 없습니다. 고객관리를 위해 다음 데이터를
입력하십시오. (Index : tourcompany, Type : customerlist) 다음 임무를 수행하기 위해 쿼리문을 작성하고 데이터베이스에 적용하십시오.
- BoraBora 여행은 공항테러 사태로 취소됐습니다. BoraBora 여행자의 명단을 삭제해주십시오. 
- Hawaii 단체 관람객의 요청으로 출발일이 조정됐습니다. 2017/01/10에 출발하는 Hawaii의 출발일을 2017/01/17일로 수정해주십시오. 
- 휴일 여행을 디즈니랜드로 떠나는 사람들의 핸드폰 번호를 조회하십시오

```json
POST tourcompany/customerlist/1
{
  "name":"Alfred",
  "phone":"010-1234-5678",
  "holiday_dest":"Disneyland",
  "departure_date":"2017/01/20"
}

POST tourcompany/customerlist/2
{
  "name":"Huey",
  "phone":"010-2222-4444",
  "holiday_dest":"Disneyland",
  "departure_date":"2017/01/20"
}

POST tourcompany/customerlist/3
{
  "name":"Naomi",
  "phone":"010-3333-5555",
  "holiday_dest":"Hawaii",
  "departure_date":"2017/01/10"
}

POST tourcompany/customerlist/4
{
  "name":"Andra",
  "phone":"010-6666-7777",
  "holiday_dest":"Bora Bora",
  "departure_date":"2017/01/11"
}

POST tourcompany/customerlist/5
{
  "name":"Paul",
  "phone":"010-9999-8888",
  "holiday_dest":"Hawaii",
  "departure_date":"2017/01/10"
}

POST tourcompany/customerlist/6
{
  "name":"Colin",
  "phone":"010-5555-4444",
  "holiday_dest":"Venice",
  "departure_date":"2017/01/16"
}


DELETE tourcompany/customerlist/4

POST tourcompany/customerlist/3/_update
{
 "doc":
 {
   "departure_date" : "2017/01/17"
 }
}

POST tourcompany/customerlist/5/_update
{
 "doc":
 {
   "departure_date" : "2017/01/17"
 }
}

GET tourcompany/customerlist/3
GET tourcompany/customerlist/5

GET tourcompany/customerlist/1
GET tourcompany/customerlist/2

POST customer/type1/_bulk
{"index":{"_id":"1"}}
{"name":"hottj1"}
{"index":{"_id":"2"}}
{"name":"hottj2"}

GET customer/type1/2

POST customer/type1/_bulk
{"update":{"_id":"1"}}
{"doc":{"age":29}}
{"delete":{"_id":"2"}}

GET customer/type1/1
```

```json
# search API query
GET _cat/indices

GET kibana_sample_data_flights/_search?q=*

GET kibana_sample_data_flights/_search?q=*&sort=AvgTicketPrice

POST kibana_sample_data_flights/_search
{
  "query":{"match_all":{}},
  "sort":{"AvgTicketPrice":"asc"}
}

POST kibana_sample_data_flights/_search
{
  "query":{"match":{"DestCountry":"AU"}},
  "sort":{"AvgTicketPrice":"desc"},
  "_source":["AvgTicketPrice","FlightNum","DestCountry"]
}

POST kibana_sample_data_flights/_search
{
  "query":{"match_phrase":{"DestCountry":"AU"}},
  "sort":{"AvgTicketPrice":"desc"},
  "_source":["AvgTicketPrice","FlightNum","DestCountry"]
}

POST kibana_sample_data_flights/_search
{
  "query":{
    "bool":{
      "must" : {"match":{"DestCountry":"AU"}},
      "must_not" : {"match":{"FlightNum": "9HY9SWR"}}
    }
  }
}

GET _search

GET kibana_sample_data_flights/_search?q=OriginWeather:Sunny AND DestCountry:AU&_source=OriginWeather,DestCountry,AvgTicketPrice&sort=AvgTicketPrice:desc

GET tourcompany/_search

#1
GET tourcompany/_search?q="010-3333-5555"

#2
GET tourcompany/_search?q=holiday_dest:Disneyland&_source=phone

#3
GET tourcompany/_search?q=departure_date:"2017/01/10" OR departure_date:"2017/01/11"&_source=name,departure_date&sort=name.keyword

#4
POST tourcompany/customerlist/_delete_by_query?q="Bora Bora"

#5
POST tourcompany/customerlist/_update_by_query
{
  "script":{"inline":"ctx._source.departure_date='2017/01/17'","lang":"painless"},
  "query":{
    "bool":{
      "must":[
        {"match":{"departure_date":"2017/01/10"}},
        {"match":{"holiday_dest":"Hawaii"}}
      ]
    }
  }
}
```





