document.addEventListener('DOMContentLoaded', function() {
    const isLoggedIn = localStorage.getItem('isLoggedIn');

    // Gérer la redirection si l'utilisateur n'est pas connecté
    const restrictedPages = ['déconnexion.html', 'élèves.html', 'sttgs.html', 'déconnexion.html'];
    const currentPage = window.location.pathname.split('/').pop();

    if (!isLoggedIn && restrictedPages.includes(currentPage)) {
        window.location.href = 'authentification.html';
    }

    // Aafficher ou masquer les boutons en fonction de l'état de connexion
    const navLinks = document.querySelectorAll('nav.nav li a');
    navLinks.forEach(link => {
        const buttonText = link.textContent.trim().toLowerCase();
        if (!isLoggedIn && (buttonText === 'se déconnecter' || buttonText === 'déconnexion' || buttonText === 'paramètres' || buttonText === 'élèves')) {
            link.style.display = 'none';
        }
    });
});