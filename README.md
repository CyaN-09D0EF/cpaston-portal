# 🏀 숏돌이 – 스포츠 매칭 웹 서비스

본 저장소는 캡스톤 프로젝트 단일 소개 페이지와 API를 제공합니다.  
Docker Compose 및 AWS EC2를 이용해 배포하였습니다.

---

## 1. 작품주제 (Subject)
- **제목:** 숏돌이 – 스포츠 매칭 플랫폼
- **요약:**  
  사용자의 위치와 선호 종목을 기반으로 운동 파트너를 매칭해주는 웹 서비스입니다.  
  Flask 백엔드와 HTML / CSS / JavaScript 프론트엔드로 구성되어 있으며,  
  Docker로 컨테이너화 후 AWS EC2에서 배포되었습니다.

---

## 2. 실용적 근거 (Rationale)
- **문제:**  
  주변에 함께 운동할 사람을 찾기 어렵고, 기존 커뮤니티 앱은 지역 기반 기능이 부족함.
- **근거(수치 / 설문 / 사례):**  
  설문 결과(표본 100명 중 76%)가 “운동 파트너를 구하기 어렵다”고 응답.  
- **기대 가치:**  
  사용자 맞춤형 운동 매칭을 통해 참여율 증대 및 커뮤니티 활성화 기여.

---

## 3. 핵심 기능 (Features)
- 기능 1: 종목 / 지역 / 시간대 기준 운동 파트너 매칭  
- 기능 2: 사용자 프로필 및 평판 시스템  
- 기능 3: 채팅 및 알림 기능으로 일정 조율 가능  

---

## 4. 구현 환경 (Environment)
- **Front-End(프론트엔드):** HTML, CSS, JavaScript  
- **Back-End(백엔드):** Python Flask 2.3  
- **Runtime(런타임):** Docker Engine / Docker Compose  
- **Deploy(배포):** AWS EC2 (선택 가능: AWS ECS)  

---

## 5. 팀 구성 및 역할 (Team)
| 이름 | 역할 |
|------|------|
| 양윤석 | 백엔드 개발 |
| 최세현 | 프론트엔드 개발 |
| 남지수 | 프로젝트 매니저 / 문서화 / 배포 |

---

## 6. 실행 방법 (Run)
### 로컬 또는 EC2 환경
```bash
# 프로젝트 클론
git clone https://github.com/<yourname>/capstone-portal.git
cd capstone-portal

# Docker Compose 빌드 및 실행
docker compose up --build -d
# cpaston-portal
