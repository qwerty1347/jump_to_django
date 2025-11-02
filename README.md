# Jump to Django

Django를 활용한 웹 애플리케이션입니다. OAuth 기반의 안전한 인증을 통해 안전하고 신뢰성 높은 서비스를 제공합니다.


## 🛠️ 기술 스택

### 백엔드
- **프레임워크**: Django 5.2.4
- **데이터베이스**:
  - MySQL


### 개발 도구
- **디버깅**: Django Debug Toolbar 6.0.0
- **환경 변수 관리**: django-environ 0.11.2
- **타임존**: pytz 2025.2


## 🔧 주요 기능

### 사용자 인증 시스템
- 회원가입 및 로그인/로그아웃
- 사용자 프로필 관리
- 권한 관리


### Q&A 게시판 (pybo)
- 질문 및 답변 작성
- 댓글 기능
- 게시물 검색 및 필터링


## 🏗️ 프로젝트 구조
```
jump_to_django/
├── apps/
│   ├── common/           # 공통 기능 (사용자 인증 등)
│   │   ├── auth/         # 인증 관련 코드
│   │   │   ├── forms/    # 폼 클래스
│   │   │   ├── repositories/  # 데이터 접근 계층
│   │   │   ├── services/     # 비즈니스 로직
│   │   │   └── views/        # 뷰 함수/클래스
│   │   └── models.py     # 공통 모델
│   └── pybo/             # Q&A 애플리케이션
│       └── ...
├── config/               # 프로젝트 설정
│   ├── __init__.py
│   ├── settings.py       # 설정 파일
│   ├── urls.py          # URL 설정
│   └── wsgi.py          # WSGI 설정
├── manage.py            # Django 명령줄 유틸리티
└── requirements.txt     # 의존성 목록
```