import React from 'react';
import { Link } from 'react-router-dom';

const LoginPage = () => {
  return (
    <div className="container">
      <style>
        {`
          .container {
            max-width: 500px;
            padding: 40px;
            margin: 0 auto;
          }

          form {
            display: grid;
            grid-template-columns: 1fr;
            grid-gap: 20px;
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

          form input[type="email"],
          form input[type="password"] {
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
      <form method="POST">
        <h3 style={{ marginBottom: '15px', textAlign: 'center' }}>Login</h3>
        <div className="form-group">
          <label htmlFor="email">Email Address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            placeholder="Enter email"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            placeholder="Enter password"
          />
        </div>
        <button type="submit" className="btn btn-primary">Login</button>
      </form>
      <p style={{ textAlign: 'center', marginTop: '20px' }}>
        Don't have an account? <Link to="/sign-up">Sign Up</Link>
      </p>
    </div>
  );
};

export default LoginPage;