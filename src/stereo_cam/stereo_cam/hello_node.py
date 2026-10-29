import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node


class HelloNode(Node):
    def __init__(self):
        super().__init__("hello_node")
        logger = self.get_logger()
        logger.info("I'm Here!")
        logger.warning("This is a warning!!!")


def main():
    try:
        # with allows rclpy to handle the clean up "node.destroy_node()" and "rclpy.shutdown()" on its own
        with rclpy.init():
            node: Node = HelloNode()
            # when you press ctrl+c you raise a keyboard exception which iniates shutdown in rclpy and moves on to the next block
            rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass


if __name__ == "__main__":
    main()
