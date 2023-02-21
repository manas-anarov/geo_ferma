from django.contrib.gis.geos import Point
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import Plot, Culture, Season
from .serializers import ListSerializer, PlotSerializer
from .pagination import PostPageNumberPagination


class PlotListAPIView(ListAPIView):
    serializer_class = ListSerializer
    pagination_class = PostPageNumberPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['culture', 'season']
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        current_user = self.request.user
        queryset_list = Plot.objects.all().filter(farmer=current_user).order_by('-id')

        return queryset_list


class PlotCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication, SessionAuthentication)

    def post(self, request):
        farmer = request.user
        culture_id = request.data.get('culture_id')
        season_id = request.data.get('season_id')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')
        contour = Point(longitude, latitude)

        try:
            culture = Culture.objects.get(id=culture_id)
        except Culture.DoesNotExist:
            return Response({'error': 'Culture with specified ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            season = Season.objects.get(id=season_id)
        except Season.DoesNotExist:
            return Response({'error': 'Season with specified ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        plot = Plot.objects.create(farmer=farmer, culture=culture, season=season, contour=contour)
        serializer = PlotSerializer(plot)
        return Response(serializer.data)
