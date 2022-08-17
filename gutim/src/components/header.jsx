import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setAuth } from '../redux/reducers/authSlice';
import { NavLink } from 'react-router-dom';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Header() {
  const dispatch = useDispatch();
  const auth = useSelector((state) => state.auth.value);
  if (localStorage.getItem('refresh')) {
    dispatch(setAuth(true));
  }
  if (auth) {
    setInterval(() => {
      axios
        .post(
          `${baseUrl}/users/token/refresh/`,
          {
            refresh: localStorage.getItem('refresh'),
          },
          {
            headers: {
              Authorization: `Bearer ${localStorage.getItem('access')}`,
            },
          }
        )
        .then((res) => {
          localStorage.setItem('access', res.data.access);
        })
        .catch((err) => {
          console.log(err);
        });
    }, 240000);
  }
  const logout = () => {
    axios
      .post(
        `${baseUrl}/users/logout/`,
        {
          refresh: localStorage.getItem('refresh'),
        },
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('access')}`,
          },
        }
      )
      .then((res) => {
        localStorage.removeItem('refresh');
        localStorage.removeItem('access');
        dispatch(setAuth(false));
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };
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
            {!auth && (
              <NavLink to="/signup" className="primary-btn signup-btn">
                Sign Up Today
              </NavLink>
            )}
            {auth && (
              <button
                className="btn btn-outline-danger signup-btn"
                onClick={logout}
              >
                Logout
              </button>
            )}
          </div>
          <div id="mobile-menu-wrap"></div>
        </div>
      </header>
    </React.Fragment>
  );
}
