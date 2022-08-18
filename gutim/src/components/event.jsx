import React from 'react';
import Paypal from './paypal';
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
          <div className="row">
            <div className="col-lg-12">
              <div className="section-title">
                <h2>Events</h2>
              </div>
            </div>
          </div>
          <div className="row">
            {eventData.map((event) => {
              return (
                <div className="col-lg-4">
                  <div
                    className="membership-item"
                    style={{
                      height: '610px',
                      overflow: 'hidden',
                    }}
                  >
                    <div className="mi-title">
                      <h4>{event.name}</h4>
                      <div className="triangle"></div>
                      <img src="{event.image}" alt="" />
                    </div>
                    <h2 className="mi-price">
                      {event.price}
                      <span> USD</span>
                    </h2>
                    <ul>
                      <li>
                        <p>Duration</p>
                        <span>
                          {event.start_date} to {event.end_date}
                        </span>
                      </li>
                      <li>
                        <p>Description</p>
                        <span>{event.description}</span>
                      </li>
                      <li>
                        <p>Max. No of Attendants</p>
                        <span>{event.capacity}</span>
                      </li>
                    </ul>
                    <p className="fs-3">Buy a Ticket</p>
                    <div className="w-75 mx-auto">
                      <Paypal name={event.name} price={event.price} />
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
