import React, { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Signup() {
  const nav = useNavigate();
  const [error, setError] = useState({});
  const [state, setState] = useState({
    name: '',
    username: '',
    email: '',
    password: '',
    password_confirmation: '',
  });
  const getName = (e) => {
    setState({
      ...state,
      name: e.target.value,
    });
  };
  const getUsername = (e) => {
    setState({
      ...state,
      username: e.target.value,
    });
  };
  const getEmail = (e) => {
    setState({
      ...state,
      email: e.target.value,
    });
  };
  const getPassword = (e) => {
    setState({
      ...state,
      password: e.target.value,
      password_confirmation: e.target.value,
    });
  };
  const submitSignup = (e) => {
    e.preventDefault();
    let errors = {};
    if (!state.name) {
      errors.name = 'Name is Required';
    } else if (state.name.length < 8) {
      errors.name = 'Name must be greater than 8 character';
    } else if (!/^[a-zA-Z\s]+$/.test(state.name)) {
      errors.name = 'Name must be String';
    }
    if (!state.username) {
      errors.username = 'Username is Required';
    } else if (state.name.length < 8) {
      errors.username = 'Username must be greater than 8 character';
    } else if (!/^[a-zA-Z\s]+$/.test(state.username)) {
      errors.username = 'Username must be String';
    }
    if (!state.email) {
      errors.email = 'Email is Required';
    } else if (!/^\S+@\S+\.\S+$/.test(state.email)) {
      errors.email = 'Invalid Email';
    }
    if (!state.password) {
      errors.password = 'Password is Required';
    } else if (state.password.length < 8) {
      errors.password = 'Password must be greater than 8 character';
    }
    setError({ ...errors });
    if (!Object.keys(errors).length) {
      axios
        .post(`${baseUrl}/users/register/`, state)
        .then((res) => console.log(res))
        .catch((e) => console.log(e));
      nav('/confirmation');
    }
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
                  <span>Sign up</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div
        className="w-75 mx-auto"
        style={{
          height: '80vh',
          display: 'flex',
          alignItems: 'center',
          paddingTop: '20px',
          paddingBottom: '20px',
        }}
      >
        <main className="form-signin w-100 m-auto">
          <form onSubmit={submitSignup}>
            <h1 className="h3 mb-3 fw-normal">Please sign up</h1>
            <div className="form-floating my-2">
              <input
                type="text"
                className="form-control"
                id="floatingName"
                placeholder="John Doe"
                onChange={getName}
              />
              <label for="floatingName">Name</label>
            </div>
            <p className="text-danger">{error.name}</p>
            <div className="form-floating my-2">
              <input
                type="text"
                className="form-control"
                id="floatingUsername"
                placeholder="Jxhn"
                onChange={getUsername}
              />
              <label for="floatingUsername">Username</label>
            </div>
            <p className="text-danger">{error.username}</p>
            <div className="form-floating my-2">
              <input
                type="email"
                className="form-control"
                id="floatingInput"
                placeholder="name@example.com"
                onChange={getEmail}
              />
              <label for="floatingInput">Email address</label>
            </div>
            <p className="text-danger">{error.email}</p>
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
            <p className="text-danger">{error.password}</p>
            <button className="w-100 btn btn-lg btn-outline-dark" type="submit">
              Sign up
            </button>
          </form>
          <p className="fs-5 mt-4">
            Have an acount{' '}
            <NavLink className="text-success" to="/login">
              Login
            </NavLink>
          </p>
        </main>
      </div>
    </React.Fragment>
  );
}
