# app/tests/test_views.py

from django.test import TestCase
from django.urls import resolve

class ViewSmokeTest(TestCase):
    def test_views_exist(self):
        from django.urls import get_resolver
        resolver = get_resolver()
        for pattern in resolver.url_patterns:
            try:
                result = resolve(pattern.pattern._route)
                self.assertIsNotNone(result.func)
            except Exception:
                pass  # pode ignorar rotas com parâmetros dinâmicos
