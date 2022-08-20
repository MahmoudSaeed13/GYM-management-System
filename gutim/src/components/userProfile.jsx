import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
const baseUrl = 'http://127.0.0.1:8000/api';

export default function UserProfile() {
  const nav = useNavigate();
  const id = localStorage.getItem('user_id');
  const auth = useSelector((state) => state.auth.value);
  const [profileData, setProfileData] = useState([]);
  useEffect(() => {
    if (!auth) {
      nav('/');
    }
    axios
      .get(`${baseUrl}/users/profile/${id}`)
      .then((res) => {
        setProfileData(res.data);
      })
      .catch((err) => console.log(err));
  }, []);

  const [userData, setUserData] = useState({
    name: '',
    age: '',
    phone: '',
    height: '',
    weight: '',
    image: '',
    gender: '',
  });

  const handleChange = (e) => {
    setUserData({
      ...userData,
      [e.target.name]: e.target.value,
    });
  };

  const handleFileChange = (e) => {
    setUserData({
      ...userData,
      [e.target.name]: e.target.files[0],
    });
  };

  const submitForm = () => {
    const userFormData = new FormData();
    userFormData.append('name', userData.name);
    userFormData.append('age', userData.age);
    userFormData.append('phone', userData.phone);
    userFormData.append('height', userData.height);
    userFormData.append('weight', userData.weight);
    userFormData.append('image', userData.image);
    userFormData.append('gender', userData.gender);

    axios
      .post(`${baseUrl}/users/profile/${id}`, userFormData, {
        headers: {
          'content-type': 'multipart/form-data',
        },
      })
      .then((res) => {
        setUserData({
          name: '',
          age: '',
          phone: '',
          height: '',
          weight: '',
          image: '',
          gender: '',
        });
        console.log(res);
      })
      .catch((err) => console.log(err));
  };

  return (
    <div className="content-wrapper">
      <section className="content-header">
        <div className="container-fluid">
          <div className="row mb-2">
            <div className="col-sm-6">
              <h1>Profile</h1>
            </div>
            <div className="col-sm-6">
              <ol className="breadcrumb float-sm-right">
                <li className="breadcrumb-item">
                  <a href="#!">Home</a>
                </li>
                <li className="breadcrumb-item active">User Profile</li>
              </ol>
            </div>
          </div>
        </div>
      </section>

      <section className="content">
        <div className="container-fluid">
          <div className="row">
            <div className="col-12">
              <div className="card card-primary card-outline">
                <div className="card-body box-profile">
                  <div className="text-center">
                    <img
                      className="profile-user-img img-fluid img-circle"
                      src="../../dist/img/user4-128x128.jpg"
                      alt=""
                    />
                  </div>
                  <h3 className="profile-username text-center">
                    {profileData}
                  </h3>
                  <p className="text-muted text-center">Trainee</p>
                  <ul className="list-group list-group-unbordered mb-3">
                    <li className="list-group-item">
                      <b>Phone</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.phone}
                      </a>
                    </li>
                    <li className="list-group-item">
                      <b>Age</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.age}
                      </a>
                    </li>
                    <li className="list-group-item">
                      <b>Height</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.height}
                      </a>
                    </li>
                    <li className="list-group-item">
                      <b>Weight</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.weight}
                      </a>
                    </li>
                    <li className="list-group-item">
                      <b>BMI</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.bmi}
                      </a>
                    </li>
                    <li className="list-group-item">
                      <b>Gender</b>{' '}
                      <a className="float-right" href="#!">
                        {profileData.gender}
                      </a>
                    </li>
                  </ul>
                  <div className="d-flex justify-content-center">
                    <a
                      className="btn btn-danger w-50"
                      data-toggle="modal"
                      data-target="#editProfile"
                      href="#!"
                    >
                      Edit Profile
                    </a>
                  </div>
                </div>
              </div>
            </div>

            <div className="col-9">
              <div
                className="modal fade"
                id="editProfile"
                tabIndex={-1}
                aria-labelledby="exampleModalLabel"
                aria-hidden="true"
              >
                <div className="modal-dialog">
                  <div className="modal-content">
                    <div className="modal-header">
                      <ul className="nav nav-pills">
                        <li className="nav-item">Edit Profile</li>
                      </ul>
                      <button
                        type="button"
                        className="close"
                        data-dismiss="modal"
                        aria-label="Close"
                      >
                        <span aria-hidden="true">×</span>
                      </button>
                    </div>
                    <div className="modal-body">
                      <div className="tab-content">
                        <div className="active tab-pane" id="editProfile">
                          <form className="form-horizontal">
                            <div className="form-group row">
                              <label
                                htmlFor="inputName"
                                className="col-sm-2 col-form-label"
                              >
                                Name
                              </label>
                              <div className="col-sm-10">
                                <input
                                  type="email"
                                  className="form-control"
                                  name="name"
                                  placeholder="Name"
                                  value={profileData}
                                  onChange={handleChange}
                                />
                              </div>
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="inputEmail"
                                className="col-sm-2 col-form-label"
                              >
                                Age
                              </label>
                              <div className="col-sm-10">
                                <input
                                  type="text"
                                  className="form-control"
                                  name="age"
                                  placeholder="Age"
                                  value={profileData.age}
                                  onChange={handleChange}
                                />
                              </div>
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="inputName"
                                className="col-sm-2 col-form-label"
                              >
                                Phone
                              </label>
                              <div className="col-sm-10">
                                <input
                                  type="text"
                                  className="form-control"
                                  name="phone"
                                  placeholder="Phone"
                                  value={profileData.phone}
                                  onChange={handleChange}
                                />
                              </div>
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="inputName2"
                                className="col-sm-2 col-form-label"
                              >
                                Height
                              </label>
                              <div className="col-sm-10">
                                <input
                                  type="text"
                                  className="form-control"
                                  name="height"
                                  placeholder="Height"
                                  value={profileData.height}
                                  onChange={handleChange}
                                  required
                                />
                              </div>
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="inputName2"
                                className="col-sm-2 col-form-label"
                              >
                                Weight
                              </label>
                              <div className="col-sm-10">
                                <input
                                  type="text"
                                  className="form-control"
                                  name="weight"
                                  placeholder="Weight"
                                  value={profileData.height}
                                  onChange={handleChange}
                                  required
                                />
                              </div>
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="formFile"
                                className="col-sm-2 col-form-label"
                              >
                                Image
                              </label>
                              <input
                                className="col-sm-10"
                                name="image"
                                type="file"
                                value="{profileData.image}"
                                onChange={handleFileChange}
                              />
                            </div>
                            <div className="form-group row">
                              <label
                                htmlFor="inputSkills"
                                className="col-sm-2 col-form-label"
                              >
                                Gender
                              </label>
                              <div className="col-sm-10">
                                <select
                                  className="form-select"
                                  name="gender"
                                  onChange={handleChange}
                                  aria-label="Default select example"
                                >
                                  <option selected>{profileData.gender}</option>
                                  <option value="male">Male</option>
                                  <option value="female">Female</option>
                                </select>
                              </div>
                            </div>
                          </form>
                        </div>
                      </div>
                    </div>
                    <div className="modal-footer">
                      <button
                        type="button"
                        className="btn btn-secondary"
                        data-dismiss="modal"
                      >
                        Close
                      </button>
                      <button
                        type="button"
                        className="btn btn-primary"
                        onClick={submitForm}
                      >
                        Submit
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
