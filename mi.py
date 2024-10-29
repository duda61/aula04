nome_digitado = input("Digite seu nome: ")
idade_digitada = int(input("Digite seu idade: "))
cpf_digitada = input("Digite seu cpf: ")
telefone = input("Digite seu telefone: ")

aluno={
    "Nome":nome_digitado,
    "Idade": idade_digitada,
    "cpf": cpf_digitada,
    "telefone":telefone,
  }
if aluno["Idade"] >18:
  print(f"O aluno {nome_digitado} é maior de idade")
else:
  print(f"O aluno {nome_digitado} é menor de idade")



