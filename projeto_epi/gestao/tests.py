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
    # Remova o "/static/img/" e deixe apenas as classes do ícone
    assert "fa-solid fa-helmet-safety" in reponse.content.decode('utf-8')

@pytest.mark.django_db
def test_menu_links_present(client):
    response = client.get(reverse('home'))
    # Verifica se os textos dos links do seu menu existem no HTML
    assert "Colaboradores" in response.content.decode('utf-8')
    assert "EPIs" in response.content.decode('utf-8')
    assert "Empréstimos" in response.content.decode('utf-8')

@pytest.mark.django_db
def test_sidebar_menu_items(client):
    response = client.get(reverse('home'))
    html = response.content.decode('utf-8')
    
    # Verifica se os textos dos itens do menu aparecem
    assert "Colaboradores" in html
    assert "EPIs" in html
    assert "Empréstimos" in html
    assert "Usuários" in html


from datetime import date # Importe isso no topo do arquivo
from gestao.models import Equipamento
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_equipamento_na_lista(client):
    # Agora passamos a data_validade que o banco exige
    Equipamento.objects.create(
        nome="Capacete de Segurança", 
        data_validade=date(2025, 12, 31) # Ajuste se o nome do campo for diferente
    )
    
    response = client.get(reverse('equipamento_list'))
    assert response.status_code == 200
    assert "Capacete de Segurança" in response.content.decode('utf-8')


