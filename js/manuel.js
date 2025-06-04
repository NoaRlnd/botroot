function showMessage(message) {
  const statusMessage = document.getElementById('status-message');
  statusMessage.textContent = message;
  statusMessage.classList.add('show');
  setTimeout(() => {
    statusMessage.classList.remove('show');
  }, 2000);
}

function move(direction) {
  const btns = document.querySelectorAll('.button');
  btns.forEach(btn => btn.disabled = true);
  fetch("http://localhost:5000/api/move", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ direction })
  })
    .then(res => res.json())
    .then(data => showMessage(data.message || "Déplacement envoyé"))
    .catch(() => showMessage("Erreur lors de l'envoi du déplacement"))
    .finally(() => btns.forEach(btn => btn.disabled = false));
}

function resetPosition() {
  const btns = document.querySelectorAll('.button');
  btns.forEach(btn => btn.disabled = true);
  showMessage("Retour à la position initiale…");
  fetch("http://localhost:5000/api/reset", {
    method: "POST"
  })
    .then(res => res.json())
    .then(data => showMessage(data.message || "Position réinitialisée"))
    .catch(() => showMessage("Erreur lors du retour à la position initiale"))
    .finally(() => btns.forEach(btn => btn.disabled = false));
}


function toggleLaser() {
  const laserButton = document.querySelector('.laser-btn');
  const isActive = laserButton.classList.toggle('active');
  const btns = document.querySelectorAll('.button');
  btns.forEach(btn => btn.disabled = true);
  showMessage(isActive ? "Activation du laser…" : "Désactivation du laser…");

  fetch("http://localhost:5000/api/laser", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ state: isActive })
  })
    .then(res => res.json())
    .then(data => showMessage(data.message || (isActive ? "Laser activé !" : "Laser désactivé !")))
    .catch(() => showMessage("Erreur lors du contrôle du laser"))
    .finally(() => btns.forEach(btn => btn.disabled = false));
}


function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  document.querySelector('.controller').classList.toggle('dark-mode');
  document.querySelectorAll('.button').forEach(btn => btn.classList.toggle('dark-mode'));
}