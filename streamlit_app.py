import streamlit as st
import time

# Set the refresh rate in seconds
refresh_rate = 10

# Main app code
def main():
    st.title("Auto Refresh Example")
    st.write("This page will automatically refresh every 10 seconds.")

    # Infinite loop to refresh the page
    while True:
        # Add a delay to control the refresh rate
        time.sleep(refresh_rate)
        # Rerun the app
        st.experimental_rerun()

if __name__ == "__main__":
    main()
