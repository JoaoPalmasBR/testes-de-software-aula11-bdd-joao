from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('que estou na página inicial')
def step_open_initial_page(context):
    # Inicializa o driver do navegador

    # Acessa a página inicial
    context.driver.get('https://joao.palmas.br/ts2024/')

@when('preencho o input com o texto "l" e submeto o formulário')
def step_fill_form_and_submit(context):
    # Clicar no input com id 'conteudo' dentro do formulário de id 'formulario'
    input_field = context.driver.find_element(By.ID, 'conteudo')
    
    # Preenche o campo com a letra 'l'
    input_field.send_keys('l')
    
    # Submete o formulário clicando no botão de id 'botaosubmit'
    submit_button = context.driver.find_element(By.ID, 'botaosubmit')
    submit_button.click()

@then('sou redirecionado para a página de resultados e verifico se há um item "li" com o texto "real"')
def step_verify_result(context):
    # Aguarda até que a página seja redirecionada e o termo 'resultado' esteja na URL
    WebDriverWait(context.driver, 10).until(EC.url_contains('resultado'))
    
    # Após o redirecionamento, procura por itens 'li' na página
    li_elements = context.driver.find_elements(By.TAG_NAME, 'li')
    
    # Verifica se algum dos itens 'li' contém o termo 'real'
    found = False
    for item in li_elements:
        if "real" in item.text.lower():  # Usa lower() para ignorar maiúsculas/minúsculas
            found = True
            print("O termo 'real' foi encontrado!")
            break

    # Verifica se o termo foi encontrado
    assert found, "O termo 'real' não foi encontrado nos itens da lista."

    # Fechar o navegador
    context.driver.quit()
