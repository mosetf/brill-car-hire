import React, { useState } from 'react';

const Home = ({ cars }) => {
  const [readMore, setReadMore] = useState({});

  const toggleReadMore = (carId) => {
    setReadMore((prevState) => ({
      ...prevState,
      [carId]: !prevState[carId],
    }));
  };

  return (
    <div className="car-grid">
      <style>
        {`
          .car-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            grid-gap: 20px;
            padding: 40px;
            margin: 0 auto;
          }

          .car-item {
            position: relative;
            overflow: hidden;
            border: 1px solid #ddd;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
          }

          .car-item:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
          }

          .car-item img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-bottom: 1px solid #ddd;
          }

          .car-name-overlay {
            position: absolute;
            top: 10px; 
            left: 10px; 
            background-color: rgba(255, 255, 255, 0.75); 
            padding: 5px 10px;
            border-radius: 4px;
            font-size: 16px;
            color: #333;
            max-width: 90%;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
          }

          .car-info {
            padding: 20px;
            text-align: center;
          }

          .car-item h3,
          .car-item p {
            margin: 0;
            padding: 4px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
          }

          .book-button {
            background-color: #FF385C; 
            color: white;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 8px 0;
            cursor: pointer;
            border: none;
            border-radius: 4px;
            transition: background-color 0.3s ease-in-out;
          }

          .book-button:hover {
            background-color: #FF5A5F; /* A slightly lighter shade for hover effect */
          }
        `}
      </style>
      {cars.map((car) => (
        <div className="car-item" key={car.id}>
          <div className="car-name-overlay">{car.name}</div>
          <img src={`/static/images/${car.image_url.split('\\').pop()}`} alt={car.name} />
          <div className="car-info">
            <h3>{car.title}</h3>
            <p className="short-text">{car.description.slice(0, 100)}</p>
            {readMore[car.id] && <p className="more-text">{car.description}</p>}
            <button className="book-button" onClick={() => toggleReadMore(car.id)}>
              {readMore[car.id] ? 'Read Less' : 'Read More'}
            </button>
            <a href={`/views/book_car/${car.id}`} className="book-button">Book Now</a>
          </div>
        </div>
      ))}
    </div>
  );
};

export default Home;