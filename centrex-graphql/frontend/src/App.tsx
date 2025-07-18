// centrex-graphql/frontend/src/App.tsx
import React, { useState, useEffect } from 'react';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import { getToken } from './utils/auth';

const App: React.FC = () => {
  const [token, setToken] = useState<string | null>(null);

  useEffect(() => {
    setToken(getToken());
  }, []);

  return token ? <Dashboard onLogout={() => setToken(null)} /> : <Login onLogin={setToken} />;
};

export default App;
