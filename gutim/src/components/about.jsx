import React from 'react';

export default function About() {
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
                <h2>About</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>About</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section className="about-section about-page spad">
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
                  rhoncus, gravida quam semper libero sit amet.
                </p>
                <img src="img/about-signature.png" alt="" />
                <div className="at-author">
                  <h4>Lettie Chavez</h4>
                  <span>CEO - Founder</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="about-counter">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <div className="about-counter-text">
                <div className="single-counter">
                  <h1 className="counter-num count">98</h1>
                  <p>Programs</p>
                </div>
                <div className="single-counter">
                  <h1 className="counter-num count">14</h1>
                  <p>Locations</p>
                </div>
                <div className="single-counter">
                  <h1 className="counter-num count">50</h1>
                  <span>k+</span>
                  <p>Members</p>
                </div>
                <div className="single-counter">
                  <h1 className="counter-num count">34</h1>
                  <p>Coaches</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <section className="gym-award spad">
        <div className="container">
          <div className="row">
            <div className="col-lg-8">
              <div className="award-text">
                <h2>Best gym award</h2>
                <p>
                  Lorem ipsum proin gravida nibh vel velit auctor aliquet.
                  Aenean pretium sollicitudin, nascetur auci elit consequat
                  ipsutissem niuis sed odio sit amet nibh vulputate cursus a
                  amet.
                </p>
                <p>
                  Etiam rhoncus. Maecenas tempus, tellus eget condimentum
                  rhoncus, gravida quam semper libero sit amet. Etiam rhoncus.
                  Maecenas tempus, tellus eget condimentum rhoncus, gravida quam
                  semper libero sit amet.
                </p>
              </div>
            </div>
            <div className="col-lg-4">
              <img src="img/award.jpg" alt="" />
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

      <section className="trainer-section about-trainer spad">
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
                <img src="img/trainer/about-trainer-1.jpg" alt="" />
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
                <img src="img/trainer/about-trainer-2.jpg" alt="" />
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
                <img src="img/trainer/about-trainer-3.jpg" alt="" />
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
    </React.Fragment>
  );
}
