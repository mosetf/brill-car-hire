import React from 'react';
import '../styles/App.css';

const SignUp = () => {
  return (
    <div className="container">
      <form method="POST">
        <h3 style={{ marginBottom: '15px', textAlign: 'center' }}>Sign Up</h3>
        <div className="form-group">
          <label for="email">Email Address</label>
          <input type="email" className="form-control" id="email" name="email" placeholder="Enter email" />
        </div>
        <div className="form-group">
          <label for="id_number">ID number</label>
          <input type="text" className="form-control" id="id_number" name="id_number" placeholder="Enter your ID number" />
        </div>
        <div className="form-group">
          <label for="Phone">Phone</label>
          <input type="text" className="form-control" id="Phone" name="Phone" placeholder="Enter your Phone number" />
        </div>
        <div className="form-group">
          <label for="Name">Name</label>
          <input type="text" className="form-control" id="Name" name="Name" placeholder="Enter your name" />
        </div>
        <div className="form-group">
          <label for="password1">Password</label>
          <input type="password" className="form-control" id="password1" name="password1" placeholder="Enter password" />
        </div>
        <div className="form-group">
          <label for="password2">Password (Confirm)</label>
          <input type="password" className="form-control" id="password2" name="password2" placeholder="Confirm password" />
        </div>
        <button type="submit" className="btn btn-primary">Submit</button>
      </form>
    </div>
  );
};

export default SignUp;