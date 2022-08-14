import React from 'react';

export default function Gallery() {
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
                <h2>Gallery</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Gallery</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div className="gallery-section spad">
        <div className="container">
          <div className="row">
            <div className="col-lg-12">
              <ul className="gallery-controls">
                <li className="active" data-filter=".all">
                  all gallery
                </li>
                <li data-filter=".fitness">fitness</li>
                <li data-filter=".coaching">coaching</li>
                <li data-filter=".event">event</li>
                <li data-filter=".other">other</li>
              </ul>
            </div>
          </div>
          <div className="row gallery-filter">
            <div className="col-lg-6 mix all fitness">
              <img src="img/gallery/gallery-1.jpg" alt="" />
            </div>
            <div className="col-lg-6">
              <div className="row">
                <div className="col-lg-6 mix all fitness coaching">
                  <img src="img/gallery/gallery-2.jpg" alt="" />
                </div>
                <div className="col-lg-6">
                  <div className="row">
                    <div className="col-lg-12 mix all coaching">
                      <img src="img/gallery/gallery-3.jpg" alt="" />
                    </div>
                    <div className="col-lg-12 mix all coaching">
                      <img src="img/gallery/gallery-4.jpg" alt="" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div className="col-lg-6">
              <div className="row">
                <div className="col-lg-6 mix all other">
                  <img src="img/gallery/gallery-5.jpg" alt="" />
                </div>
                <div className="col-lg-6 mix all other">
                  <img src="img/gallery/gallery-6.jpg" alt="" />
                </div>
              </div>
            </div>
            <div className="col-lg-6 mix all event">
              <img src="img/gallery/gallery-7.jpg" alt="" />
            </div>
          </div>
        </div>
      </div>
    </React.Fragment>
  );
}
