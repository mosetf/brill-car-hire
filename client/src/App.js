import React from 'react';
import './styles/App.css';
import './styles/global.css';
import PaymentSelection from './components/PaymentSelection';
import SignUp from './components/SignUp';

function App() {
  const booking = { id: 1, total_price: 100 }; // Example booking data

  return (
    <div className="App">
      <PaymentSelection booking={booking} />
      <SignUp />
    </div>
  );
}

export default App;