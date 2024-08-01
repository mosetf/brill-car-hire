import React, { useState } from 'react';

const EditProfile = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    password: ''
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
  };

  return (
    <div className="container">
      <style>
        {`
          .container {
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
          }

          h2 {
            color: #FF5A5F;
            font-family: 'Circular', sans-serif;
            text-align: center;
            margin-bottom: 30px;
          }

          form {
            font-family: 'Circular', sans-serif;
          }

          label {
            color: #484848;
            display: block;
            margin-bottom: 8px;
          }

          input {
            border-radius: 4px;
            border: 1px solid #EBEBEB;
            padding: 10px;
            width: 100%;
            margin-bottom: 20px;
          }

          button {
            background-color: #FF5A5F;
            color: white;
            border-radius: 4px;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
            display: block;
            width: 100%;
          }
        `}
      </style>
      <h2>Edit Profile</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="name">Name</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
          size="32"
        />
        <label htmlFor="email">Email</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          size="32"
        />
        <label htmlFor="password">Password</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          size="32"
        />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default EditProfile;