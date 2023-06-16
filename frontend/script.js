var currentPlayer = 1;
var maxHealth = 100;
var health1 = maxHealth;
var health2 = maxHealth;

function updateHealthBar(playerId) {
  var health = (playerId === 1) ? health1 : health2;
  var healthBar = document.getElementById("healthBar" + playerId);
  var percentage = (health / maxHealth) * 100;
  healthBar.style.width = percentage + "%";
}

function ataque() {
    // Lógica de ataque do jogador atual
    
    // Adiciona a classe de animação ao jogador atacado
    var playerToAttack = (currentPlayer === 1) ? 2 : 1;
    var playerElement = document.getElementById("player" + playerToAttack);
    playerElement.classList.add("shake");
  
    // Atualiza a vida do jogador atual
    if (currentPlayer === 1) {
      health2 -= 20;
      updateHealthBar(2);
    } else {
      health1 -= 20;
      updateHealthBar(1);
    }
  
    // Alterna a vez para o próximo jogador
    currentPlayer = (currentPlayer === 1) ? 2 : 1;
    var turnElement = document.getElementById("turn");
    turnElement.textContent = "Vez do jogador: " + currentPlayer;
  
    // Remove a classe de animação após um tempo
    setTimeout(function() {
      playerElement.classList.remove("shake");
    }, 500);
  }

  function defesa() {
    // Lógica de defesa do jogador atual
    
    // Adiciona a classe de animação de defesa ao jogador atual
    var playerElement = document.getElementById("player" + currentPlayer);
    playerElement.classList.add("defense");
  
    // Atualiza a vida do jogador atual
    if (currentPlayer === 1) {
      health1 += 10;
      updateHealthBar(1);
    } else {
      health2 += 10;
      updateHealthBar(2);
    }
  
    // Alterna a vez para o próximo jogador
    currentPlayer = (currentPlayer === 1) ? 2 : 1;
    var turnElement = document.getElementById("turn");
    turnElement.textContent = "Vez do jogador: " + currentPlayer;
  
    // Remove a classe de animação após um tempo
    setTimeout(function() {
      playerElement.classList.remove("defense");
    }, 500);
  }
function recuperarVida() {
  // Lógica de recuperação de vida do jogador atual
  
  // Atualiza a vida do jogador atual
  if (currentPlayer === 1) {
    health1 = maxHealth;
    updateHealthBar(1);
  } else {
    health2 = maxHealth;
    updateHealthBar(2);
  }

  // Alterna a vez para o próximo jogador
  currentPlayer = (currentPlayer === 1) ? 2 : 1;
  var turnElement = document.getElementById("turn");
  turnElement.textContent = "Vez do jogador: " + currentPlayer;
}

// Inicializa as barras de vida
updateHealthBar(1);
updateHealthBar(2);
