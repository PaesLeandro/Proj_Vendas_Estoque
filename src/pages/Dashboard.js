import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import api from '../services/api';

const Dashboard = () => {
    const [dados, setDados] = useState([]);

    useEffect(() => {
        api.get('/relatorio/faturamento')
            .then(response => setDados(response.data))
            .catch(err => console.error("Erro ao carregar relatório", err));
    }, []);

    return (
        <div style={{ width: '100%', height: 400 }}>
            <h3>Faturamento Diário (Análise Pandas)</h3>
            <ResponsiveContainer>
                <LineChart data={dados}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="data" />
                    <YAxis />
                    <Tooltip />
                    <Line type="monotone" dataKey="valor" stroke="#8884d8" strokeWidth={2} />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

export default Dashboard;