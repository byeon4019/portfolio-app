from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='static')

# 포트폴리오 데이터 API
@app.route('/api/profile', methods=['GET'])
def get_profile():
    return jsonify({
        "name": "변혜와",
        "title": "서비스 기획자",
        "tagline": "문제 정의부터 해결까지, 기술과 사람을 연결합니다.",
        "contact": {
            "email": "byeon4019@naver.com",
            "phone": "+82 10 6238 8448"
        }
    })

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify([
        {
            "id": 1,
            "title": "공공부문 SaaS 신규 개발 검증 사업",
            "role": "실무 책임자",
            "period": "1차년도 ~ 2차년도",
            "tags": ["SaaS", "기획", "보안인증", "Kubernetes"],
            "results": [
                "사업 성공판정 (1·2차년도 80점 안정 종료)",
                "CSAP · 클라우드서비스확인제 · PaaSTa 인증 획득",
                "긍정 응답률 80% 이상 달성",
                "혁신시제품 선정 → 매출 증가",
                "내부 개발팀 전환 성공"
            ],
            "description": "기획부터 보안인증까지 통합적으로 수행한 공공 SaaS 프로젝트. 텍스트 기반 데이터 제공의 한계를 시각화 대시보드로 개선하고, CSAP 인증을 고려한 인프라 설계에 참여했습니다."
        },
        {
            "id": 2,
            "title": "협업 서비스 두레이 온보딩 매니저",
            "role": "온보딩 기획 담당",
            "period": "진행중",
            "tags": ["온보딩", "UX기획", "교육설계", "커뮤니케이션"],
            "results": [
                "비전공자 대상 클라우드·컨테이너 교육 기획 및 진행",
                "사용자 서비스 적응 지원 체계 구축"
            ],
            "description": "기술과 사용자 사이의 이해도를 연결하는 온보딩 기획. 기능과 활용 방식을 쉽게 전달하여 서비스 빠른 정착을 지원했습니다."
        }
    ])

@app.route('/api/skills', methods=['GET'])
def get_skills():
    return jsonify([
        {"category": "기획 · 설계", "items": ["서비스 기획", "UX/UI 기획", "요구사항 분석", "프로토타이핑"]},
        {"category": "프로젝트 관리", "items": ["WBS 일정 관리", "산출물 관리", "이해관계자 커뮤니케이션"]},
        {"category": "보안 · 인증", "items": ["CSAP", "클라우드서비스확인제", "PaaSTa 호환성 인증", "정보보안 정책 수립"]},
        {"category": "기술 이해", "items": ["Kubernetes", "컨테이너", "SaaS 구조", "클라우드 인프라"]}
    ])

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "포트폴리오 API 서버가 정상 동작 중입니다."})

# 프론트엔드 서빙
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
