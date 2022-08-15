import React from 'react';
import { useState, useEffect } from 'react';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function Events() {
  const [eventData, setEventData] = useState([]);
  useEffect(() => {
    try {
      axios.get(baseUrl + '/events/').then((res) => {
        setEventData(res.data);
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
                <h2>EVENTS</h2>
                <div className="breadcrumb-option">
                  <a href="./index.html">
                    <i className="fa fa-home"></i> Home
                  </a>
                  <span>Events</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section className="membership-section spad" class="my-5">
        <div className="container">
          {eventData.map(() => {
            return (
              <div>
                <div className="row">
                  <div className="col-lg-4">
                    <div className="membership-item">
                      <div className="mi-title">
                        <h4>{eventData.name}</h4>
                        <div className="triangle"></div>
                        <img src="{eventData.image}" />
                      </div>
                      <h2 className="mi-price">
                        {eventData.price}
                        <span>EGP</span>
                      </h2>
                      <ul>
                        <li>
                          <p>Duration</p>
                          <span>
                            {eventData.start_date} to {eventData.end_date}
                          </span>
                        </li>
                        <li>
                          <p>Description</p>
                          <span>{eventData.description}</span>
                        </li>
                        <li>
                          <p>Max. No of Attendants</p>
                          <span>{eventData.capacity}</span>
                        </li>
                        <li>
                          <p>Number of Participants</p>
                          <span>{eventData.event_participants}</span>
                        </li>
                      </ul>
                      <a href="#!" className="primary-btn membership-btn">
                        Going
                      </a>
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
