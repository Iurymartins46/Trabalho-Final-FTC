var currentPlayer;
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

    if (arquivo.includes("1")) {
      player1MachineSelect.appendChild(option);
    } else {
      player2MachineSelect.appendChild(option);
    }
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

  escolherMaquina(player1Machine, player2Machine)
  .then(function(data) {
    currentPlayer = data.rodadaDoJogador;
    maxHealth = data.player1.vida;
    health1 = data.player1.vida;
    health2 = data.player2.vida;
  })
  .catch(function(error) {
    console.error("Erro ao realizar a escolha das maquinas", error);
  });

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

function distribuirAnimacao(data){
  health1 = data.player1.vidaAtual
  health2 = data.player2.vidaAtual
  updateHealthBar(1)
  updateHealthBar(2)

  //Player 1
  if (data.player1.estadoAtual.charAt(0) == "A"){
    ataque(1);
  } else if (data.player1.estadoAtual.charAt(0) == "D"){
    defesa(1);
  } else if (data.player1.estadoAtual.charAt(0) == "C"){
    cura(1);
  }

  //Player 2
  if (data.player2.estadoAtual.charAt(0) == "A"){
    ataque(2);
  } else if (data.player2.estadoAtual.charAt(0) == "D"){
    defesa(2);
  } else if (data.player2.estadoAtual.charAt(0) == "C"){
    cura(2);
  }

  if (health2 <= 0) {
    var closeElement = document.querySelector("#player2 .close");
    closeElement.style.display = "block";
    endGame();
    return;
  }

  if (health1 <= 0) {
    var closeElement = document.querySelector("#player1 .close");
    closeElement.style.display = "block";
    endGame();
    return;
  }

  // Alterna a vez para o próximo jogador
  currentPlayer = data.rodadaDoJogador;
  updateTurnMessage();
}

function click0(){
  rodada(0)
  .then(function(data) {
    distribuirAnimacao(data);
  })
  .catch(function(error) {
    console.error("Erro ao realizar a rodada", error);
  });
}

function click1(){
  rodada(1)
  .then(function(data) {
    distribuirAnimacao(data);
  })
  .catch(function(error) {
    console.error("Erro ao realizar a rodada", error);
  });
}

function click2(){
  rodada(2)
  .then(function(data) {
    distribuirAnimacao(data);
  })
  .catch(function(error) {
    console.error("Erro ao realizar a rodada", error);
  });
}

function ataque(playerAttack) {
  var gifElement = document.getElementById("player" + playerAttack + "-gif");
  gifElement.classList.add("player-gif");
  gifElement.style.display = "block";

  var gifPath = "";
  var duration = 0;
  if (playerAttack == 1) {
    gifPath = "images/Tank1Atk.gif";
    duration = 1000;
  } else {
    gifPath = "images/Tank2Atk.gif";
    duration = 1000;
  }

  gifElement.style.backgroundImage = "url('" + gifPath + "')";

  // Restaura a imagem original após a duração definida
  setTimeout(function() {
    gifElement.style.display = "none";
    gifElement.style.backgroundImage = "none";
  }, duration);
}


function defesa(playerDefend) {
  var playerElement = document.getElementById("player" + playerDefend);
  playerElement.classList.add("defense");
  updateHealthBar(playerDefend);
  setTimeout(function() {
    playerElement.classList.remove("defense");
  }, 500);
}

function cura(playerCura) {
  // Adiciona a classe de pulsação ao jogador atual
  var playerElement = document.getElementById("player" + playerCura);
  playerElement.classList.add("pulse");

  // Mostra o ícone "+" durante a pulsação
  var plusIcon = document.getElementById("plusIcon" + playerCura);
  plusIcon.style.display = "inline";

  // Remove a classe de pulsação e oculta o ícone após um tempo
  setTimeout(function() {
    playerElement.classList.remove("pulse");
    plusIcon.style.display = "none";
  }, 1000);
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