from kuksa_client.grpc import VSSClient

# Define a counter for the number of updates received
updates_received = 0

with VSSClient('127.0.0.1', 55555) as client:
    # Subscribe to both latitude and longitude
    for updates in client.subscribe_current_values([
        'Vehicle.CurrentLocation.Latitude',
        'Vehicle.CurrentLocation.Longitude',
    ]):
        # Process latitude updates
        if 'Vehicle.CurrentLocation.Latitude' in updates:
            latitude = updates['Vehicle.CurrentLocation.Latitude'].value
            print(f"Received updated latitude: {latitude}")
            updates_received += 1

        # Process longitude updates
        if 'Vehicle.CurrentLocation.Longitude' in updates:
            longitude = updates['Vehicle.CurrentLocation.Longitude'].value
            print(f"Received updated longitude: {longitude}")
            updates_received += 1

        # Check if we have received two updates for each
        if updates_received >= 4:  # 2 latitude updates and 2 longitude updates
            print("Received two updates for both latitude and longitude.")
            break  # Exit the loop after receiving the required updates

print("Finished subscribing.")
