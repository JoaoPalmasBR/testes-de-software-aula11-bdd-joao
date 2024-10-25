Feature: Verificar a presença de "Real" na página de resultados

  Scenario: Acessar a página, preencher o campo e verificar o resultado
    Given que estou na página inicial
    When preencho o input com o texto "l" e submeto o formulário
    Then sou redirecionado para a página de resultados e verifico se há um item "li" com o texto "real"
