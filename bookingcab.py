import streamlit as st

def main():
    st.title("Cab Booking System")

    # Input fields for booking details
    st.header("Book a Cab")

    # Departure and Destination
    departure = st.text_input("Departure Location", "Enter your location")
    destination = st.text_input("Destination Location", "Enter your destination")

    # Date and Time
    date = st.date_input("Date of Travel")
    time = st.time_input("Time of Travel")

    # Number of Passengers
    passengers = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

    # Confirm booking
    if st.button("Book Cab"):
        st.write(f"Booking Details:")
        st.write(f"Departure Location: {departure}")
        st.write(f"Destination Location: {destination}")
        st.write(f"Date of Travel: {date}")
        st.write(f"Time of Travel: {time}")
        st.write(f"Number of Passengers: {passengers}")
        st.success("Your cab has been booked successfully!")

if __name__ == "__main__":
    main()
