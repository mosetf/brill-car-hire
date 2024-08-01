import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './styles/App.css';
import './styles/global.css';
import PaymentSelection from './components/PaymentSelection';
import SignUp from './components/SignUp';
import BaseLayout from './components/BaseLayout';
import AdminSignUp from './components/AdminSignUp';
import BookCar from './components/BookCar';
import CarForm from './components/CarForm';
import ConfirmBooking from './components/ConfirmBooking';
import UserDashboard from './components/UserDashboard';
import EditProfile from './components/EditProfile';
import Home from './components/Home';

function App() {
  const booking = { id: 1, total_price: 100 }; // Example booking data

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" exact component={Home} />
          <Route path="/payment-selection" render={() => <PaymentSelection booking={booking} />} />
          <Route path="/sign-up" component={SignUp} />
          <Route path="/base-layout" component={BaseLayout} />
          <Route path="/admin-sign-up" component={AdminSignUp} />
          <Route path="/book-car" component={BookCar} />
          <Route path="/car-form" component={CarForm} />
          <Route path="/confirm-booking" component={ConfirmBooking} />
          <Route path="/user-dashboard" component={UserDashboard} />
          <Route path="/edit-profile" component={EditProfile} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;