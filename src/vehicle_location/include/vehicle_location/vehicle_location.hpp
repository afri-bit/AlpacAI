#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

class VehicleLocation : public rclcpp::Node
{
public:
    VehicleLocation();

private:
    rclcpp::TimerBase::SharedPtr timer_;

    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;

    size_t count_;

    void timer_callback();
};
