from selenium import webdriver # importa webdriver do selenium
from selenium.webdriver.chrome.options import Options # importa a Classe Options do selenium.webdriver.chrome.options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select # manipular tags <select> , <option>
import re
import pygetwindow as GW
import pyautogui
import time

# Nome Do Cadastrante (capitalize o dado quando for coloca-ló na função (def))
Nome_do_Cadastrante = input("insira seu Nome: \n Nome:")
while not Nome_do_Cadastrante:
    print("Nome não Pode Ser Vazio !!!")
    Nome_do_Cadastrante = input("insira seu Nome: \n Nome:")
# Data Do Nascimento Do Cadastrante
Data_do_Cadastrante = input("insira sua Idade: \n Observação: sem '/' e sem espaços. \n - desse modo: 02062005 \n Data: ")

while not Data_do_Cadastrante.isdigit() or ' ' in Data_do_Cadastrante or len(Data_do_Cadastrante) > 8:
    print("deve ser uma sequência númerica (ddmmAAAA) e sem espaços e no máximo 8 digitos")
    Data_do_Cadastrante = input("insira sua Idade: \n Observação: sem '/' e sem espaços. \n Data: ")

# Email Do Cadastrante
Email_do_Cadastrante = input("Digita seu Email: \n Email: ")
regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
while not re.match(regex , Email_do_Cadastrante):
    print("Email Inválido")
    Email_do_Cadastrante = input("Digita seu Email: \n Email: ") 

# Genero Do Cadastrante (capitalize o dado quando for coloca-ló na função (def)) 
Genero_do_Cadastrante = input("Digita seu Genero: \n Observação o sistema do SENAC permite apenas (Masculino e Feminino) \n Genero: ")
while not Genero_do_Cadastrante and Genero_do_Cadastrante.lower() != 'masculino' and Genero_do_Cadastrante.lower() != 'feminino':
    print("Genero não Reconhecido ou Vazio !!!")
    Genero_do_Cadastrante = input("Digita seu Genero: \n Observação o sistema do SENAC permite apenas (Masculino e Feminino) \n Genero: ")
    
# Telefone 1
Primeiro_Telefone_do_Cadastrante = input("Insira seu Primeiro Telefone para Contato: \n Observação: insira o telefone com o DDD (61) ou o seu DDD , e sem parenteses \n Telefone: ")
while not Primeiro_Telefone_do_Cadastrante or not Primeiro_Telefone_do_Cadastrante.isdigit() or len(Primeiro_Telefone_do_Cadastrante) > 11:
    print("formato inválido por favor siga as observações")
    Primeiro_Telefone_do_Cadastrante = input("Insira seu Primeiro Telefone para Contato: \n Observação: insira o telefone com o DDD (61) ou o seu DDD , e sem parenteses \n Telefone: ")

# Telefone 2
Segundo_Telefone_do_Cadastrante = input("Insira seu Segundo Telefone para Contato: \n Observação: insira o telefone com o DDD (61) ou o seu DDD , e sem parenteses '()' \n Telefone: ")
while not Segundo_Telefone_do_Cadastrante or not Segundo_Telefone_do_Cadastrante.isdigit() or len(Segundo_Telefone_do_Cadastrante) > 11:
    print("formato inválido por favor siga as observações")
    Segundo_Telefone_do_Cadastrante = input("Insira seu Segundo Telefone para Contato: \n Observação: insira o telefone com o DDD (61) ou o seu DDD , e sem parenteses '()' \n Telefone: ")

# Nome do Seu Responsavel (capitalize)
Nome_do_Responsavel_Do_Cadastrante = input("Insira o Nome do seu Responsavel: \n Observação: se você for de maior , pode colocar seu proprio nome aí \n Nome Do Responsavel: ")
while not Nome_do_Responsavel_Do_Cadastrante:
    print("O Nome do seu Responsavel Não pode ser Nulo")
    Nome_do_Responsavel_Do_Cadastrante = input("Insira o Nome do seu Responsavel: \n Observação: se você for de maior , pode colocar seu proprio nome aí \n Nome Do Responsavel: ")

# Telefone do seu Responsavel
Telefone_do_Responsavel_Do_Cadastrante = input("Insira o Telefone do seu Responsavel: \n Observação: pode ser o seu proprio telefone se você ja for de maior \n Telefone do Responsavel: ")
while not Telefone_do_Responsavel_Do_Cadastrante or not Telefone_do_Responsavel_Do_Cadastrante.isdigit() or len(Telefone_do_Responsavel_Do_Cadastrante) > 11:
    print("O Telefone do Responsavel Não pode ser Vazia , não pode ter parenteses e deve ser apenas numeros e por favor certifique-se de que a somatoria do seu numero com seu DDD resulta em 11 digitos \n")
    Telefone_do_Responsavel_Do_Cadastrante = input("Insira o Telefone do seu Responsavel: \n Observação: pode ser o seu proprio telefone se você ja for de maior \n Telefone do Responsavel: ")

# Email do seu Responsavel
Email_do_Responsavel_Do_Cadastrante = input("Insira o E-mail do seu Responsavel: \n Observação: caso seja de maior pode ser seu proprio e-mail \n Email do Responsavel: ")
while not re.match(regex , Email_do_Responsavel_Do_Cadastrante):
    print("Email Inválido !!!")
    Email_do_Responsavel_Do_Cadastrante = input("Insira o E-mail do seu Responsavel: \n Observação: caso seja de maior pode ser seu proprio e-mail \n Email do Responsavel: ")

# Cep do Cadastrante
Cep_do_Cadastrante = input("Insira seu CEP: \n Observação: Sem nenhum simbolo apenas os numeros \n CEP: ")
while not Cep_do_Cadastrante.isdigit():
    print("CEP inválido !!!")
    Cep_do_Cadastrante = input("Insira seu CEP: \n Observação: Sem nenhum simbolo apenas os numeros \n CEP: ")
    
# Endereço 
Endereco_do_Cadastrante = input("Insira seu Endereço: \n Observação: \n -> Modo: Endereço QNO/QNN/QNM... Conjunto/Bloco... \n Endereço:")
while not Endereco_do_Cadastrante:
    print("Endereco Não Pode ser Nulo")
    Endereco_do_Cadastrante = input("Insira seu Endereço: \n Observação: \n -> Modo: Endereço QNO/QNN/QNM... Conjunto/Bloco... \n Endereço:")

# Bairro (capitalize)
Bairro_do_Cadastrante = input("Insira seu Bairro: \n -> Brasília (Plano Piloto) \n -> Gama \n -> Taguatinga \n -> Brazlândia \n -> Sobradinho \n -> Planaltina \n -> Paranoá \n -> Núcleo Bandeirante \n -> Ceilândia \n -> Guará \n -> Cruzeiro \n -> Samambaia \n -> Santa Maria \n -> São Sebastião \n -> Recanto das Emas \n -> Lago Sul \n -> Riacho Fundo \n -> Lago Norte \n -> Candangolândia \n -> Águas Claras \n -> Riacho Fundo II \n -> Sudoeste/Octogonal \n -> Varjão \n -> Park Way \n -> SCIA (Setor Complementar de Indústria e Abastecimento) / Estrutural \n -> Sobradinho II \n -> Jardim Botânico \n -> Itapoã \n -> SIA (Setor de Indústria e Abastecimento) \n -> Vicente Pires \n -> Fercal \n -> Sol Nascente/Pôr do Sol \n -> Arniqueira \n Bairro: ")
while not Bairro_do_Cadastrante: 
    print("O Bairro Não pode ser Nulo: ")
    Bairro_do_Cadastrante = input("Insira seu Bairro: \n -> Brasília (Plano Piloto) \n -> Gama \n -> Taguatinga \n -> Brazlândia \n -> Sobradinho \n -> Planaltina \n -> Paranoá \n -> Núcleo Bandeirante \n -> Ceilândia \n -> Guará \n -> Cruzeiro \n -> Samambaia \n -> Santa Maria \n -> São Sebastião \n -> Recanto das Emas \n -> Lago Sul \n -> Riacho Fundo \n -> Lago Norte \n -> Candangolândia \n -> Águas Claras \n -> Riacho Fundo II \n -> Sudoeste/Octogonal \n -> Varjão \n -> Park Way \n -> SCIA (Setor Complementar de Indústria e Abastecimento) / Estrutural \n -> Sobradinho II \n -> Jardim Botânico \n -> Itapoã \n -> SIA (Setor de Indústria e Abastecimento) \n -> Vicente Pires \n -> Fercal \n -> Sol Nascente/Pôr do Sol \n -> Arniqueira \n Bairro: ")

# Número da Casa do Cadastrante
Numero_da_Casa_do_Cadastrante = input("Insira o Número Da Sua Casa: ")
while not Numero_da_Casa_do_Cadastrante.isdigit():
    print("Número Inválido")
    Numero_da_Casa_do_Cadastrante = input("Insira o Número Da Sua Casa: ")

# Complemento do Cadastrante
Complemento_da_Casa_do_Cadastrante = input("Insira o Complemento da sua Casa por favor \n -> se não tiver apenas precione pressione ENTER \n Complemento:")

# Referencia do Cadastrante 
Referencia_da_Casa_do_Cadastrante = input("Insira a Referencia Da Sua Casa \n -> se não tiver referencia apenas pressione ENTER \n Referencia: ")

# Nome Da sua Escola 
Nome_Da_Escola_Do_Cadastrante = input("Insira o Nome Da Sua Escola: ")
while not Nome_Da_Escola_Do_Cadastrante:
    print("Nome da sua Escola Não Pode Ser Nulo , Por favor Insira onde Você Estuda ou Já Estudou , se Já Completou seu Ensino Médio")
    Nome_Da_Escola_Do_Cadastrante = input("Insira o Nome Da Sua Escola: ")

# Estado Letivo (Em Formação ou Concluído)
print("Selecione Qual dessas é a Sua Situação Atual em Relação a Escola: \n ")
situacoes = ['Ensino Fundamental Cursando','Ensino Fundamental Concluído','Ensino Médio Cursando','Ensino Médio Concluído','Ensino Superior Cursando','Ensino Superior Concluído']

# enumerate -> adiciona numeros associado a dados em uma array , tipo array = ['nome','email','senha'] , com enumerate array = [0 => 'nome',1 => 'email' , 2 => 'senha']
for id ,situacao in enumerate(situacoes):
    print(f"Pressione {id} se você está com/em {situacao}")
selecao = input("digite o número referente a sua situação letiva: ")
while int(selecao) > len(situacoes) or int(selecao) < 0 or not selecao.isdigit():
    print("valor inválido")
    selecao = input("digite o número referente a sua situação letiva: ")
indice = int(selecao)
Ano_Letivo = ""
for id, situacao in enumerate(situacoes):
    if indice == id:
        Ano_Letivo = situacao
        break

# Turno Da Escola Do Cadastrante
turnos = ['Matutino','Vespertino']
for id,turno in enumerate(turnos):
    print(f"Pressione {id} para {turno}")
selecao_turno = input("selecione o número desejado: ")
while int(selecao_turno) > len(turnos) or int(selecao_turno) < 0 or not selecao_turno.isdigit():
    print("valor inválido")
    selecao_turno = input("selecione o número desejado: ")
indice_turnos = int(selecao_turno)
Turno_Letivo = ""
for id , turno in enumerate(turnos):
    if id == indice_turnos:
        Turno_Letivo = turno
        break

# Curso de Interesse do Cadastrante
cursos = ['Aprendizagem Profissional de Qualificação em Serviços de Venda','Aprendizagem Profissional de Qualificação em Serviços de Administrativos em Instituições de Saúde','Aprendizagem Profissional de Qualificação em Serviços Administrativos','Aprendizagem Profissional de Qualificação em Serviços de Supermercados','Aprendizagem Profissional de Qualificação em Serviços de Farmácias e Drogarias','Aprendizagem Profissional de Qualificação em Serviços de Desenvolvimento de Software','Aprendizagem Profissional de Qualificação em Serviços de Hotelaria','Aprendizagem Profissional de Qualificação em Serviços de Postos de Combustíveis','Aprendizagem Profissional de Qualificação em Serviços de Aplicações Financeiras','Aprendizagem Profissional de Qualificação em Comércio de Bens, Serviços e Turismo']
for id,curso in enumerate(cursos):
    print(f"Pressione {id} se seu interesse for o Curso de {curso}")
selecao_do_curso = input("Selecione o número do seu interesse: ")
while not selecao_do_curso.isdigit() or int(selecao_do_curso) < 0 or int(selecao_do_curso) > len(cursos):
    print("o curso selecionado não foi reconhecido !!!")
    selecao_do_curso = input("Selecione o número do seu interesse: ")
indice_cursos = int(selecao_do_curso)
Cursos_Interesse = ""
for id, curso in enumerate(cursos):
    if id == indice_cursos:
        Cursos_Interesse = curso
        break
print("\n \n \n Quantas Vezes Pretende Enviar ao SENAC essas informações ? \n")

limite = input("Limite: ")

while not limite.isdigit():
    print("Deve ser um Número por Favor insira um Valor !!!")
    limite = input("Limite: ")



# configura o Service
caminho = "./chromedriver-win64/chromedriver-win64/chromedriver.exe"
servico = Service(caminho)

# configura o Options
options = Options()

# --disable-blink-features=AutomationControlled:  Oculta que o Chrome está sendo controlado pelo Selenium, evitando restrições em sites.
options.add_argument('--disable-blink-features=AutomationControlled')

# --log-level=3 - impede mensagens de automação
options.add_argument('--log-level=3')

driver = webdriver.Chrome(service=servico , options=options)

pyautogui.click(x=1024 , y=130)

try:
    driver.get("https://google.com/")

    # criando uma função 
    def seeding_curriculum_in_senac(param,name,data,email,genero,phone1,phone2,responsavel_nome,responsavel_phone,responsavel_email,cep,endereco,bairro,numero,complemento,referencia,estado,cidade,escola,ano_escolar,turno,cidade_escola,bairro_escola,cursos_de_interesse):
        # pega a URL Pesquisa do Google
        driver.get(param)
        # busca os links do Senac
        links_buttons = WebDriverWait(driver , 20).until(
            expected_conditions.presence_of_all_elements_located((By.XPATH , "//*[contains(text() , 'Clique aqui!')]"))
        )
        # clica no primeiro botão 
        links_buttons[0].click()

        # irá abrir outra aba (target="_blank")
        # driver é o Navegador que estou e também a janela atual que estou (mesmo que o target="_blank" , abra uma nova página ainda estaremos na janela original)
        # window_handles -> todas as janelas abertas (inclusive a que estamos)
        todas_janelas = driver.window_handles

        # janela atual 
        # current_window_handle (pega a atual)
        janela_original = driver.current_window_handle
        # laço de repetição para percorrer todas as janelas (todas_janelas)
        for janelas in todas_janelas:
            # se janelas for diferente da janela atual
            if janelas != janela_original: 
                # se for diferente , troca para (switch_to) janela (window) , janelas que é diferente da atual
                driver.switch_to.window(janelas)
                # quebra o loop
                break
        nome_do_candidato = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "name"))
        )

        nome_do_candidato.click()

        nome_do_candidato.send_keys(name)

        data_do_candidato = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "birthday"))
        )

        data_do_candidato.click()

        data_do_candidato.send_keys(data)

        email_do_candidato = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , 'email'))
        )

        email_do_candidato.click()

        email_do_candidato.send_keys(email)

        genero_do_candidato = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "genre"))
        )
        # aloca a instancia da Classe Select
        # dentro da instancia passa o parametro (input <select>)
        select = Select(genero_do_candidato)
        # seleciona o <option> desejado 
        select.select_by_visible_text(genero)

        first_phone = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "phone_primary"))
        )

        first_phone.click()

        first_phone.send_keys(phone1)

        first_second = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "phone_secondary"))
        )

        first_second.click()

        first_second.send_keys(phone2)

        nome_do_responsavel = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "responsible_name"))
        )

        nome_do_responsavel.click()

        nome_do_responsavel.send_keys(responsavel_nome)

        phone_do_responsavel = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "responsible_phone"))
        )

        phone_do_responsavel.click()

        phone_do_responsavel.send_keys(responsavel_phone)

        email_do_responsavel = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "responsible_email"))
        )

        email_do_responsavel.click()

        email_do_responsavel.send_keys(responsavel_email)

        cep_do_cadastrado = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "zipcode"))
        )

        cep_do_cadastrado.click()

        cep_do_cadastrado.send_keys(cep)

        endereco_do_cadastrado = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "address"))
        )

        endereco_do_cadastrado.click()

        endereco_do_cadastrado.send_keys(endereco)

        bairro_do_cadastrado = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "neighborhood"))
        )

        bairro_do_cadastrado.click()

        bairro_do_cadastrado.send_keys(bairro)

        numero_da_casa_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "number"))
        )

        numero_da_casa_do_cadastrante.click()

        numero_da_casa_do_cadastrante.send_keys(numero)

        complemento_da_casa_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "complement"))
        )

        complemento_da_casa_do_cadastrante.click()

        complemento_da_casa_do_cadastrante.send_keys(complemento)

        referencia_da_casa_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "reference"))
        )

        referencia_da_casa_do_cadastrante.click()

        referencia_da_casa_do_cadastrante.send_keys(referencia)

        estado_da_casa_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "state"))
        )

        select_estado_da_casa_do_cadastrante = Select(estado_da_casa_do_cadastrante)

        select_estado_da_casa_do_cadastrante.select_by_visible_text(estado)

        cidade_da_casa_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "city"))
        )

        select_da_cidade_da_casa_do_cadastrante = Select(cidade_da_casa_do_cadastrante)

        select_da_cidade_da_casa_do_cadastrante.select_by_visible_text(cidade)

        nome_da_escola_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "name_school"))
        )

        nome_da_escola_do_cadastrante.click()

        nome_da_escola_do_cadastrante.send_keys(escola)

        ano_escolar_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "year_school"))
        )

        select_do_ano_escolar_do_cadastrante = Select(ano_escolar_do_cadastrante)

        select_do_ano_escolar_do_cadastrante.select_by_visible_text(ano_escolar)

        turno_escolar_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "shift_school"))
        )

        select_turno_escolar_do_cadastrante = Select(turno_escolar_do_cadastrante)

        select_turno_escolar_do_cadastrante.select_by_visible_text(turno)

        cidade_da_escola_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "city_school"))
        )

        select_cidade_da_escola_do_cadastrante = Select(cidade_da_escola_do_cadastrante)

        select_cidade_da_escola_do_cadastrante.select_by_visible_text(cidade_escola)

        bairro_da_escola_do_cadastrante = WebDriverWait(driver ,10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "district_school"))
        )

        select_bairro_da_escola_do_cadastrante = Select(bairro_da_escola_do_cadastrante)

        select_bairro_da_escola_do_cadastrante.select_by_visible_text(bairro_escola)

        cursos_de_interesse_do_cadastrante = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.NAME , "course"))
        )

        select_cursos_de_interesse_do_cadastrante = Select(cursos_de_interesse_do_cadastrante)

        select_cursos_de_interesse_do_cadastrante.select_by_visible_text(cursos_de_interesse)

        cadastrar_informacoes_do_cadastrante_no_senac = WebDriverWait(driver , 10).until(
            expected_conditions.element_to_be_clickable((By.CLASS_NAME , "btn-primary"))
        )
        
        cadastrar_informacoes_do_cadastrante_no_senac.click()

        # a janela atual (não-original/primeira) fecha
        driver.close()

        # volta para a janela original
        driver.switch_to.window(janela_original)

        # volta para o google
        driver.get("https://google.com/")

    for enviar in range(int(limite)):
        seeding_curriculum_in_senac("https://www.df.senac.br/jovem-aprendiz/",Nome_do_Cadastrante,Data_do_Cadastrante,Email_do_Cadastrante,Genero_do_Cadastrante,Primeiro_Telefone_do_Cadastrante,Segundo_Telefone_do_Cadastrante,Nome_do_Responsavel_Do_Cadastrante,Telefone_do_Responsavel_Do_Cadastrante,Email_do_Responsavel_Do_Cadastrante,Cep_do_Cadastrante,Endereco_do_Cadastrante,Bairro_do_Cadastrante,Numero_da_Casa_do_Cadastrante,Complemento_da_Casa_do_Cadastrante,Referencia_da_Casa_do_Cadastrante,"Distrito Federal","Brasília",Nome_Da_Escola_Do_Cadastrante,Ano_Letivo,Turno_Letivo,"Brasília","Brasília",Cursos_Interesse)
    input("Desativar")
except ValueError :
    print("Error")