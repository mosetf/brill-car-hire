import React from 'react';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <div>
      <style>
        {`
          .hero {
            position: relative;
            overflow: hidden;
          }

          .hero-video {
            width: 100%;
            height: auto;
          }

          .hero-content {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            text-align: center;
          }

          .btn-primary, .btn-secondary {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px;
            text-decoration: none;
            border-radius: 4px;
            transition: background-color 0.3s ease-in-out;
          }

          .btn-primary {
            background-color: #FF385C;
            color: white;
          }

          .btn-primary:hover {
            background-color: #FF5A5F;
          }

          .btn-secondary {
            background-color: #333;
            color: white;
          }

          .btn-secondary:hover {
            background-color: #555;
          }

          .about, .services {
            padding: 40px;
            text-align: center;
          }

          footer {
            text-align: center;
            padding: 20px;
            background-color: #f1f1f1;
          }
        `}
      </style>
      <header>
        <nav>
          <a href="#" className="logo">Brill Car Hire</a>
          <ul>
            <li><a href="#services">Services</a></li>
            <li><a href="#about">About Us</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </header>
      <main>
        <section className="hero">
          <video autoPlay muted loop className="hero-video">
            <source src="../static/videos/051_051-0411_preview.mp4" type="video/mp4" />
            Your browser does not support the video tag.
          </video>
          <div className="hero-content">
            <h1>Welcome to Brill Car Hire</h1>
            <p>
              Discover the freedom to explore with our premium car rental services. Whether you're planning a weekend getaway or a cross-country adventure, Brill Car Hire is your key to hassle-free and stylish travel.
            </p>
            <Link to="/login" className="btn-primary">Rent Now</Link>
            <a href="#about" className="btn-secondary">Know More</a>
          </div>
        </section>
        <section id="about" className="about">
          <h2>About Us</h2>
          <p>
            Welcome to Brill Car Hire! Discover the freedom to explore with our premium car rental services. Whether you're planning a weekend getaway or a cross-country adventure, Brill Car Hire is your key to hassle-free and stylish travel. Browse our diverse fleet of quality cars, book seamlessly, and experience the joy of the open road. Your journey begins with Brill Car Hire – Where Every Drive is an Adventure!
          </p>
        </section>
        <section id="services" className="services">
          <h2>Our Services</h2>
          <p>#1 Car Rent Service In Your City.</p>
        </section>
      </main>
      <footer>
        <p>&copy; 2023 Brill Car Hire. All rights reserved.</p>
      </footer>
    </div>
  );
};

export default HomePage;