import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { setAuth } from '../redux/reducers/authSlice';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Login() {
  const dispatch = useDispatch();
  const [error, setError] = useState({});
  const [state, setState] = useState({
    email: '',
    password: '',
  });
  const nav = useNavigate();
  const getUsername = (e) => {
    setState({
      ...state,
      username: e.target.value,
    });
  };
  const getPassword = (e) => {
    setState({
      ...state,
      password: e.target.value,
    });
  };
  const submitLogin = (e) => {
    e.preventDefault();
    axios
      .post(`${baseUrl}/users/login/`, state)
      .then((res) => {
        console.log(res.data);
        setError({});
      })
      .catch((err) => setError({ ...err }));
    // dispatch(setAuth(true));
    // nav('/');
  };

  return (
    <React.Fragment>
      <section
        className="breadcrumb-section"
        style={{
          background: 'url(img/breadcrumb/classes-breadcrumb.jpg)',
        }}
      >
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="breadcrumb-text">
                <h2>Classes</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Login</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div
        className="w-75 mx-auto"
        style={{
          height: '60vh',
          display: 'flex',
          alignItems: 'center',
          paddingTop: '20px',
          paddingBottom: '20px',
        }}
      >
        <main className="form-signin w-100 m-auto">
          <form onSubmit={submitLogin}>
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>
            <div className="form-floating my-2">
              <input
                type="text"
                className="form-control"
                id="floatingInput"
                placeholder="Jxhn"
                onChange={getUsername}
              />
              <label for="floatingInput">Username</label>
            </div>
            <div className="form-floating my-2">
              <input
                type="password"
                className="form-control"
                id="floatingPassword"
                placeholder="Password"
                onChange={getPassword}
              />
              <label for="floatingPassword">Password</label>
            </div>
            <p className="text-danger">{error?.response?.data?.detail}</p>
            <button className="w-100 btn btn-lg btn-primary" type="submit">
              Sign in
            </button>
          </form>
        </main>
      </div>
    </React.Fragment>
  );
}
