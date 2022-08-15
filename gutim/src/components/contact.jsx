import React from 'react';

export default function Contact() {
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
                <h2>Contact</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Contact</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="map">
        <iframe
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d27285.30437547654!2d29.994362657675627!3d31.257749913247157!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14f5c52e0c4b1135%3A0x79b9f57984645d94!2sGold&#39;s%20Gym%20Elite%20San%20Stefano!5e0!3m2!1sar!2seg!4v1660570409480!5m2!1sar!2seg"
          title="map"
          height="612"
          style={{
            border: '0',
          }}
          allowfullscreen=""
        ></iframe>
        <img src="img/icon/location.png" alt="" />
      </div>

      <section className="contact-section spad">
        <div className="container">
          <div className="row">
            <div className="col-lg-4">
              <div className="contact-info">
                <h4>Contacts Us</h4>
                <div className="contact-address">
                  <div className="ca-widget">
                    <div className="cw-icon">
                      <img src="img/icon/icon-1.png" alt="" />
                    </div>
                    <div className="cw-text">
                      <h5>Our Location</h5>
                      <p>7 San Stifano, Alexandria, Egypt</p>
                    </div>
                  </div>
                  <div className="ca-widget">
                    <div className="cw-icon">
                      <img src="img/icon/icon-2.png" alt="" />
                    </div>
                    <div className="cw-text">
                      <h5>Phone:</h5>
                      <p>+65 11.188.888</p>
                    </div>
                  </div>
                  <div className="ca-widget">
                    <div className="cw-icon">
                      <img src="img/icon/icon-3.png" alt="" />
                    </div>
                    <div className="cw-text">
                      <h5>Mail</h5>
                      <p>gutimgym@gmail.com</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-8">
              <div className="contact-form">
                <h4>Leave A Comment</h4>
                <form action="#">
                  <div className="row">
                    <div className="col-lg-6">
                      <input type="text" placeholder="Your name" />
                    </div>
                    <div className="col-lg-6">
                      <input type="text" placeholder="Your email" />
                    </div>
                    <div className="col-lg-12">
                      <textarea placeholder="Your messages"></textarea>
                      <button type="submit">Send Message</button>
                    </div>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </section>
    </React.Fragment>
  );
}
