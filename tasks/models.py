from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    progress = models.IntegerField(default=0)  # Новое поле

    def save(self, *args, **kwargs):
        """
               Переопределяет метод сохранения модели.

               Описание:
                   - Если значение прогресса больше 0 и статус не равен "done", устанавливается статус "in_progress".
                   - Если прогресс равен 0, статус обновляется на "todo".
                   - После проверки вызывает метод `save` родительского класса для сохранения изменений в базе данных.

               Аргументы:
                   *args: Позиционные аргументы, переданные в метод `save`.
                   **kwargs: Именованные аргументы, переданные в метод `save`.

               Возвращает:
                   None
               """
        # Если прогресс больше 0, устанавливаем статус "In Progress"
        if self.progress > 0 and self.status != 'done':
            self.status = 'in_progress'
        # Если прогресс равен 0, возвращаем статус "To Do"
        elif self.progress == 0:
            self.status = 'todo'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def is_completed(self):
        """
               Проверяет, завершена ли задача.

               Описание:
                   - Метод возвращает True, если статус задачи равен "Done".

               Возвращает:
                   bool: True, если задача завершена, иначе False.
               """
        return self.status == 'Done'

# Create your models here.
