document.addEventListener('DOMContentLoaded', () => {
    const signupForm = document.getElementById('signup-form');
    const languageChanger = document.getElementById('language-changer');

    const translations = {
        ko: {
            title: '회원가입',
            usernameLabel: '사용자 이름',
            emailLabel: '이메일',
            passwordLabel: '비밀번호',
            confirmPasswordLabel: '비밀번호 확인',
            signupButton: '회원가입',
            loginText: '이미 계정이 있으신가요?',
            loginLink: '로그인'
        },
        en: {
            title: 'Sign Up',
            usernameLabel: 'Username',
            emailLabel: 'Email',
            passwordLabel: 'Password',
            confirmPasswordLabel: 'Confirm Password',
            signupButton: 'Sign Up',
            loginText: 'Already have an account?',
            loginLink: 'Login'
        }
    };

    const changeLanguage = (language) => {
        const t = translations[language];
        document.querySelector('h2').textContent = t.title;
        document.querySelector('label[for="username"]').textContent = t.usernameLabel;
        document.querySelector('label[for="email"]').textContent = t.emailLabel;
        document.querySelector('label[for="password"]').textContent = t.passwordLabel;
        document.querySelector('label[for="confirm-password"]').textContent = t.confirmPasswordLabel;
        document.querySelector('button[type="submit"]').textContent = t.signupButton;
        document.querySelector('.login-link p').innerHTML = `${t.loginText} <a href="login.html">${t.loginLink}</a>`;
        localStorage.setItem('language', language);
        languageChanger.value = language;
    };

    languageChanger.addEventListener('change', (event) => {
        changeLanguage(event.target.value);
    });

    const savedLanguage = localStorage.getItem('language') || 'ko';
    changeLanguage(savedLanguage);

    signupForm.addEventListener('submit', (event) => {
        event.preventDefault();

        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();
        const confirmPassword = document.getElementById('confirm-password').value.trim();

        if (username === '' || email === '' || password === '' || confirmPassword === '') {
            alert('모든 필드를 입력해주세요.');
            return;
        }

        if (password !== confirmPassword) {
            alert('비밀번호가 일치하지 않습니다.');
            return;
        }

        // 실제 회원가입 처리 로직 (예: 서버로 데이터 전송)
        alert(`회원가입 시도: 
사용자 이름: ${username}
이메일: ${email}`);

        // 폼 초기화
        signupForm.reset();
    });
});
