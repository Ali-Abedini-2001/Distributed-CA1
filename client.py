import grpc
import time

from protos1 import order_management_python_pb2
from protos1 import order_management_python_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = order_management_python_pb2_grpc.OrderManagementStub(channel)
        print("1. Unary")
        print("2. Server Side Streaming")
        print("3. Client Side Streaming")
        print("4. Both Streaming")
        rpc_call = input("Which rpc would you like to make: ")

        if rpc_call == "1":
            order_request = order_management_python_pb2.OrderRequest(item = "apple")
            order_response = stub.GetUnaryOrder(order_request)
            print("Unary Mode:")
            print(order_response)
        elif rpc_call == "2":
            hello_request = greet_pb2.HelloRequest(greeting = "Bonjour", name = "YouTube")
            hello_replies = stub.ParrotSaysHello(hello_request)

            for hello_reply in hello_replies:
                print("ParrotSaysHello Response Received:")
                print(hello_reply)
        elif rpc_call == "3":
            delayed_reply = stub.ChattyClientSaysHello(get_client_stream_requests())

            print("ChattyClientSaysHello Response Received:")
            print(delayed_reply)
        elif rpc_call == "4":
            responses = stub.InteractingHello(get_client_stream_requests())

            for response in responses:
                print("InteractingHello Response Received: ")
                print(response)

    """
    with grpc.insecure_channel('localhost:50051') as channel:
            stub = order_management_python_pb2_grpc.OrderManagementStub(channel)
            response_iterator = stub.GetOrder(order_management_python_pb2.OrderRequest(item='apple'))
            for response in response_iterator:
                print(f'Item: {response.item}, Timestamp: {response.timestamp}')
    """


    

if __name__ == '__main__':
    run()
