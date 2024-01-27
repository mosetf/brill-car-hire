import unittest
from datetime import datetime, timedelta
from booking import create_booking

class BookingTestCase(unittest.TestCase):
    def test_create_booking_success(self):
        # Test creating a booking with available car and valid dates
        start_date = datetime.now()
        end_date = start_date + timedelta(days=3)
        booking = create_booking(1, 1, start_date, end_date)
        self.assertIsNotNone(booking)
        self.assertEqual(booking.user_id, 1)
        self.assertEqual(booking.car_id, 1)
        self.assertEqual(booking.start_date, start_date)
        self.assertEqual(booking.end_date, end_date)
        self.assertGreater(booking.total_price, 0)

    def test_create_booking_unavailable_car(self):
        # Test creating a booking with unavailable car
        start_date = datetime.now()
        end_date = start_date + timedelta(days=3)
        booking = create_booking(1, 2, start_date, end_date)
        self.assertFalse(booking)
        # Assert that the flash message is set correctly
        self.assertEqual(flash_message, 'This car is not available for the selected dates.\nFailed to create a booking. Please try again.')

    def test_create_booking_invalid_dates(self):
        # Test creating a booking with invalid dates (end date before start date)
        start_date = datetime.now()
        end_date = start_date - timedelta(days=3)
        booking = create_booking(1, 1, start_date, end_date)
        self.assertFalse(booking)
        # Assert that the flash message is set correctly
        self.assertEqual(flash_message, 'Invalid booking dates. Please select valid dates.')

if __name__ == '__main__':
    unittest.main()