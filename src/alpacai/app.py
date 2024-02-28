import argparse


def run(args):
    # TODO: Do things
    ...


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="AttentiveAI",
        description="Intelligent driver drowsiness avoidance with GenAI")
    parser.add_argument("model_path", help="Path to the driver drowsiness path")
    parser.add_argument("vehicle_ip", default="127.0.0.1", help="IP address to the vehicle interface communication")
    parser.add_argument("vehicle_port", default="55555", help="Port communication to the vehicle")
    args = parser.parse_args()

    run(args)
