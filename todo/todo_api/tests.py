from django.test import TestCase
from .models import Todo


class TodoTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.todo = Todo.objects.create(task="test", completed=False)

    # @classmethod
    # def setUptestData(cls):
    #     cls.todo = Todo.objects.create(task="test", completed=False)
    #     cls.todo2 = Todo.objects.create(task="test2", completed=False)
    #     cls.todo3 = Todo.objects.create(task="test3", completed=False)

    # @classmethod
    # def setUptestData(cls):
    testthing = Todo.objects.create(task="test", completed=True)
    testthing.save()

    def test_Todo_model(self):
        self.assertEqual(self.todo.task, "test")
        self.assertEqual(self.todo.completed, False)

    def test_Todo_model_2(self):
        thing = Todo.objects.get(id=1)
        actual_task = thing.task
        self.assertEqual(actual_task, "test")
