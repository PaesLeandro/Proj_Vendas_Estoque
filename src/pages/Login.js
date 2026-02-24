import React, { useState } from 'react';
import api from '../services/api';

const Login = () => {
  const [login, setLogin] = useState('');
  const [senha, setSenha] = useState('');

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post('/login', { login, senha });
      const { access_token } = response.data;

      // Salva o token para persistência
      localStorage.setItem('token', access_token);
      
      alert('Login realizado com sucesso!');
      window.location.href = '/dashboard'; // Redireciona
    } catch (error) {
      alert('Falha no login: ' + error.response?.data?.erro);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <h2>Acesso ao Sistema de Vendas</h2>
      <input type="text" placeholder="Login" onChange={e => setLogin(e.target.value)} />
      <input type="password" placeholder="Senha" onChange={e => setSenha(e.target.value)} />
      <button type="submit">Entrar</button>
    </form>
  );
};

export default Login;