# Finance Teacher 개요

## 팀원

**여대기<버니>**

**팀장**

[https://github.com/daegi0923](https://github.com/daegi0923)

**진아현<푸린>**

**팀원**

[https://github.com/akeroroh](https://github.com/akeroroh)

## 개발 기간
- 2024.05.08 ~ 2024.05.24

# 컨셉 및 서비스 구상

## 기획 의도 및 서비스 대상
- <금선생>는 사회초년생을 대상으로 미래의 금융 계획을 세워주고 금융 정보들을 알려주는 서비스입니다. 

## 서비스 소개


# GOAL

# 개발 계획 및 역할 구분



## 기술스택

### Frontend
![CSS](https://github.com/daegi0923/Finance_Teacher/assets/156268579/844bf7c2-b437-493e-bd56-c8f8e2f9a0ac)
![HTML](https://github.com/daegi0923/Finance_Teacher/assets/156268579/abf1b0c3-c9b4-4d1b-86b4-70e6b81fff14)
![JavaScript](https://github.com/daegi0923/Finance_Teacher/assets/156268579/699fa91c-d9ae-4cc8-a94c-4bfd212d13ee)
![NodeJS](https://github.com/daegi0923/Finance_Teacher/assets/156268579/3682f902-0df9-4dfd-af3d-fe7984a79adc)
![Vue](https://github.com/daegi0923/Finance_Teacher/assets/156268579/a824421a-b4c6-4ede-a0a3-bc7f7b0a4eac)
![Bootstrap](https://github.com/daegi0923/Finance_Teacher/assets/156268579/ec6f4c82-c51f-4ec7-a9ea-bc7c0e9186a2)



### Backend

![Django](https://github.com/daegi0923/Finance_Teacher/assets/156268579/8615975f-6d58-481e-8193-0dd1fe7aaf7f)
![Python-Dark](https://github.com/daegi0923/Finance_Teacher/assets/156268579/255e8516-1621-46a0-8873-175dac677949)

### Database

![SQLite](https://github.com/daegi0923/Finance_Teacher/assets/156268579/d08e0340-15d6-46cf-bd13-5667b510ba07)

### Communication

![Github-Dark](https://github.com/daegi0923/Finance_Teacher/assets/156268579/4f360ced-a27e-4e29-bb87-f11e93792c06)

# ERD
![ERD](https://github.com/daegi0923/Finance_Teacher/assets/156268579/02ad2ba8-f6ca-400d-8b11-47d7b1f87c71)


# 컴포넌트 구조


# 개발일지
| 날짜 | 푸린 | 버니 |
| --- | --- | --- |
| 240508 | 컨셉, 아이디어 회의, github 협업 등록 | 아이디어 회의, 프로젝트 계획 간트차트 작성, github Repository 생성 |
| 240509 | 요구사항 명세서 작성, 역할 구분  | 요구사항 명세서 작성, 팀 역할 구분   |
| 240510 | 컴포넌트 설계서 작성 | ERD 초기 작성  |
| 240511 | 와이어프레임 작성, vue-project 생성 | ERD 작성 |
| 240512 | router 지정, component 생성, view 생성 | ERD 최종 작성   |
| 240513 | 카카오맵지도 받아오기 | django skeleton code 작성, 금융상품 api 작성 |
| 240514 | 네이버기사 크롤링 | 로그인, 로그아웃, 회원가입 기능 구현   |
| 240515 | 환율 데이터 읽어오기 | - |
| 240516 | 환율 계산기 | 게시판 CRUD, 댓글 CRD 구현   |
| 240517 | 환율 계산기와 지도 마무리하기 | 금융상품목록, 상세 출력    |
| 240518 | 라우터 정리 | 금융상품 구독기능 구현    |
| 240519 | 단어장 api 읽어오기 | 회원정보 수정 api 구현   |
| 240520 | gemini 챗봇 만들기
프론드 디자인 구성 | 회원정보 수정(FE), 회원탈퇴, 회원 정보 필드 추가, 프로필 페이지 구현, 금융상품목록 에러 해결        |
| 240521 | CSS 수정 | CSS 수정, 프로필 페이지 그래프 구현 |
| 240522 | CSS 수정 | 상품 추천 알고리즘 및 페이지 구현, 프로필 페이지 네비게이션 구현, CSS 수정       |
| 240523 | CSS 수정, 챗봇 수정, 단어장 완성, 지도 완성 | CSS수정, 상품추천 페이지 오류 해결, 배포작업 수행     |
| 240524 | 발표 당일  | 발표 당일  |

# 이슈 관리
| 이름 | 내용 | 해결 여부 | 해결 과정 | 일시 |
| --- | --- | --- | --- | --- |
| 버니 | Django User Model Custom 도중 에러 발생   | O | http://settings.py 에 AUTH_USER_MODEL 등록 누락   | 240513 |
| 버니 | User Info update api 구현 중 'str' object has no attribute '_meta'에러 발생 | O | http://serializers.py 에서 AUTH_USER_MODEL 사용이 아닌 get_user_model 사용해야함     | 240519 |
| 버니 | 프로필 페이지 graph 출력에서 데이터가 연결되지 않음         | O | Vue의 Life Cycle Hook 때문에 생긴 문제, 부모 페이지의 mount 가 자식 페이지의  mount 보다 늦게 일어나는데, 이때문에 graph가 mount 될때 반응형 변수가 비어있었음. store 사용하여 해결 |240520
| 버니 | 예금, 적금 목록 필터링 중 filter메소드 사용하여 렌더링할 시 undefined 참조 에러 발생          | O | 데이터 구조 변화를 통해 deposit item 하위의 option객체를 가지는 형태가 아닌 N*M 형태의 테이블 형태로 변경(반정규화) | 240520 |
| 버니 | intr_rate가 null인 option 이 새로생김(금융감독원 api)     | O | 데이터 제약조건 변경    | 240521 |
| 푸린 | 네이버 뉴스 크롤링 Axios 에러 | O | 프론트에서 proxy를 우회하여 해결 | 240514 |
| 푸린 | 환율계산기 나라별 단위가 다르고 업데이트가 11시를 기준으로 되며 공휴일에 제공하지 않음 | O | 날짜 함수와 조건문 함수를 이용해 해결 | 240516 |
| 푸린 | chatGPT 할당량 초과 | O | Gemini를 이용하여 제작 | 240520 |
| 푸린  | 단어장  html 코드가 계속 나옴 | O | 함수를 사용해 해결 | 240523 |
| 푸린 | 챗봇 입력 오류 | O | 함수 수정 | 240523 |

# 노션 링크
[https://www.notion.so/P-B-53d3afb7de7544bfbf7cf3cbc2e06474](https://www.notion.so/P-B-53d3afb7de7544bfbf7cf3cbc2e06474)
