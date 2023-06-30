var currentPlayer = 1;
var maxHealth = 100;
var health1 = maxHealth;
var health2 = maxHealth;

// Obter elementos dos selects
var player1MachineSelect = document.getElementById("player1-machine");
var player2MachineSelect = document.getElementById("player2-machine");

// Função para preencher as opções do select
function preencherOpcoesSelect(arquivos) {
  arquivos.forEach(function(arquivo) {
    var option = document.createElement("option");
    option.value = arquivo;
    option.text = arquivo;
    player1MachineSelect.appendChild(option);

    option = document.createElement("option");
    option.value = arquivo;
    option.text = arquivo;
    player2MachineSelect.appendChild(option);
  });
}

// Carregar arquivos ao abrir o modal
listarArquivos()
  .then(function(arquivos) {
    preencherOpcoesSelect(arquivos);
  })
  .catch(function(error) {
    console.error("Erro ao obter a lista de arquivos:", error);
  });

// Função para abrir o modal
function openModal() {
  var modal = document.getElementById('modal');
  modal.style.display = 'block';
}

// Função para fechar o modal
function closeModal() {
  var modal = document.getElementById('modal');
  modal.style.display = 'none';
}

// Função chamada ao clicar no botão "Iniciar Partida"
async function startGame() {
  var player1Machine = document.getElementById('player1-machine').value;
  var player2Machine = document.getElementById('player2-machine').value;

  closeModal();
}

// Abre o modal assim que a página for carregada
window.onload = openModal;

// Adiciona o evento de clique ao botão "Iniciar Partida"
var startButton = document.getElementById('start-button');
startButton.addEventListener('click', startGame);

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
    gifPath = "images/Tank1Atk.gif";
    duration = 1000; // 1.0 segundos
  } else {
    gifPath = "images/Tank2Atk.gif";
    duration = 1000; // 1.0 segundos
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