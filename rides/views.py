from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# list of available rides
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def available_rides(request):
    return Response()


# assign a ride
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def pick_ride(request):
    return Response()


# create a new ride
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_ride(request):
    return Response()


# update_ride_detail
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update_ride_detail(request):
    return Response()


# cancel a ride
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def cancel_ride(request):
    return Response()


# add passenger to a ride
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_passenger(request):
    return Response()


# remove a passenger from a ride
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def remove_passenger(request):
    return Response()


# get a list of passengers for a ride
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_passengers(request):
    return Response()


# detail of a ride
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_detail(request):
    return Response()


# real-time location of a ride
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_ride_location(request):
    return Response()
