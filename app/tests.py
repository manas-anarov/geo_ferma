from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import get_user_model

from django.urls import reverse, resolve
from .models import Plot, Culture, Season

from app.views import PlotCreateView, PlotListAPIView

User = get_user_model()


class PlotCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.culture = Culture.objects.create(name='Corn')
        self.season = Season.objects.create(season_number=1, year=2023)

    def test_create_plot(self):
        self.client.login(username='testuser', password='testpass')
        data = {'culture_id': self.culture.id, 'season_id': self.season.id, 'latitude': 39.762229,
                'longitude': -104.875610}
        response = self.client.post(reverse('app:plot-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Plot.objects.count(), 1)
        self.assertEqual(Plot.objects.get().farmer, self.user)
        self.assertEqual(Plot.objects.get().culture, self.culture)
        self.assertEqual(Plot.objects.get().season, self.season)
        self.assertEqual(Plot.objects.get().contour.x, -104.87561)
        self.assertEqual(Plot.objects.get().contour.y, 39.762229)

    def test_create_plot_with_invalid_culture_id(self):
        self.client.login(username='testuser', password='testpass')
        data = {'culture_id': 999, 'season_id': self.season.id, 'latitude': 39.762229, 'longitude': -104.875610}
        response = self.client.post(reverse('app:plot-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Plot.objects.count(), 0)

    def test_create_plot_with_invalid_season_id(self):
        self.client.login(username='testuser', password='testpass')
        data = {'culture_id': self.culture.id, 'season_id': 999, 'latitude': 39.762229, 'longitude': -104.875610}
        response = self.client.post(reverse('app:plot-create'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Plot.objects.count(), 0)


class TestUrls(TestCase):
    def test_plot_create_url_resolves(self):
        url = reverse('app:plot-create')
        self.assertEqual(resolve(url).func.view_class, PlotCreateView)

    def test_profile_list_url_resolves(self):
        url = reverse('app:plot-list')
        self.assertEqual(resolve(url).func.view_class, PlotListAPIView)
