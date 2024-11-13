from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from blog.models import Board

class BoardModelTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_data = {
            'title': 'Valid Title',
            'content': 'This is valid content.',
            'created_at': '2024-11-13T12:00:00',
            'updated_at': '2024-11-13T12:00:00',
        }
        self.invalid_data_missing_field = {
            'content': 'Missing title field.',  # title 필드가 누락된 데이터
            'created_at': '2024-11-13T12:00:00',
            'updated_at': '2024-11-13T12:00:00',
        }
        self.invalid_data_wrong_format = {
            'title': 'Invalid Title',
            'content': 'This is invalid content.',
            'created_at': 'invalid-date-format',  # 잘못된 날짜 형식
            'updated_at': '2024-11-13T12:00:00',
        }

    def test_create_board_with_valid_data(self):
        response = self.client.post('/blog/', self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(Board.objects.get().title, 'Valid Title')

    def test_create_board_with_missing_field(self):
        response = self.client.post('/blog/', self.invalid_data_missing_field, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Board.objects.count(), 0)

    def test_create_board_with_wrong_format(self):
        response = self.client.post('/blog/', self.invalid_data_wrong_format, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Board.objects.count(), 0)
