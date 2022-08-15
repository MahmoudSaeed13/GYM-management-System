import React from 'react';
import { useState, useEffect } from 'react';

import axios from 'axios';
const baseURL = 'http://127.0.0.1:8000/api';
export default function Home() {
  const [trainerData, setTrainerData] = useState([]);
  const [planData, setPlanData] = useState([]);
  useEffect(() => {
    try {
      axios.get(baseUrl + '/trainers/').then((res) => {
        setTrainerData(res.data);
      });
    } catch (error) {
      console.log(error);
    }
    try {
      axios.get(baseUrl + '/sub/plan/').then((res) => {
        setPlanData(res.data);
      });
    } catch (error) {
      console.log(error);
    }
  }, []);
  return (
    <React.Fragment>
      <section
        className="hero-section"
        style={{
          background: 'url(img/hero-bg.jpg)',
        }}
      >
        <div className="container">
          <div className="row">
            <div className="col-lg-8">
              <div className="hero-text">
                <span>FITNESS ELEMENTS</span>
                <h1>Gutim. Gym Theory</h1>
                <p>
                  All gyms are not created equal. Ours fuse a broad range of
                  high quality equipment with friendly, helpful staff and a
                  culture of support and encouragement for all.
                </p>
                <a
                  href="http://172.20.196.180:3000/signup"
                  className="primary-btn"
                >
                  Sign Up
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="about-section spad">
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <div className="about-pic">
                <img src="img/about-pic.jpg" alt="" />
                <a
                  href="https://www.youtube.com/watch?v=SlPhMPnQ58k"
                  className="play-btn video-popup"
                >
                  <img src="img/play.png" alt="" />
                </a>
              </div>
            </div>
            <div className="col-lg-6">
              <div className="about-text">
                <h2>Story About Us</h2>
                <p className="first-para">
                  <strong>
                    Our clubs are well equipped, conveniently situated and home
                    to some of the friendliest faces in the fitness industry.
                  </strong>
                </p>
                <p className="second-para">
                  We will always try to make every individual that makes up our
                  diverse membership feel right at home when using our cubs.
                  Wherever you are starting from, we’re by your side to help you
                  meet your health and fitness goals.
                </p>
                <a
                  href="http://172.20.196.180:3000/about"
                  className="primary-btn"
                >
                  Read More
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="services-section">
        <div className="container-fluid">
          <div className="row">
            <div className="col-lg-6">
              <div className="services-pic">
                <img src="img/services/service-pic.jpg" alt="" />
              </div>
            </div>
            <div className="col-lg-6">
              <div className="service-items">
                <div className="row">
                  <div className="col-md-6">
                    <div className="services-item bg-gray">
                      <img src="img/services/service-icon-1.png" alt="" />
                      <h4>Strategies</h4>
                      <p>
                        We help every one of our members to be the best they can
                        possibly be, inside and out.
                      </p>
                    </div>
                    <div className="services-item bg-gray pd-b">
                      <img src="img/services/service-icon-3.png" alt="" />
                      <h4>Workout</h4>
                      <p>
                        An overall full body toning workout with a mixture of
                        both body weight and resistance.
                      </p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="services-item">
                      <img src="img/services/service-icon-2.png" alt="" />
                      <h4>Yoga</h4>
                      <p>
                        A class that increases flexibility, mobility, posture
                        and relaxes the mind
                      </p>
                    </div>
                    <div className="services-item pd-b">
                      <img src="img/services/service-icon-4.png" alt="" />
                      <h4>Weight Loss</h4>
                      <p>
                        A high-intensity class using a mixture of treadmills and
                        weights for a full-body workout.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="trainer-section spad">
        <div className="container">
          {trainerData.map(() => {
            return (
              <div>
                <div className="row">
                  <div className="col-lg-12">
                    <div className="section-title">
                      <h2>EXPERT TRAINERS</h2>
                    </div>
                  </div>
                </div>
                <div className="row">
                  <div className="col-lg-4 col-md-6">
                    <div className="single-trainer-item">
                      <img src="{trainerData.image}" />
                      <div className="trainer-text">
                        <h5>{trainerData.name}</h5>
                        <span>
                          {trainerData.experience} Years of Experience.
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <section
        className="banner-section"
        style={{
          background: 'url(img/banner-bg.jpg)',
        }}
      >
        <div className="container">
          <div className="row">
            <div className="col-lg-6">
              <div className="banner-text">
                <h2>Get training today</h2>
                <p>
                  Are you passionate, personable, proactive and positive? Then
                  you need to be part of a fitness family that shares those
                  values.
                </p>
                <a
                  href="http://172.20.196.180:3000/contact"
                  className="primary-btn banner-btn"
                >
                  Contact Now
                </a>
              </div>
            </div>
            <div className="col-lg-5">
              <img src="img/banner-person.png" alt="" />
            </div>
          </div>
        </div>
      </section>

      <section className="membership-section spad">
        <div className="container">
          {trainerData.map(() => {
            return (
              <div>
                <div className="row">
                  <div className="col-lg-4">
                    <div className="membership-item">
                      <div className="mi-title">
                        <h4>{planData.name}</h4>
                        <div className="triangle"></div>
                      </div>
                      <h2 className="mi-price">
                        {planData.price}
                        <span> EGP</span>
                      </h2>
                      <ul>
                        <li>
                          <p>{planData.duration_months} Month</p>
                        </li>
                      </ul>
                      <a
                        href="http://172.20.196.180:3000/signup"
                        className="primary-btn membership-btn"
                      >
                        Start Now
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>

      <section className="register-section spad">
        <div className="container">
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
      </section>
    </React.Fragment>
  );
}
