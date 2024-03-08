#include "vehicle_location/vehicle_location.hpp"

using namespace std::chrono_literals;

VehicleLocation::VehicleLocation() : Node("minimal_publisher"), count_(0)
{
  this->publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
  
  this->timer_ = this->create_wall_timer(1000ms, std::bind(&VehicleLocation::timer_callback, this));
}

void VehicleLocation::timer_callback()
{
  auto message = std_msgs::msg::String();

  message.data = "Hello, world! " + std::to_string(count_++);

  RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", message.data.c_str());

  this->publisher_->publish(message);
}
