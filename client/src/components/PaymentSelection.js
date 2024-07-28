import React from 'react';
import '../styles/App.css';

const PaymentSelection = ({ booking }) => {
  return (
    <div>
      <h2>Select Payment Method</h2>
      <p>Total Amount: ${booking.total_price}</p>
      <form method="POST" action={`/select_payment/${booking.id}`}>
        <div>
          <input type="radio" id="credit_card" name="payment_method" value="credit_card" required />
          <label for="credit_card">Credit Card</label>
        </div>
        <div>
          <input type="radio" id="paypal" name="payment_method" value="paypal" required />
          <label for="paypal">PayPal</label>
        </div>
        <input type="hidden" name="booking_id" value={booking.id} />
        <button type="submit">Proceed to Payment</button>
      </form>
    </div>
  );
};

export default PaymentSelection;