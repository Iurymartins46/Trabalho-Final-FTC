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