import React from 'react';

const Header = ({ onLogout, isLoggedIn }) => (
  <header>
    <h1>Blog</h1>
    {isLoggedIn && <button onClick={onLogout}>Выйти</button>}
  </header>
);

export default Header;