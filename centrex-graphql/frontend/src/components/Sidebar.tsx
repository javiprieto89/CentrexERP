// centrex-graphql/frontend/src/components/Sidebar.tsx
import React from 'react';
import entities from '../data/entities';

const Sidebar: React.FC = () => (
  <aside className="w-60 bg-gray-800 text-white p-4 space-y-2 overflow-y-auto">
    {entities.map((e) => (
      <div key={e} className="hover:bg-gray-700 p-2 rounded">
        {e}
      </div>
    ))}
  </aside>
);

export default Sidebar;
