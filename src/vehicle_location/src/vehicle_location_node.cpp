#include "rclcpp/rclcpp.hpp"

#include "vehicle_location/vehicle_location.hpp"

int main(int argc, char *argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<VehicleLocation>());
  rclcpp::shutdown();
  return 0;
}