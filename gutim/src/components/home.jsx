import React from 'react';

export default function Home() {
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
                <h1>BMI CALCULATOR</h1>
                <p>
                  Gutim comes packed with the user-friendly BMI Calculator
                  <br />
                  shortcode which lets
                </p>
                <a href="#!" className="primary-btn">
                  Read More
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
                  Lorem ipsum proin gravida nibh vel velit auctor aliquet.
                  Aenean pretium sollicitudin, nascetur auci elit consequat
                  ipsutissem niuis sed odio sit amet nibh vulputate cursus a
                  amet.
                </p>
                <p className="second-para">
                  Etiam rhoncus. Maecenas tempus, tellus eget condimentum
                  rhoncus, gravida quam semper libero sit amet. Etiam rhoncus.
                  Maecenas tempus, tellus eget condimentum rhoncus, gravida quam
                  semper libero sit amet.
                </p>
                <a href="#!" className="primary-btn">
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
                        Aenean massa. Cum sociis Theme et natoque penatibus et
                        magnis dis part urient montes.
                      </p>
                    </div>
                    <div className="services-item bg-gray pd-b">
                      <img src="img/services/service-icon-3.png" alt="" />
                      <h4>Workout</h4>
                      <p>
                        Aenean massa. Cum sociis Theme et natoque penatibus et
                        magnis dis part urient montes.
                      </p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="services-item">
                      <img src="img/services/service-icon-2.png" alt="" />
                      <h4>Yoga</h4>
                      <p>
                        Aenean massa. Cum sociis Theme et natoque penatibus et
                        magnis dis part urient montes.
                      </p>
                    </div>
                    <div className="services-item pd-b">
                      <img src="img/services/service-icon-4.png" alt="" />
                      <h4>Weight Loss</h4>
                      <p>
                        Aenean massa. Cum sociis Theme et natoque penatibus et
                        magnis dis part urient montes.
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
                <img src="img/trainer/trainer-1.jpg" alt="" />
                <div className="trainer-text">
                  <h5>Patrick Cortez</h5>
                  <span>Leader</span>
                  <p>
                    non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem.
                  </p>
                  <div className="trainer-social">
                    <a href="#!">
                      <i className="fa fa-facebook"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-instagram"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-twitter"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-pinterest"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-4 col-md-6">
              <div className="single-trainer-item">
                <img src="img/trainer/trainer-2.jpg" alt="" />
                <div className="trainer-text">
                  <h5>Gregory Powers</h5>
                  <span>Gym coach</span>
                  <p>
                    non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem.
                  </p>
                  <div className="trainer-social">
                    <a href="#!">
                      <i className="fa fa-facebook"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-instagram"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-twitter"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-pinterest"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-4 col-md-6">
              <div className="single-trainer-item">
                <img src="img/trainer/trainer-3.jpg" alt="" />
                <div className="trainer-text">
                  <h5>Walter Wagner</h5>
                  <span>Dance trainer</span>
                  <p>
                    non numquam eius modi tempora incidunt ut labore et dolore
                    magnam aliquam quaerat voluptatem.
                  </p>
                  <div className="trainer-social">
                    <a href="#!">
                      <i className="fa fa-facebook"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-instagram"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-twitter"></i>
                    </a>
                    <a href="#!">
                      <i className="fa fa-pinterest"></i>
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
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
                  Gimply dummy text of the printing and typesetting industry.
                  Lorem Ipsum has been the industry’s standard.
                </p>
                <a href="#!" className="primary-btn banner-btn">
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
          <div className="row">
            <div className="col-lg-12">
              <div className="section-title">
                <h2>MEMBERSHIP PLANS</h2>
              </div>
            </div>
          </div>
          <div className="row">
            <div className="col-lg-4">
              <div className="membership-item">
                <div className="mi-title">
                  <h4>Basic</h4>
                  <div className="triangle"></div>
                </div>
                <h2 className="mi-price">
                  $17<span>/01 mo</span>
                </h2>
                <ul>
                  <li>
                    <p>Duration</p>
                    <span>12 months</span>
                  </li>
                  <li>
                    <p>Personal trainer</p>
                    <span>00 person</span>
                  </li>
                  <li>
                    <p>Amount of people</p>
                    <span>01 person</span>
                  </li>
                  <li>
                    <p>Number of visits</p>
                    <span>Unlimited</span>
                  </li>
                </ul>
                <a href="#!" className="primary-btn membership-btn">
                  Start Now
                </a>
              </div>
            </div>
            <div className="col-lg-4">
              <div className="membership-item">
                <div className="mi-title">
                  <h4>Standard</h4>
                  <div className="triangle"></div>
                </div>
                <h2 className="mi-price">
                  $57<span>/01 mo</span>
                </h2>
                <ul>
                  <li>
                    <p>Duration</p>
                    <span>12 months</span>
                  </li>
                  <li>
                    <p>Personal trainer</p>
                    <span>01 person</span>
                  </li>
                  <li>
                    <p>Amount of people</p>
                    <span>01 person</span>
                  </li>
                  <li>
                    <p>Number of visits</p>
                    <span>Unlimited</span>
                  </li>
                </ul>
                <a href="#!" className="primary-btn membership-btn">
                  Start Now
                </a>
              </div>
            </div>
            <div className="col-lg-4">
              <div className="membership-item">
                <div className="mi-title">
                  <h4>Premium</h4>
                  <div className="triangle"></div>
                </div>
                <h2 className="mi-price">
                  $98<span>/01 mo</span>
                </h2>
                <ul>
                  <li>
                    <p>Duration</p>
                    <span>12 months</span>
                  </li>
                  <li>
                    <p>Personal trainer</p>
                    <span>01 person</span>
                  </li>
                  <li>
                    <p>Amount of people</p>
                    <span>01 person</span>
                  </li>
                  <li>
                    <p>Number of visits</p>
                    <span>Unlimited</span>
                  </li>
                </ul>
                <a href="#!" className="primary-btn membership-btn">
                  Start Now
                </a>
              </div>
            </div>
          </div>
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
