// centrex-graphql/frontend/src/components/Header.tsx
import React from 'react';

interface Props {
  onLogout: () => void;
}

const Header: React.FC<Props> = ({ onLogout }) => (
  <header className="bg-blue-600 text-white p-4 flex justify-between">
    <h1 className="font-bold">Centrex ERP</h1>
    <button onClick={onLogout} className="underline">
      Cerrar sesión
    </button>
  </header>
);

export default Header;
