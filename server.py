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
                return order_response
    
    def GetSSOrder(self, request, context):
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
        print("GetSSOrder Request Made:")
        print(request)

        for i in range(3):
            for order in server_orders:
                if request.item == order : 
                    order_response = order_management_python_pb2.OrderResponse(
                    item=order , timestamp=time.ctime()
                )
                    # order_response.item = f"{request.item} {i + 1}"
                    # order_response.timestamp = f"{request.time.ctime()}"
                    yield order_response
                    time.sleep(3)


    def GetCSOrder(self, request_iterator, context):
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
        delayed_reply = order_management_python_pb2.DelayedReply()
        for request in request_iterator:
            for order in server_orders:
                if request.item == order:
                    print("GetCSOrder Request Made:")
                    print(request)
                    delayed_reply.request.append(request)

        delayed_reply.item = f"You have sent {len(delayed_reply.request)} messages. Please expect a delayed response."
        return delayed_reply

    def GetBothOrder(self, request_iterator, context):
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
        for request in request_iterator:
            for server_order in server_orders:
                if request.item == server_order:
                    print("GetBothOrder Request Made:")
                    print(request)
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
