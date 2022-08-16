import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Branches() {
  const [branchData, setBranchData] = useState([]);
  useEffect(() => {
    try {
      axios.get(baseUrl + '/branch/').then((res) => {
        setBranchData(res.data);
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
                <h2>Branches</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Branches</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="membership-section spad" class="my-5">
        <div className="container">
          {branchData.map(() => {
            return (
              <div>
                <div className="row">
                  <div className="col-lg-4">
                    <div className="membership-item">
                      <div className="mi-title">
                        <h4>{branchData.name}</h4>
                        <div className="triangle"></div>
                      </div>
                      <h2 className="mi-price">
                        <span><i class="fa-solid fa-phone"></i></span>
                        {branchData.phone}
                      </h2>
                      <ul>
                        <li>
                          <p>Description</p>
                          <span>{branchData.description}</span>
                        </li>
                        <li>
                          <p>Address</p>
                          <span>{branchData.address}</span>
                        </li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </React.Fragment>
  );
}
