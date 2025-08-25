document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
    const languageChanger = document.getElementById('language-changer');

    const translations = {
        ko: {
            title: '로그인',
            usernameLabel: '사용자 이름',
            passwordLabel: '비밀번호',
            rememberLabel: '아이디 저장',
            forgotPasswordLink: '비밀번호를 잊으셨나요?',
            loginButton: '로그인',
            signupText: '계정이 없으신가요?',
            signupLink: '회원가입'
        },
        en: {
            title: 'Login',
            usernameLabel: 'Username',
            passwordLabel: 'Password',
            rememberLabel: 'Remember me',
            forgotPasswordLink: 'Forgot your password?',
            loginButton: 'Login',
            signupText: 'Don\'t have an account?',
            signupLink: 'Sign up'
        }
    };

    const changeLanguage = (language) => {
        const t = translations[language];
        document.querySelector('h2').textContent = t.title;
        document.querySelector('label[for="username"]').textContent = t.usernameLabel;
        document.querySelector('label[for="password"]').textContent = t.passwordLabel;
        document.querySelector('.options label').innerHTML = `<input type="checkbox" name="remember"> ${t.rememberLabel}`;
        document.querySelector('.options a').textContent = t.forgotPasswordLink;
        document.querySelector('button[type="submit"]').textContent = t.loginButton;
        document.querySelector('.signup-link p').innerHTML = `${t.signupText} <a href="signup.html">${t.signupLink}</a>`;
        localStorage.setItem('language', language);
        languageChanger.value = language;
    };

    languageChanger.addEventListener('change', (event) => {
        changeLanguage(event.target.value);
    });

    const savedLanguage = localStorage.getItem('language') || 'ko';
    changeLanguage(savedLanguage);

    loginForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value.trim();
        const password = document.getElementById('password').value.trim();

        if (username === '' || password === '') {
            alert('사용자 이름과 비밀번호를 모두 입력해주세요.');
        } else {
            // 실제 로그인 처리 로직 (예: 서버로 데이터 전송)
            alert(`로그인 시도: 
사용자 이름: ${username}
비밀번호: ${password}`);
            
            // 폼 초기화
            loginForm.reset();
        }
    });
});
