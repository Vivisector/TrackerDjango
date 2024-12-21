from django.test import TestCase

# Create your tests here.
from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from .models import Task
from .forms import TaskForm
from .views import task_list


# Тесты для моделей
class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title="Test Task",
            description="This is a test description.",
            status="in progress"
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.status, "in progress")
        self.assertIsInstance(self.task, Task)


# Тесты для представлений
class TaskViewTest(TestCase):
    def test_index_view_status_code(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_template(self):
        response = self.client.get(reverse('task_list'))
        self.assertTemplateUsed(response, 'tasks/task_list.html')
        self.assertTemplateUsed(response, 'base.html')


# Тесты для форм
class TaskFormTest(TestCase):
    def test_valid_form(self):
        data = {
            'title': 'Test Task',
            'description': 'Test Description',
            'status': 'done',
            'created_at': '2024_12_21',
            'updated_at': '2024_12_20',
            'progress': '80',
        }
        form = TaskForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {
            'title': '',  # Пустое название задачи
            'description': 'Test Description',
        }
        form = TaskForm(data=data)
        self.assertFalse(form.is_valid())


# Тесты для URL
class UrlsTest(SimpleTestCase):
    def test_index_url_is_resolved(self):
        url = reverse('task_list')
        self.assertEqual(resolve(url).func, task_list)
