const realizarVenda = async (clienteId, listaProdutos) => {
  try {
    const dadosVenda = {
      cliente_id: clienteId,
      itens: listaProdutos // Ex: [{produto_id: 1, quantidade: 5}]
    };

    const response = await api.post('/registrar_venda', dadosVenda);
    console.log('Venda OK:', response.data);
    alert('Venda e estoque atualizados!');
  } catch (error) {
    console.error('Erro na venda:', error.response.data);
  }
};