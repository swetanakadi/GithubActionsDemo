from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import os

print(f"Current file: {__file__}")
print(f"Current working directory: {os.getcwd()}")


class TesDemoView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('test-view')
        print(self.url)

    def test_get_request(self):
        response = self.client.get(self.url)
        print(response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), 'Hello from the server!!')
