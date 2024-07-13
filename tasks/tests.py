from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskAPITests(APITestCase):

    def setUp(self):
        self.task_data = {'title': 'Test Task', 'description': 'This is a test task', 'completed': False}
        self.task = Task.objects.create(**self.task_data)
        self.task_url = reverse('task-detail', kwargs={'pk': self.task.id})
        self.tasks_url = reverse('task-list-create')

    def test_create_task(self):
        response = self.client.post(self.tasks_url, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(id=2).title, 'Test Task')

    def test_retrieve_task_by_id(self):
        response = self.client.get(self.task_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.task.title)

    def test_retrieve_all_tasks(self):
        response = self.client.get(self.tasks_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.task.title)

    def test_update_task(self):
        updated_data = {'title': 'Updated Task', 'description': 'This is an updated test task', 'completed': True}
        response = self.client.put(self.task_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')
        self.assertEqual(self.task.completed, True)

    def test_delete_task(self):
        response = self.client.delete(self.task_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
