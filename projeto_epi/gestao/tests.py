from django.urls import reverse

def test_home_url():
    assert reverse('home') == '/'



from django.test import Client
from django.urls import reverse
import pytest

@pytest.mark.django_db
def test_home_template():
    client = Client()
    reponse = client.get(reverse('home'))
    assert reponse.status_code == 200
    assert "/static/img/bg-logo.png" in reponse.content.decode('utf-8')
