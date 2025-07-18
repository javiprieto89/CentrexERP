// centrex-graphql/frontend/src/pages/Dashboard.tsx
import React from 'react';
import Header from '../components/Header';
import Sidebar from '../components/Sidebar';
import { clearToken } from '../utils/auth';

interface Props {
  onLogout: () => void;
}

const Dashboard: React.FC<Props> = ({ onLogout }) => {
  const handleLogout = () => {
    clearToken();
    onLogout();
  };

  return (
    <div className="flex h-screen">
      <Sidebar />
      <div className="flex-1 flex flex-col">
        <Header onLogout={handleLogout} />
        <main className="p-4">Bienvenido al dashboard</main>
      </div>
    </div>
  );
};

export default Dashboard;
