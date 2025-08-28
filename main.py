from flask import Flask, render_template_string

app = Flask(__name__)

# HTML 페이지 내용을 파이썬 변수로 저장합니다.
HTML_CONTENT = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>조윤슬 개발자 프로필</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            padding: 0;
            background-color: #f4f4f4;
            color: #333;
        }
        .profile-container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1, h2 {
            color: #2c3e50;
        }
        .contact-info a {
            color: #3498db;
            text-decoration: none;
        }
        .contact-info a:hover {
            text-decoration: underline;
        }
        .skills ul {
            list-style-type: none;
            padding: 0;
        }
        .skills li {
            background: #ecf0f1;
            padding: 8px 12px;
            margin: 5px 0;
            border-radius: 5px;
            display: inline-block;
        }
    </style>
</head>
<body>

    <div class="profile-container">
        <header>
            <h1>조윤슬 (Yooh-seul Jo)</h1>
            <p><strong>주니어 백엔드 개발자</strong></p>
        </header>

        <section class="about-me">
            <h2>자기소개</h2>
            <p>안녕하세요! 사용자에게 가치를 제공하는 훌륭한 백엔드 시스템을 만드는 것을 즐기는 개발자 조윤슬입니다. 효율적이고 확장 가능한 코드를 작성하는 것을 목표로 끊임없이 배우고 성장하고 있습니다. 새로운 기술에 대한 호기심이 많고, 동료들과 협력하여 문제를 해결하는 것을 좋아합니다.</p>
        </section>

        <section class="skills">
            <h2>기술 스택</h2>
            <ul>
                <li>Python</li>
                <li>Django</li>
                <li>Flask</li>
                <li>SQL (PostgreSQL, MySQL)</li>
                <li>RESTful API</li>
                <li>Git</li>
                <li>Docker</li>
            </ul>
        </section>

        <section class="projects">
            <h2>주요 프로젝트</h2>
            <p>이곳에 프로젝트 관련 정보를 추가하세요.</p>
        </section>

        <section class="contact-info">
            <h2>연락처</h2>
            <p>
                이메일: <a href="mailto:yoonseul.jo@example.com">yoonseul.jo@example.com</a><br>
                GitHub: <a href="https://github.com/yoonseuljo" target="_blank">github.com/yoonseuljo</a><br>
                링크드인: <a href="https://linkedin.com/in/yoonseuljo" target="_blank">linkedin.com/in/yoonseuljo</a>
            </p>
        </section>

        <footer>
            <p><small>&copy; 2025 조윤슬. All Rights Reserved.</small></p>
        </footer>
    </div>

</body>
</html>
"""

# 웹사이트의 기본 주소("/")로 접속하면 HTML_CONTENT 변수의 내용을 보여줍니다.
@app.route('/')
def home():
    return render_template_string(HTML_CONTENT)

# 이 파일을 직접 실행할 때 웹 서버를 시작합니다.
if __name__ == '__main__':
    app.run(debug=True)
