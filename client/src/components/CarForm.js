import React, { useState } from 'react';

const CarForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    model: '',
    description: '',
    engine: '',
    car_image: null,
  });

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    setFormData({
      ...formData,
      [name]: files ? files[0] : value,
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
          form {
              display: grid;
              grid-template-columns: 1fr;
              grid-gap: 20px;
              padding: 40px;
              margin: 0 auto;
              max-width: 500px;
          }

          form div {
              position: relative;
              overflow: hidden;
              border: 1px solid #ddd;
              border-radius: 8px;
              box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
          }

          form label {
              display: block;
              margin-bottom: 5px;
              color: #333;
              font-size: 16px;
          }

          form input[type="text"],
          form textarea,
          form input[type="file"] {
              width: calc(100% - 20px);
              padding: 10px;
              margin: 10px;
              border: none;
              outline: none;
          }

          form button[type="submit"] {
              background-color: #FF385C;
              color: white;
              padding: 10px 20px;
              text-align: center;
              text-decoration: none;
              display: block;
              font-size: 16px;
              margin: 8px auto;
              cursor: pointer;
              border: none;
              border-radius: 4px;
              transition: background-color 0.3s ease-in-out;
          }

          form button[type="submit"]:hover {
              background-color: #FF5A5F;
          }
        `}
      </style>
      <form onSubmit={handleSubmit} encType="multipart/form-data">
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="model">Model:</label>
          <input
            type="text"
            id="model"
            name="model"
            value={formData.model}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
          ></textarea>
        </div>
        <div>
          <label htmlFor="engine">Engine:</label>
          <input
            type="text"
            id="engine"
            name="engine"
            value={formData.engine}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="car_image">Car Image:</label>
          <input
            type="file"
            id="car_image"
            name="car_image"
            accept="image/*"
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Add Car</button>
      </form>
    </div>
  );
};

export default CarForm;