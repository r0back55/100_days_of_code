import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight, FlightData


# ==================== Set up the Flight Search ====================
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# Set your origin airport
ORIGIN_CITY_IATA = "WAW"


# ==================== Update the Airport Codes in Google Sheet ====================
for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        # slowing down requests to avoid rate limit
        time.sleep(2)
print(f"sheet_data:\n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_code()


# ==================== Search for Flights ====================

tomorrow = datetime.now() + timedelta(days=1)
three_month_from_today = datetime.now() + timedelta(days=(3 * 30))
five_month_from_today = datetime.now() + timedelta(days=(5 * 30))

for destination in sheet_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=three_month_from_today,
        to_time=five_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights)

    if isinstance(cheapest_flight, FlightData) and cheapest_flight.price != "N/A":
        print(f"{destination['city']}: zł{cheapest_flight.price}")

        # Compare with the price in the sheet
        if float(cheapest_flight.price) < float(destination['lowestPrice']):
            print(f"New lower price found for {destination['city']}!")
            # Update the price in the sheet
            data_manager.update_price(destination['id'], cheapest_flight.price)
            # Update the local data
            destination['lowestPrice'] = cheapest_flight.price
    else:
        print(f"No valid flight data found for {destination['city']}")

    # Slowing down requests to avoid rate limit
    time.sleep(2)
