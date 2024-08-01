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
import HomePage from './components/HomePage';
import Home from './components/Home';
import LoginPage from './components/LoginPage';

function App() {
  const booking = { id: 1, total_price: 100 }; // Example booking data

  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/payment-selection" element={<PaymentSelection booking={booking} />} />
          <Route path="/sign-up" element={<SignUp />} />
          <Route path="/base-layout" element={<BaseLayout />} />
          <Route path="/admin-sign-up" element={<AdminSignUp />} />
          <Route path="/book-car" element={<BookCar />} />
          <Route path="/car-form" element={<CarForm />} />
          <Route path="/confirm-booking" element={<ConfirmBooking />} />
          <Route path="/user-dashboard" element={<UserDashboard />} />
          <Route path="/edit-profile" element={<EditProfile />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;