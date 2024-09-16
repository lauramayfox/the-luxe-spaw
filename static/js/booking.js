// update booking modal with selected choices
    function updateBookingModal() {
        document.getElementById('booking-service').textContent = document.getElementById('id_service').selectedOptions[0].text;
        document.getElementById('booking-groomer').textContent = document.getElementById('id_groomer').selectedOptions[0].text;
        document.getElementById('booking-date').textContent = document.getElementById('id_booking_date').value;
        document.getElementById('booking-time').textContent = document.getElementById('id_booking_time').selectedOptions[0].text;
    }

    // booking confirmation
    const confirmBookingButton = document.getElementById('confirm-booking');
    if (confirmBookingButton) {
        confirmBookingButton.addEventListener('click', function () {
            console.log('Confirm booking button clicked');
       
            document.getElementById('booking-form').submit();
        });
    }

    // cancel booking action
    const cancelBookingButton = document.getElementById('cancel-booking');
    if (cancelBookingButton) {
        cancelBookingButton.addEventListener('click', function () {
            window.location.href = 'booking/create_booking.html';
        });
    }

 
    const bookButton = document.querySelector('[data-bs-target="#confirmBookingModal"]');
    if (bookButton) {
        bookButton.addEventListener('click', function () {
            updateBookingModal();
        });
    }







