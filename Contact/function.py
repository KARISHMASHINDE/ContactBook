from rest_framework.response import Response


def createResponse(status, message, data, typeOfData):
    msg = {"status": status, "message": message}
    return Response({"message": msg, typeOfData: data})
