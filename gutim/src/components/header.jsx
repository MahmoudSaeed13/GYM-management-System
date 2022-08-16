import React from 'react';
import { NavLink } from 'react-router-dom';

export default function Header() {
  return (
    <React.Fragment>
      <header className="header-section">
        <div className="container">
          <div className="logo">
            <NavLink to="/">
              <img src="img/logo.png" alt="" />
            </NavLink>
          </div>
          <div className="nav-menu">
            <nav className="mainmenu mobile-menu">
              <ul>
                <li className="active">
                  <NavLink to="/">Home</NavLink>
                </li>
                <li>
                  <NavLink to="/branch">Branches</NavLink>
                </li>
                <li>
                  <NavLink to="/classes">Classes</NavLink>
                </li>
                <li>
                  <NavLink to="/event">Events</NavLink>
                </li>
                <li>
                  <NavLink to="/gallery">Gallery</NavLink>
                </li>
                <li>
                  <NavLink to="/contact">Contact Us</NavLink>
                </li>
                <li>
                  <NavLink to="/about">About</NavLink>
                </li>
              </ul>
            </nav>
            <NavLink to="/signup" className="primary-btn signup-btn">
              Sign Up Today
            </NavLink>
          </div>
          <div id="mobile-menu-wrap"></div>
        </div>
      </header>
    </React.Fragment>
  );
}
