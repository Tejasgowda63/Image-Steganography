const wrapper=document.querySelector('.wrapper');
        const loginLink=document.querySelector('.login-link');
        const registerLink=document.querySelector('.register-link');
        const btnpopup=document.querySelector('.lo');
        const iconClose=document.querySelector('.icon-close');
        registerLink.addEventListener('click',()=> {
            wrapper.classList.add('active');
            wrapper.classList.add('marg');
        });

        loginLink.addEventListener('click',()=> {
            wrapper.classList.remove('active');
        });

        btnpopup.addEventListener('click',()=> {
            wrapper.classList.add('active-popup');
            wrapper.classList.add('marg');
        });

        iconClose.addEventListener('click',()=> {
            wrapper.classList.remove('active-popup');
        });


        