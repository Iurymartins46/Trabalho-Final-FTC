const baseUrl = 'http://127.0.0.1:5000';

const listarArquivos = async () => {
  try {
    const response = await axios.get(`${baseUrl}/listarArquivos`);
    return response.data.arquivos;
  } catch (error) {
    console.error('Erro ao obter a lista de arquivos:', error);
    return [];
  }
};

const escolherMaquina = async (maquina1, maquina2) => {
  try {
    const response = await axios.post(`${baseUrl}/escolherMaquina`, {
      player1: maquina1,
      player2: maquina2,
    });
    console.log('Maquinas Iniciadas', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro ao obter a lista de arquivos:', error);
    return null;
  }
}

const rodada = async (entrada) => {
  try {
    const response = await axios.post(`${baseUrl}/rodada`, {
      entrada: entrada
    });
    console.log('Rodada Executada', response.data);
    return response.data;
  } catch (error) {
    console.error('Erro ao obter a lista de arquivos:', error);
    return null;
  }
}