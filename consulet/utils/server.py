import auth_pb2
import auth_pb2_grpc
import grpc


from concurrent import futures
from db import db


class validate(auth_pb2_grpc.TokenValidationServicer):

    def validate(self, request, context):
        email = db.get_email(request.token)
        if email is None:
            email = "No email Matching Found"
        return auth_pb2.result(email=email)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    auth_pb2_grpc.add_TokenValidationServicer_to_server(
        validate(), server
    )
    server.add_insecure_port("127.0.0.1:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
