import grpc
import time
from concurrent import futures

from protos1 import order_management_python_pb2
from protos1 import order_management_python_pb2_grpc


class OrderManagementServicer(order_management_python_pb2_grpc.OrderManagementServicer):

    def GetUnaryOrder(self, request, context):
        server_orders = [
            "banana",
            "apple",
            "orange",
            "grape",
            "red apple",
            "kiwi",
            "mango",
            "pear",
            "cherry",
            "green apple",
        ]
        print("GetUnaryOrder Request Made:")
        print(request)
        for order in server_orders:
            if request.item == order :
                order_response = order_management_python_pb2.OrderResponse(
                    item=order, timestamp=time.ctime()
                )
                # order_response.message = f"{request.item} {request.timestamp}"
                return order_response
        


    def GetOrder(self, request_iterator, context):
        server_orders = [
            "banana",
            "apple",
            "orange",
            "grape",
            "red apple",
            "kiwi",
            "mango",
            "pear",
            "cherry",
            "green apple",
        ]
        for order in request_iterator:
            for server_order in server_orders:
                if order.item.lower() in server_order.lower():
                    yield order_management_python_pb2.OrderResponse(
                        item=server_order, timestamp=time.ctime()
                    )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_management_python_pb2_grpc.add_OrderManagementServicer_to_server(
        OrderManagementServicer(), server
    )
    server.add_insecure_port("localhost:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
