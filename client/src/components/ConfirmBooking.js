import React from 'react';

const ConfirmBooking = ({ car, carPrice, bookingId }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle form submission logic here
    console.log('Booking confirmed for booking ID:', bookingId);
  };

  return (
    <div className="container">
      <style>
        {`
          .container {
            padding: 20px;
            max-width: 600px;
            margin: 0 auto;
          }
          .btn-primary {
            background-color: #007bff;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
          }
          .btn-primary:hover {
            background-color: #0056b3;
          }
        `}
      </style>
      <h2>Confirm Booking</h2>
      <p>Car Name: {car.name}</p>
      <p>Category: {car.category}</p>
      <p>Price: ${carPrice}</p>

      <form onSubmit={handleSubmit}>
        <input type="hidden" name="booking_id" value={bookingId} />
        <button type="submit" className="btn-primary">Confirm Booking</button>
      </form>
    </div>
  );
};

export default ConfirmBooking;