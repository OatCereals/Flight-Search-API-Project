from datetime import datetime
from airportsdata import load
from amadeus import Client, ResponseError
import re

amadeus = Client(client_id='5BwgzFezNbfF0jtT7Y7nt93zA5sJs3jQ', client_secret='kDqnTGBswVHc4EG4')
airports = load('IATA')

def main():
    print("\nFor viewing information and cost to fly between 2 destinations, type 'specific'")
    print("To check informations about flights anywhere from a city, type 'any'")
    while True:
        match input('Please select your option: ').strip().lower():
            case "specific":
                origin = input("Please enter origin airport IATA (airport code): ").strip().upper()
                destination = input("Please enter destination airport IATA (airport code): ").strip().upper()
                departure_date = input("Enter date in yyyy-mm-dd format: ")
                specific(origin, destination, departure_date)
                break
            case "any":
                anyl(input("Please enter origin airport IATA (airport code): ").strip().upper())
                break
            case _:
                print("Invalid option")

def anyl(home):
    try:
        response = amadeus.shopping.flight_destinations.get(origin = home)
        for flightoffer in response.data:
            print("Offer Details:")
            pricez = flightoffer.get("price", {})
            price = pricez.get("total", "N/A")
            origin = flightoffer.get("origin", {})
            destination = flightoffer.get("destination", {})
            origin_details = get_airport_details(origin)
            destination_details = get_airport_details(destination)
            departure = flightoffer.get("departureDate", {})
            ret = flightoffer.get("returnDate", {})
            print(f"\n   Departure airport: {origin} - {origin_details} on {departure}")
            print(f"   Arrival: {destination} - {destination_details} on {ret}")
            print(f"    Ticket Price: {price}")
            print("-" * 40)
        return True

    except ResponseError as error:
        print(f"API error: {error}")
        return False

def specific(origin, destination, departure_date):
    try:
        response = amadeus.shopping.flight_offers_search.get(originLocationCode=origin,
        destinationLocationCode=destination, departureDate=f"{departure_date}", adults=1)
        print(response.data)
        for flightoffer in response.data:
            print("\nOffer Details:")
            traveler_pricings = flightoffer.get("travelerPricings", [])
            for traveler in traveler_pricings:
                traveler_price = traveler.get("price", {})
                currency = traveler_price.get("currency", "N/A")
                total_price = traveler_price.get("total", "N/A")
                base_price = traveler_price.get("base", "N/A")
                print(f"  Ticket Price: {total_price} {currency} (Base: {base_price})")

            itineraries = flightoffer.get("itineraries", [])
            for itinerary in itineraries:
                for item in itinerary.get("segments", []):
                    departure = item.get("departure", {})
                    arrival = item.get("arrival", {})
                    carrier = item.get("carrierCode", "Unknown")
                    flight_number = item.get("number", "Unknown")
                    duration = item.get("duration", "Unknown")
                    time= time_conversion(duration)
                    departure_time = departure.get("at", "Unknown")
                    arrival_time = arrival.get("at", "Unknown")

                    try:
                        departure_time = datetime.strptime(departure_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y at %H:%M")
                        arrival_time = datetime.strptime(arrival_time, "%Y-%m-%dT%H:%M:%S").strftime("%d-%m-%Y at %H:%M")
                    except ValueError:
                        departure_time = "Invalid date-time format"
                        arrival_time = "Invalid date-time format"
                    origin_details = get_airport_details(departure.get("iataCode", "Unknown"))
                    destination_details = get_airport_details(arrival.get("iataCode", "Unknown"))
                    print(f"      Flight {carrier} {flight_number}")
                    print(f"      Departure: {departure.get('iataCode', 'Unknown')} at {departure_time}\n        Airport: {origin_details}")
                    print(f"      Arrival: {arrival.get('iataCode', 'Unknown')} at {arrival_time}\n        Airport: {destination_details}")
                    print(f"      Duration: {time}\n")
            print("-" * 40)
            print()
        return True

    except ResponseError as error:
        print(f"API error: {error}")
        return False

    except Exception as e:
        print(f"Unexpected error: {e}")
        return False

def time_conversion(time):
    pattern = re.compile(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?")
    match = pattern.match(time)
    if match:
        hours, minutes, seconds = match.groups()
        readable_duration = []
        if hours:
            readable_duration.append(f"{hours} hour{'s' if int(hours) > 1 else ''}")
        if minutes:
            readable_duration.append(f"{minutes} minute{'s' if int(minutes) > 1 else ''}")
        if seconds:
            readable_duration.append(f"{seconds} second{'s' if int(seconds) > 1 else ''}")
        return ", ".join(readable_duration)
    else:
        return "Invalid duration format"

def get_airport_details(iata_code):
    airport = airports.get(iata_code)
    if airport:
        return f"{airport['name']}, {airport['city']}, {airport['country']}"
    return "Airport not found."


if __name__ == "__main__":
    main()
