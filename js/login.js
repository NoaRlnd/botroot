document.addEventListener('DOMContentLoaded', () => {
    // Vérifie si déjà connecté
    const isLoggedIn = localStorage.getItem('isLoggedIn') === 'true';
    const loggedInUser = localStorage.getItem('loggedInUser');

    // Affiche/masque le bouton de déconnexion
    document.getElementById('logout-link').style.display = isLoggedIn ? 'inline-block' : 'none';

    // Affiche le formulaire admin si connecté
    if (isLoggedIn) {
        document.querySelector('.container-admin').style.display = 'block';
    }

    // Gestion du formulaire de login
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://localhost:3000/login', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username, password })
                });
                const result = await response.json();
                if (result.success) {
                    localStorage.setItem('isLoggedIn', 'true');
                    localStorage.setItem('loggedInUser', username);
                    document.getElementById('login-message').textContent = "Connexion réussie !";
                    window.location.href = 'index.html';
                } else {
                    document.getElementById('login-message').textContent = "Identifiant ou mot de passe incorrect.";
                }
            } catch (e) {
                document.getElementById('login-message').textContent = "Erreur de connexion au serveur.";
            }
        });
    }

    // Gestion du formulaire d’ajout utilisateur (admin)
    const addUserForm = document.getElementById('add-user-form');
    if (addUserForm) {
        addUserForm.addEventListener('submit', async function(event) {
            event.preventDefault();
            const newUsername = document.getElementById('new-username').value;
            const newPassword = document.getElementById('new-password').value;
            const role = document.getElementById('role').value;
            try {
                const response = await fetch('http://localhost:3000/addUser', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ username: newUsername, password: newPassword, role })
                });
                const result = await response.json();
                if (result.success) {
                    document.getElementById('add-user-message').textContent = "Utilisateur ajouté avec succès !";
                } else {
                    document.getElementById('add-user-message').textContent = "Erreur lors de l'ajout de l'utilisateur.";
                }
            } catch (e) {
                document.getElementById('add-user-message').textContent = "Erreur de connexion au serveur.";
            }
        });
    }

    // Redirection automatique si nécessaire (exemple)
    const restrictedPages = ['déconnexion.html', 'élèves.html', 'sttgs.html'];
    const currentPage = window.location.pathname.split('/').pop();
    if (!isLoggedIn && restrictedPages.includes(currentPage)) {
        window.location.href = 'authentification.html';
    }
});