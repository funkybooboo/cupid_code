from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DaterSerializer, CupidSerializer, MessageSerializer, QuestSerializer, GigSerializer, DateSerializer, FeedbackSerializer, PaymentCardSerializer, BankAccountSerializer

# TODO write doc strings for all the views so we know what they should take in, what they should do, and what they should return


@api_view(['POST'])
def create_user(request):
    """
    Request the server to create an appropriate dater, cupid, or manager from info given.

    Args (request.post)
       user_type(str): Dater, Cupid, Manager
       password(str): unhashed password
       username(str) 
       email(str)
       first_name(str)
       last_name(str)
       phone_number(str)

       budget(float): the user's default budget
       communication_preference(int): EMAIL = 0, TEXT = 1
       description(str)
       dating_strengths(str)
       dating_weaknesses(str)
       interests(str)
       past(str)
       nerd_type(str)
       relationship_goals(str)
       ai_degree(str)
       cupid_cash_balance(str)
    Returns:
        Dater, Cupid, or Manager serialized
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user(request):
    """
    Get a user's information

    Args (request.post)
        user_id(int): The id of the user
    
    Returns:
        Dater, Cupid, or Manager serialized
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def send_chat_message(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_five_messages(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def calendar(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def rate_dater(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_ratings(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_avg_rating(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def dater_transfer(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_balance(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_profile(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def set_dater_profile(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def rate_cupid(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_ratings(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)

# ME FINISH

@api_view(['GET'])
def get_cupid_avg_rating(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def cupid_transfer(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_balance(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_profile(request, pk):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def set_cupid_profile(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def create_gig(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def accept_gig(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def complete_gig(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def drop_gig(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gigs(request, count):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_stores(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_activities(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_events(request):
    """

    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_attractions(request):
    """

    """
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_user_location(request, pk):
    """
    For gigs, the location of the user is needed to determine the delivery location of the gig.

    Args:
        request: Information about the request.
        pk (int): The id of the user to get the location of.
    Returns:
        Response:
            If the location of the user was retrieved successfully, return a 200 status code.
            If the location of the user was not retrieved successfully, return a 400 status code.

    """
    return Response(status=status.HTTP_200_OK)

@api_view(['GET'])
def get_cupids(request):
    """
    A manager can get all the cupid profiles.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the cupid profiles were retrieved successfully, return a 200 status code.
            If the cupid profiles were not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_daters(request):
    """
    A manager can get all the dater profiles.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the dater profiles were retrieved successfully, return a 200 status code.
            If the dater profiles were not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dater_count(request):
    """
    A manager can get the number of daters that are currently active.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of daters that are currently active was retrieved successfully, return a 200 status code.
            If the number of daters that are currently active was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_cupid_count(request):
    """
    A manager can get the number of cupids that are currently active.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of cupids that are currently active was retrieved successfully, return a 200 status code.
            If the number of cupids that are currently active was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_cupids(request):
    """
    A manager can get the number of active cupids.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of active cupids was retrieved successfully, return a 200 status code.
            If the number of active cupids was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_active_daters(request):
    """
    A manager can get the number of active daters.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of active daters was retrieved successfully, return a 200 status code.
            If the number of active daters was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_rate(request):
    """
    A manager can get the rate of gigs per hour.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs per hour was retrieved successfully, return a 200 status code.
            If the rate of gigs per hour was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_count(request):
    """
    A manager can get the number of gigs that are currently active.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the number of gigs that are currently active was retrieved successfully, return a 200 status code.
            If the number of gigs that are currently active was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_drop_rate(request):
    """
    A manager can get the rate of gigs that are dropped.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs that are dropped was retrieved successfully, return a 200 status code.
            If the rate of gigs that are dropped was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_gig_complete_rate(request):
    """
    A manager can get the rate of gigs that are completed.

    Args:
        request: Information about the request.
    Returns:
        Response:
            If the rate of gigs that are completed was retrieved successfully, return a 200 status code.
            If the rate of gigs that are completed was not retrieved successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def suspend(request):
    """
    Manager can suspend a user.

    Args (request.post):
        user_id (int): The id of the user to suspend.
    Returns:
        Response:
            If the user was suspended successfully, return a 200 status code.
            If the user was not suspended successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def unsuspend(request):
    """
    Manager can unsuspend a user.

    Args (request.post):
        user_id (int): The id of the user to unsuspend.
    Returns:
        Response:
            If the user was unsuspended successfully, return a 200 status code.
            If the user was not unsuspended successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def speech_to_text(request):
    """
    For a Dater.
    Convert an audio file to text. When the audio is converted to text, the text is sent to the external AI service.
    The response from the AI service is analyzed and a gig could be created based on the response.

    Args (request.post):
        audio (json): The audio to convert to text.
            audio['type'] (str): The type of audio file.
            audio['data'] (str): The audio file in base64 format.
    Returns:
        Response:
            If the audio was converted to text successfully and indicate if a gig was created or not, return a 200 status code.
            If the audio was not converted to text successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def notify(request):
    """
    Notify a user (any type) of something via a text or email.

    Args (request.post):
        user_id (int): The id of the user to notify.
        message (str): The message to send to the user.
    Returns:
        Response:
            If the message was sent successfully, return a 200 status code.
            If the message was not sent successfully, return a 400 status code.
    """
    return Response(status=status.HTTP_200_OK)
