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
          src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d24112.92132811736!2d-74.20651812810036!3d40.93514309648714!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c2fda38587e887%3A0xf03207815e338a0d!2sHaledon%2C%20NJ%2007508%2C%20USA!5e0!3m2!1sen!2sbd!4v1578120776078!5m2!1sen!2sbd"
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
                      <p>60-49 Road 11378 New York</p>
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
                      <p>hellocolorlib@ gmail.com</p>
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
