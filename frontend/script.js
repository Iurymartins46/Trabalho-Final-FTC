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
  // Remove a classe de animação do jogador atacado
  var playerToAttack = (currentPlayer === 1) ? 1 : 2;
  var playerElement = document.getElementById("player" + playerToAttack);
  playerElement.classList.remove("shake");
  
  // Adiciona a classe de sobreposição ao jogador atacado
  var gifElement = document.getElementById("player" + playerToAttack + "-gif");
  gifElement.classList.add("player-gif");

  // Exibe o GIF de ataque sobreposto ao jogador
  gifElement.style.display = "block";

  // Define o caminho do GIF de ataque com base no jogador
  var gifPath = "";
  var duration = 0;
  if (playerToAttack === 1) {
    gifPath = "tank1atk.gif";
    duration = 1600; // 1.6 segundos
  } else {
    gifPath = "tank2atk.gif";
    duration = 3100; // 3.1 segundos
  }

  // Define a imagem do GIF de ataque
  gifElement.style.backgroundImage = "url('" + gifPath + "')";

  // Atualiza a vida do jogador atual
  if (currentPlayer === 1) {
    health2 -= 20;
    updateHealthBar(2);

    if (health2 <= 0) {
      // Exibe a caveira e encerra o jogo
      var closeElement = document.querySelector("#player2 .close");
      closeElement.style.display = "block";
      endGame();
      return;
    }
  } else {
    health1 -= 20;
    updateHealthBar(1);

    if (health1 <= 0) {
      // Exibe a caveira e encerra o jogo
      var closeElement = document.querySelector("#player1 .close");
      closeElement.style.display = "block";
      endGame();
      return;
    }
  }

  // Restaura a imagem original após a duração definida
  setTimeout(function() {
    gifElement.style.display = "none";
    gifElement.style.backgroundImage = "none";
  }, duration);

  // Alterna a vez para o próximo jogador
  currentPlayer = (currentPlayer === 1) ? 2 : 1;
  updateTurnMessage();
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
  updateTurnMessage();

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

  // Adiciona a classe de pulsação ao jogador atual
  var playerElement = document.getElementById("player" + currentPlayer);
  playerElement.classList.add("pulse");

  // Mostra o ícone "+" durante a pulsação
  var plusIcon = document.getElementById("plusIcon" + currentPlayer);
  plusIcon.style.display = "inline";

  // Remove a classe de pulsação e oculta o ícone após um tempo
  setTimeout(function() {
    playerElement.classList.remove("pulse");
    plusIcon.style.display = "none";
  }, 1000);

  // Alterna a vez para o próximo jogador
  currentPlayer = (currentPlayer === 1) ? 2 : 1;
  updateTurnMessage();
}

function updateTurnMessage() {
  var turnElement = document.getElementById("turn");
  var playerName = (currentPlayer === 1) ? "Player 1" : "Player 2";
  turnElement.textContent = "Vez do jogador: " + playerName;
  turnElement.classList.add("turn");
}

function endGame() {
  // Desabilita os botões de ação
  var buttons = document.querySelectorAll(".options button");
  buttons.forEach(function (button) {
    button.disabled = true;
  });

  // Atualiza a mensagem de turno
  var turnElement = document.getElementById("turn");
  turnElement.textContent = "Fim do Jogo!";
}


// Inicializa as barras de vida
updateHealthBar(1);
updateHealthBar(2);
