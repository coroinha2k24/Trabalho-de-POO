medicos = [
    { "nome":"dr. Cecilia",
     "idade":"23",
     "cpf":"124.234.123.54",
     "rg":"fg789094",
     "crm":"mgp1765",
     "telefone":"(99)457556-56654",
     "endereco":"rua antônio lima número:89",
     "sexo":"m",
     "senha":"454gh68",
        },

        {"nome":"dr. Mauricio",
     "idade":"28",
     "cpf":"301.890.987.90",
     "rg":"30e108908",
     "crm":"juiui89090",
     "telefone":"(99)994028922",
     "endereço":"gonçalves dias numero:59",
     "sexo":"f",
     "senha":"tvdgghj",
     },
     {
     "nome":"dr. Ricardo",
     "idade":"90",
     "cpf":"678.896.123.87",
     "rg":"786378388",
     "crm":"juteri865456",
     "telefone":"(99)998765432",
     "endereço":"pedro daniel numero:34",
     "sexo":"m",
     "senha":"123456778",

       }
    
    ]
pacientes = [
    { "nome":"gabriel",
    "cpf":"678.908.987.98",
    "rg":"67y9867547",
    "telefone":"(99)9876544",
    "endereco":"rua alves numero:67",
    "sexo":"m",
    "convenio":"67890",

    },

       { "nome":"Cecilia",
     "CPF":"204.183.033.07",
     "rg":"20b1367",
     "telefone":"(88) 2008-3894",
     "endereco":"rua vitoria regia numero:17",
     "sexo":"f",
     "convenio":"13537",

    },

    { "nome":"Larissa",
     "CPF":"137.295.831.05",
     "rg":"62n0178",
     "telefone":"(88) 3918-0312",
     "endereco":"rua das palmeiras numero:38",
     "sexo":"f",
     "convenio":"08428",

    }
]
convenios=[
    { "nome":"Fernando",
    "telefone":"(88)99652-3598",
    "endereco":"rua do sabia n4",
    "cnpj":"728139",
   },
   { "nome":"Eliane",
    "telefone":"(88)99657-0102",
    "endereco":"sitio saco n6",
    "cnpj":"843128",
   },
   
   { "nome":"Eliakim",
    "telefone":"(88)5432-8921",
    "endereco":"rua jaguaribe n73",
    "cnpj":"843769",
   }
    
]

consultas = [
    {   
        "medico": "Dr. vinicius",
        "paciente":"Sara V.",
        "data" : "16/09/2025",
        "hora inicial" : "12:00",
        "hora final" : "1:00",
        "descrição" : "consulta do ouvido"
    },
        {
            
        "medico": "Dr. carlos alexandre",
        "paciente":"Sara V.",
        "data" : "16/09/2024",
        "hora inicial" : "1:00",
        "hora final" : "5:00",
        "descrição" : "consulta braço"
    },
        {

        "medico": "Dr.Vitória",
        "paciente":"Sara V.",
        "data" : "16/09/2026",
        "hora inicial" : "2:00",
        "hora final" : "3:00",
        "descrição" : "consulta da cabeça"
    }
]

compromissos = [
{
    "data":"23/05/2026",
    "hora inicial":"09;54",
    "hora final":"21;59",
    "descricao":"formatura",
},
{
    "data":"31/09/2024",
    "hora inicial":"12::40",
    "hora final":"16;00",
    "descricao":"casamento",
}]



from datetime import datetime
import re

def validar_data(data_str):
    try:
        datetime.strptime(data_str, '%d/%m/%Y')
        return True
    except ValueError:
        return False


def cadastrarMedicos():
    nomemed = input("digite o nome do medico")
    idademed =input("digite a idade do medico ")
    cpfmed = input("digite o cpf do medico ")
    rgmed = input("digite o rg do medico ") 
    crmmed = input("digite o crm do medico")
    telefonemed =input("digite o telefone do medico")
    enderecomed = input("digite o endereço do medico")
    sexomed = input("digite o sexo do medico")
    senhamed = ("digite a senha do medico")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("os dados foram cadrastados com sucesso")
        medicos.append({"nome":nomemed,
                "idade":idademed,
                "cpf": cpfmed,
                "rg":rgmed,
                "crm":crmmed,
                "telefone":telefonemed,
                "endereço":enderecomed,
                "sexo":sexomed,
                "senha":senhamed })
        print(medicos)
    else:
        print("programa cancelado!")
        breakpoint
    

def cadastrarPacientes():
    nome = input("Digite o nome do paciente: ")
    cpf = input("Digite o CPF do paciente: ")
    rg = input("Digite o RG do paciente: ")
    telefone = input("Digite o telefone do paciente: ")
    endereco = input("Digite o endereço do paciente: ")
    sexo = input("Digite o sexo do paciente (M/F): ")
    convenio = input("Digite o convenio que o paciente está associado: ")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("os dados foram cadrastados com sucesso")
        pacientes.append({"nome":nome,
                "cpf": cpf,
                "rg":rg,
                "telefone":telefone,
                "endereço":endereco,
                "sexo":sexo,
                "convenio":convenio })
        print(pacientes)
    else:
        print("progra1ma cancelado!")
        breakpoint

def cadastrarConvenios():
    nome=input("digite o seu nome:")
    fone=input("digite seu telefone para contato:")
    endereco=input("digite seu endereço:")
    cnpj=input("digite seu cnpj:")
    p= input("você deseja salva as informaçoes?(sim/não)")
    if p == "sim":
        print("os dados foram cadrastados com sucesso")
        convenios.append({"nome":nome,
                "telefone":fone,
                "endereço":endereco,
                "cnpj":cnpj})
        print(convenios)
    else:
        print("programa cancelado!")
        breakpoint

def buscarMedicos():
    print("Informe o nome ou CRM do médico que deseja buscar:")
    busm = input("")
    resultados = [medico for medico in medicos if busm.lower() == medico.get('nome', '').lower() or busm == medico.get('crm', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CRM: {resultado['crm']}")
    else:
        print("Nenhum médico encontrado.")

def buscarPacientes():
    print("Informe o nome ou CPF do paciente que deseja buscar:")
    busp = input("")
    resultados = [paciente for paciente in pacientes if busp.lower() == paciente.get('nome', '').lower() or busp == paciente.get('cpf', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CPF: {resultado['cpf']}")
    else:
        print("Nenhum paciente encontrado.")

def buscarConvenios():
    print("Informe o nome ou CNPJ do convênio que deseja buscar:")
    busc = input("")
    resultados = [convenio for convenio in convenios if busc.lower() == convenio.get('nome', '').lower() or busc == convenio.get('cnpj', '')]
    if resultados:
        for resultado in resultados:
            print(f"Nome: {resultado['nome']}, Telefone: {resultado['telefone']}, CNPJ: {resultado['cnpj']}")
    else:
        print("Nenhum convênio encontrado.")

def alterarMedicos():
  
  print("Informe o CRM do médico que deseja alterar:")
  crm = input("")
  medico = next((medico for medico in medicos if medico['crm'] == crm), None)
  if medico:
        print(f"Dados atuais: {medico}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({medico['nome']}): ") or medico['nome']
        cpf = input(f"CPF ({medico['cpf']}): ") or medico['cpf']
        rg = input(f"RG ({medico['rg']}): ") or medico['rg']
        telefone = input(f"Telefone ({medico['telefone']}): ") or medico['telefone']
        endereco = input(f"Endereço ({medico['endereco']}): ") or medico['endereco']
        sexo = input(f"Sexo ({medico['sexo']}): ") or medico['sexo']
        senha = input(f"Senha ({medico['senha']}): ") or medico['senha']
        medico.update({
            "nome": nome,
            "cpf": cpf,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "senha": senha
        })
        print("Dados do médico atualizados.")
        print(medicos)
  else:
        print("Médico não encontrado.")

def alterarPacientes():

    print("Informe o CPF do paciente que deseja alterar:")
    cpf = input("")
    paciente = next((paciente for paciente in pacientes if paciente['cpf'] == cpf), None)
    if paciente:
        print(f"Dados atuais: {paciente}")
        print("Forneça os novos dados (deixe em branco para manter o valor atual):")
        nome = input(f"Nome ({paciente['nome']}): ") or paciente['nome']
        rg = input(f"RG ({paciente['rg']}): ") or paciente['rg']
        telefone = input(f"Telefone ({paciente['telefone']}): ") or paciente['telefone']
        endereco = input(f"Endereço ({paciente['endereco']}): ") or paciente['endereco']
        sexo = input(f"Sexo ({paciente['sexo']}): ") or paciente['sexo']
        convenio = input(f"Convênio ({paciente['convenio']}): ") or paciente['convenio']
        paciente.update({
            "nome": nome,
            "rg": rg,
            "telefone": telefone,
            "endereco": endereco,
            "sexo": sexo,
            "convenio": convenio
        })
        print("Dados do paciente atualizados.")
    else:
        print("Paciente não encontrado.")
    
def marcarCompromisso():
    print("Você deseja marcar um compromisso? Digite: S para sim e N para não.")
    com = input("")
    if com.upper() == "S":
        data = input("Informe a data do compromisso (formato DD/MM/AAAA): ")
        if not validar_data(data):
            print("Data inválida. Encerrando o programa.")
            return
        
        hi = input("Informe a hora inicial do compromisso (formato HH:MM): ")
        hf = input("Informe a hora final do compromisso (formato HH:MM): ")
        desc = input("Descreva o seu compromisso: ")
        
        compromissos.append({
            "data": data,
            "hora inicial": hi,
            "hora final": hf,
            "descrição": desc
        })
        print("Compromisso marcado com sucesso!")
        print(f"Seu compromisso foi agendado com os seguintes dados: {compromissos[-1]}")
    else:
        print("Programa cancelado!")

def marcarConsulta():
    print("Você quer marcar uma consulta? (sim/não)")
    mc = input("")
    if mc.upper() == "sim":
        nm = input("Informe o nome do médico: ")
        mencontrado = next((medico for medico in medicos if medico['nome'] == nm), None)
        if mencontrado:
            pnome = input("Informe o nome do paciente: ")
            pencontrado = next((paciente for paciente in pacientes if paciente['nome'] == pnome), None)
            if pencontrado:
                data = input("Informe a data da consulta (formato DD/MM/AAAA): ")
                if not validar_data(data):
                    print("Data inválida. Encerrando o programa.")
                    return
                
                hi = input("Informe a hora inicial da consulta (formato HH:MM): ")
                hf = input("Informe a hora final da consulta (formato HH:MM): ")
                desc = input("Descreva a consulta: ")
                
                consultas.append({
                    "data": data,
                    "hora inicial": hi,
                    "hora final": hf,
                    "medico": nm,
                    "paciente": pnome,
                    "descrição": desc
                })
                print("Consulta marcada com sucesso!")
                print(f"Os dados da consulta são: {consultas[-1]}")
            else:
                print("Paciente não encontrado.")
        else:
            print("Médico não encontrado.")
    else:
        print("Programa cancelado!")

def emitirRelatorio():
    print("Qual relatório você deseja emitir?")
    print("1 - Médicos cadastrados")
    print("2 - Pacientes cadastrados")
    print("3 - Convênios")
    print("4 - Consultas realizadas em um intervalo de data")
    print("5 - Compromissos realizados em um intervalo de data")
    
    escolha = input("Escolha uma opção: ")
    if escolha == "1":
        print("Médicos cadastrados:")
        for medico in medicos:
            print(f"Nome: {medico['nome']}, CPF: {medico['cpf']}, CRM: {medico['crm']}, Telefone: {medico['telefone']}")
    elif escolha == "2":
        print("Pacientes cadastrados:")
        for paciente in pacientes:
            print(f"Nome: {paciente['nome']}, CPF: {paciente['cpf']}, Telefone: {paciente['telefone']}")
    elif escolha == "3":
        print("Convênios:")
        for convenio in convenios:
            print(f"Nome: {convenio['nome']}, CNPJ: {convenio['cnpj']}, Telefone: {convenio['telefone']}")
    elif escolha == "4":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Encerrando o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Encerrando o programa.")
            return
        
        print(f"Consultas de {data_inicio} a {data_fim}:")
        for consulta in consultas:
            data_consulta = consulta.get("data", "")
            if data_inicio <= data_consulta <= data_fim:
                print(f"Data: {consulta['data']}, Horário: {consulta['hora inicial']}-{consulta['hora final']}, Médico: {consulta['medico']}, Paciente: {consulta['paciente']}, Descrição: {consulta['descrição']}")
    elif escolha == "5":
        data_inicio = input("Informe a data de início (formato DD/MM/AAAA): ")
        if not validar_data(data_inicio):
            print("Data de início inválida. Por favor reinicie o encerre o programa.")
            return
        
        data_fim = input("Informe a data de fim (formato DD/MM/AAAA): ")
        if not validar_data(data_fim):
            print("Data de fim inválida. Por favor reinicie o encerre o programa.")
            return
        
        print(f"Compromissos de {data_inicio} a {data_fim}:")
        for compromisso in compromissos:
            data_compromisso = compromisso.get("data", "")
            if data_inicio <= data_compromisso <= data_fim:
                print(f"Data: {compromisso['data']}, Horário: {compromisso['hora inicial']}-{compromisso['hora final']}, Descrição: {compromisso['descrição']}")
    else:
        print("Opção inválida. Encerrando o programa.")
a = True
while a:
   
   lang = input("1 - Cadastrar Médico\n"
                "2 - Cadastrar Paciente\n"
                "3 - Cadastrar Convênio\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer?")


   match lang:
       case "1":
            cadastrarMedicos()
            
       case "2":
           cadastrarPacientes()
           
       case "3":
           cadastrarConvenios()
       
       case "4":
           buscarMedicos()
   
       case "5":
           buscarPacientes()
           
       case "6":
           buscarConvenios()
   
       case "7":
           alterarMedicos()
   
       case "8":
           alterarPacientes()
       
       case "9":
           marcarCompromisso()
   
       case "10":
           marcarConsulta()
   
       case "11":
           emitirRelatorio()
       
       case "12":
           print("Programa Encerrado!")
           breakpoint
   
       case _:
           print("Escolha uma opção válida")
           lang = input("O que você deseja fazer? \n"
               "1 - Cadastrar Médicos\n"
                "2 - Cadastrar Pacientes\n"
                "3 - Cadastrar Convênios\n"
                "4 - Buscar Médicos\n"
                "5 - Buscar Pacientes\n"
                "6 - Buscar Convênios\n"
                "7 - Alterar Medicos\n"
                "8 - Alterar Pacientes\n"
                "9 - Marcar Compromisso\n"
                "10 - Marcar Consulta\n"
                "11 - Emitir Relatorio\n"
                "12 - Encerrar Programa\n"
                "O que você deseja fazer? ")
   