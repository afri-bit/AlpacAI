from kuksa_client.grpc import VSSClient
from kuksa_client.grpc import Datapoint
import time

# Define your coordinates
coordinates = [
    (51.1657, 10.4515),  # First set of coordinates (latitude, longitude)
    (50.1234, 10.1234)   # Second set of coordinates (latitude, longitude)
]

with VSSClient('127.0.0.1', 55555) as client:
    for lat, lon in coordinates:
        # Set latitude
        client.set_current_values({
            'Vehicle.CurrentLocation.Latitude': Datapoint(lat),
        })
        print(f"Feeding Vehicle.CurrentLocation.Latitude to {lat}")

        # Set longitude
        client.set_current_values({
            'Vehicle.CurrentLocation.Longitude': Datapoint(lon),
        })
        print(f"Feeding Vehicle.CurrentLocation.Longitude to {lon}")

        # Wait for a while before sending the next set of coordinates
        time.sleep(1)

print("Finished.")
