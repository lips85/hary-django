from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from .models import User
from tweets.models import Tweet
from tweets.serializers import TweetSerializer


class tweets_by_user(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweets = Tweet.objects.filter(user=self.get_object(pk))
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)
