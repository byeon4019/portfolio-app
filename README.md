# 변혜와 포트폴리오

Flask 기반 REST API 서버와 포트폴리오 프론트엔드를 결합한 웹 애플리케이션입니다.  
AppPaaS(NHN Enterprise) GitHub 연동 배포를 위해 구성되었습니다.

## 구조

```
portfolio-app/
├── app.py              # Flask API 서버 (백엔드)
├── static/
│   └── index.html      # 포트폴리오 페이지 (프론트엔드)
├── requirements.txt
├── Dockerfile
└── README.md
```

## API 엔드포인트

| Method | Path | 설명 |
|--------|------|------|
| GET | `/api/health` | 서버 상태 확인 |
| GET | `/api/profile` | 기본 프로필 정보 |
| GET | `/api/projects` | 담당 프로젝트 목록 |
| GET | `/api/skills` | 역량 목록 |

## 로컬 실행

```bash
pip install -r requirements.txt
python app.py
```

## Docker 실행

```bash
docker build -t portfolio-app .
docker run -p 5000:5000 portfolio-app
```

접속: http://localhost:5000
