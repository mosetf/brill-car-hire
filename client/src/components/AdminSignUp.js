import React, { useState } from 'react';
import BaseLayout from './BaseLayout';

const AdminSignUp = () => {
  const [formData, setFormData] = useState({
    email: '',
    id_number: '',
    phone: '',
    name: '',
    password1: '',
    password2: ''
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
  };

  return (
    <BaseLayout title="Admin Sign Up">
      <form onSubmit={handleSubmit}>
        <h3 align="center">Admin Sign Up</h3>
        <div className="form-group">
          <label htmlFor="email">Email Address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            placeholder="Enter email"
            required
            value={formData.email}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="id_number">ID number</label>
          <input
            type="text"
            className="form-control"
            id="id_number"
            name="id_number"
            placeholder="Enter your ID number"
            required
            value={formData.id_number}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="phone">Phone</label>
          <input
            type="text"
            className="form-control"
            id="phone"
            name="phone"
            placeholder="Enter your Phone number"
            required
            value={formData.phone}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            type="text"
            className="form-control"
            id="name"
            name="name"
            placeholder="Enter your name"
            required
            value={formData.name}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password1">Password</label>
          <input
            type="password"
            className="form-control"
            id="password1"
            name="password1"
            placeholder="Enter password"
            required
            value={formData.password1}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password2">Password (Confirm)</label>
          <input
            type="password"
            className="form-control"
            id="password2"
            name="password2"
            placeholder="Confirm password"
            required
            value={formData.password2}
            onChange={handleChange}
          />
        </div>
        <br />
        <button type="submit" className="btn btn-primary">Register Admin</button>
      </form>
    </BaseLayout>
  );
};

export default AdminSignUp;