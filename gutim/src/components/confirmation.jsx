import React from 'react';
import Footer from './footer';
import Header from './header';

export default function Confirmation() {
  return (
    <React.Fragment>
      <Header />
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
                <h2>Confirmation</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Confirmation</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="container">
        <h1 className="text-center m-5">
          Thanks for Registring at <span className="text-success">Gutim </span>
          Please Verify your email.
        </h1>
        <div className="text-center">
          <img src="/images/goodbye.jpeg" alt="" />
        </div>
      </div>
      <Footer />
    </React.Fragment>
  );
}
