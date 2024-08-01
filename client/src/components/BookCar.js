import React, { useState } from 'react';

const BookCar = () => {
  const [formData, setFormData] = useState({
    car_id: '',
    start_date: '',
    end_date: '',
  });

  const [errors, setErrors] = useState({
    car_id: [],
    start_date: [],
    end_date: [],
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log(formData);
  };

  return (
    <div className="container">
      <style>
        {`
          .container {
              max-width: 600px;
              margin: 50px auto;
              padding: 20px;
              background-color: #fff;
              border-radius: 8px;
              box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
          }

          h2 {
              color: #FF385C;
              text-align: center;
              margin-bottom: 30px;
          }

          .form-group {
              margin-bottom: 20px;
          }

          label {
              display: block;
              margin-bottom: 5px;
              color: #484848;
          }

          .form-control {
              width: 100%;
              padding: 10px;
              border: 1px solid #ddd;
              border-radius: 4px;
              box-sizing: border-box;
          }

          .btn-primary {
              width: 100%;
              padding: 10px;
              border: none;
              border-radius: 4px;
              background-color: #FF385C;
              color: white;
              font-size: 16px;
              cursor: pointer;
              transition: background-color 0.3s ease;
          }

          .btn-primary:hover {
              background-color: #FF5A5F;
          }

          span {
              color: red;
              font-size: 14px;
          }
        `}
      </style>
      <h2>Book a Car</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="car_id">Select Car:</label>
          <input
            type="text"
            id="car_id"
            name="car_id"
            className="form-control"
            value={formData.car_id}
            onChange={handleChange}
            required
          />
          {errors.car_id.map((error, index) => (
            <span key={index}>{error}</span>
          ))}
        </div>
        <div className="form-group">
          <label htmlFor="start_date">Start Date:</label>
          <input
            type="date"
            id="start_date"
            name="start_date"
            className="form-control"
            value={formData.start_date}
            onChange={handleChange}
            required
          />
          {errors.start_date.map((error, index) => (
            <span key={index}>{error}</span>
          ))}
        </div>
        <div className="form-group">
          <label htmlFor="end_date">End Date:</label>
          <input
            type="date"
            id="end_date"
            name="end_date"
            className="form-control"
            value={formData.end_date}
            onChange={handleChange}
            required
          />
          {errors.end_date.map((error, index) => (
            <span key={index}>{error}</span>
          ))}
        </div>
        <div className="form-group">
          <button type="submit" className="btn btn-primary">
            Confirm Booking
          </button>
        </div>
      </form>
    </div>
  );
};

export default BookCar;