# Django 1~5일차 정리

## 핵심 명령어
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/Scripts/activate

# 프로젝트 및 앱 생성
django-admin startproject demo_first .
python manage.py startapp demo_app

# 서버 실행
python manage.py runserver

# DB 마이그레이션
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# shell_plus 실행 및 ORM 테스트
python manage.py shell_plus
demo_model.objects.all()
demo_model.objects.create(num=1, destination="test")


## 이론 요약

- **URL → View → Template**: 사용자의 요청은 URL 패턴을 통해 View 함수로 전달되고, View는 처리 결과를 Template에 담아 반환한다.  
- **Model**: 데이터베이스와 연결되는 구조로, `IntegerField`, `TextField`, `TimeField` 등 다양한 필드 타입을 지원하며 ORM을 통해 조작된다.  
- **ORM (Object Relational Mapping)**: SQL 문을 직접 작성하지 않고 Python 객체를 통해 데이터베이스를 조회·생성·수정·삭제할 수 있다.  
- **CRUD 흐름**: Create, Read, Update, Delete 기능을 View와 Template을 연결하여 구현한다.  
- **템플릿 상속**: `base.html`에서 공통 레이아웃을 정의하고, `index.html`이나 다른 페이지에서 이를 상속받아 재사용할 수 있다.  
- **Admin & shell_plus**: Admin 페이지에서는 GUI로 데이터를 관리할 수 있고, shell_plus에서는 ORM 쿼리를 빠르게 실습할 수 있다.  

## 회고

오늘은 Django의 기본 사이클을 따라가며 환경 세팅부터 프로젝트와 앱 생성, URL과 View 연결, Model 정의, 그리고 CRUD 구현까지 전 과정을 직접 실습하였다.  
명령어 중심으로 작업한 덕분에 흐름이 단순하게 정리되었고, Django 개발의 핵심 단계를 명확히 이해할 수 있었다.  
특히 ORM과 Admin 페이지를 통해 데이터가 실제 데이터베이스에 반영되는 과정을 눈으로 확인하면서 Django가 제공하는 편리함을 체감할 수 있었으며, 템플릿 상속을 통해 코드 재사용성과 구조적 설계의 장점을 경험할 수 있었다.  
이번 과정을 통해 Django의 기초를 한 사이클 돌려봤다는 성취감이 생겼고, 앞으로는 기능을 확장해가며 더 복잡한 웹 애플리케이션을 만들어보고 싶다는 동기부여가 되었다.  
