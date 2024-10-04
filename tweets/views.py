from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TweetSerializer
from .models import Tweet


class All_Tweets(APIView):
    def get_object(self, pk):
        pass

    def get(self, request):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
