import React from 'react';

const UserDashboard = ({ bookings }) => {
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
            color: #FF385C;
            text-align: center;
            margin-bottom: 30px;
          }

          .table {
            border-collapse: collapse;
            width: 100%;
            margin-bottom: 30px;
          }

          .table th,
          .table td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
          }

          .table th {
            background-color: #FF385C;
            color: white;
          }

          .table tr:nth-child(even) {
            background-color: #f2f2f2;
          }

          .table tr:hover {
            background-color: #ddd;
          }

          p {
            text-align: center;
          }

          .btn-primary {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
            text-decoration: none;
            display: inline-block;
            margin-bottom: 20px;
          }

          .btn-primary:hover {
            background-color: #0056b3;
          }
        `}
      </style>
      <h2>User Dashboard</h2>
      <a href="/edit-profile" className="btn-primary">Edit Profile</a>
      {bookings && bookings.length > 0 ? (
        <table className="table">
          <thead>
            <tr>
              <th>Car</th>
              <th>Start Date</th>
              <th>End Date</th>
              <th>Time Remaining</th>
              <th>Fine</th>
            </tr>
          </thead>
          <tbody>
            {bookings.map((booking, index) => (
              <tr key={index}>
                <td>{booking.car.name}</td>
                <td>{booking.start_date}</td>
                <td>{booking.end_date}</td>
                <td>{booking.time_remaining()}</td>
                <td>{booking.fine}</td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No bookings found.</p>
      )}
    </div>
  );
};

export default UserDashboard;