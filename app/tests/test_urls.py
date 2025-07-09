# app/tests/test_urls.py

from django.test import TestCase
from django.urls import get_resolver, reverse, NoReverseMatch

class URLSmokeTest(TestCase):
    def test_all_urls_status_code(self):
        urlconf = get_resolver()
        for name in urlconf.reverse_dict.keys():
            if isinstance(name, str):  # ignora rotas anônimas
                try:
                    url = reverse(name)
                    response = self.client.get(url)
                    self.assertIn(response.status_code, [200, 302, 403, 401])
                except NoReverseMatch:
                    pass  # ignora se a rota precisa de argumento
