import React from 'react';
import { useEffect, useState } from 'react';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Classes() {
  const [classData, setClassData] = useState([]);
  useEffect(() => {
    try {
      axios.get(baseUrl + '/classes/').then((res) => {
        setClassData(res.data);
      });
    } catch (error) {
      console.log(error);
    }
  }, []);

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
                  <span>Class</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="register-section classes-page spad">
        <div className="container">
          <div className="classes-page-text">
            <div className="row">
              <div className="col-lg-8">
                <div className="register-text">
                  <div className="section-title">
                    <h2>Register Now</h2>
                    <p>
                      The First 7 Day Trial Is Completely Free With The Teacher
                    </p>
                  </div>
                  <form action="#" className="register-form">
                    <div className="row">
                      <div className="col-lg-6">
                        <label for="name">First Name</label>
                        <input type="text" id="name" />
                      </div>
                      <div className="col-lg-6">
                        <label for="email">Your email address</label>
                        <input type="text" id="email" />
                      </div>
                      <div className="col-lg-6">
                        <label for="last-name">Last Name</label>
                        <input type="text" id="last-name" />
                      </div>
                      <div className="col-lg-6">
                        <label for="mobile">Mobile No*</label>
                        <input type="text" id="mobile" />
                      </div>
                    </div>
                    <button type="submit" className="register-btn">
                      Get Started
                    </button>
                  </form>
                </div>
              </div>
              <div className="col-lg-4">
                <div className="register-pic">
                  <img src="img/register-pic.jpg" alt="" />
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="classes-section classes-page spad">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="section-title">
                <h2>UNLIMITED CLASSES</h2>
              </div>
            </div>
          </div>
          <div className="row">
            {classData.map((cls, i) => {
              return (
                <div className="col-lg-4 col-md-6">
                  <div
                    className="single-class-item"
                    style={{
                      background: `url(img/classes/classes-${i + 1}.jpg)`,
                    }}
                  >
                    <div className="si-text">
                      <h4>{cls.name}</h4>
                      <span>
                        <i className="fa fa-money"></i>
                        {cls.price}
                      </span>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>
    </React.Fragment>
  );
}