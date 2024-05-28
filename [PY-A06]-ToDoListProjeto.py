def criar_tarefa(cod: str, desc: str, prioridade: str, cat: str) -> bool:
  if len(tarefas) == 0:
    tarefa = {
        'codigo': cod,
        'descricao': desc,
        'prioridade': prioridade,
        'categoria': cat,
        'concluida': False,    
    }
    tarefas.append(tarefa)
    return True
  else:
    for item_lista in tarefas:
      if cod == item_lista['codigo']:
        # print('Já existe este codigo na lista')
        return False
      else:
        tarefa = {
        'codigo': cod,
        'descricao': desc,
        'prioridade': prioridade,
        'categoria': cat,
        'concluida': False,    
        }
        tarefas.append(tarefa)
        return True
  
def exibir_tarefa(lista:list, tipo:int) -> bool:    
  if len(lista) == 0:
    print ("Não existe tarefa!!!")
    return False  # Retorna Falso quando não existe tarefa cadastrada    
  else:
    print('='*30)

    if tipo == 1: # Prioridade - Baixa, Media, Alta
        prioridade = input("Qual prioridade - (Baixa, Media, Alta): ").strip().upper()
    elif tipo == 2:
        categoria = input("Qual categoria - (Estudo, Lazer, Trabalho): ").strip().upper()   
    
    
    for item_lista in lista:
      if tipo == 1: # Prioridade - Baixa, Media, Alta
        # prioridade = input("Qual prioridade - (Baixa, Media, Alta): ").strip().upper()
        
        if item_lista['prioridade'] == prioridade:
          print(prioridade)
          print(f'Codigo da Tarefa:    {item_lista ["codigo"]}')
          print(f'Descrição da Tarefa: {item_lista ["descricao"]}')
          print(f'Prioridade da Tarefa: {item_lista ["prioridade"]}')
          print(f'Categoria da Tarefa: {item_lista ["categoria"]}')
          print(f'Status da tarefa:    {item_lista ["concluida"]}')
          print('='*30)        

      elif tipo == 2:
        # categoria = input("Qual categoria - (Estudo, Lazer, Trabalho): ").strip().upper()      
        if item_lista['categoria'] == categoria:
          print(categoria)
          print(f'Codigo da Tarefa:    {item_lista ["codigo"]}')
          print(f'Descrição da Tarefa: {item_lista ["descricao"]}')
          print(f'Prioridade da Tarefa: {item_lista ["prioridade"]}')
          print(f'Categoria da Tarefa: {item_lista ["categoria"]}')
          print(f'Status da tarefa:    {item_lista ["concluida"]}')
          print('='*30)
        

      else:
        print('='*30)
        print(f'Codigo da Tarefa:    {item_lista ["codigo"]}')
        print(f'Descrição da Tarefa: {item_lista ["descricao"]}')
        print(f'Prioridade da Tarefa: {item_lista ["prioridade"]}')
        print(f'Categoria da Tarefa: {item_lista ["categoria"]}')
        print(f'Status da tarefa:    {item_lista ["concluida"]}')
    return True  # Retorna True quando existe tarefa cadastrada

def concluir_tarefa(lista:list, cod: str):
  i = 0
  if len(lista) == 0:
    return "Não existe tarefa!!!"
  else:
    for item_lista in lista:
      if cod == item_lista['codigo']:
        lista[i]['concluida'] = True
        return "Tarefa Concluida"
      i += 1
    return "Essa tarefa não existe"
  
def excluir_tarefa(lista: list, cod: str):
  i = 0
  if len(lista) == 0:
    return "Não existe tarefa!!!"
  else:
    for item_lista in lista:
      if cod == item_lista['codigo']:
        lista.pop(i)
        return "Tarefa Excluida"
      i += 1
    return "Essa tarefa não existe"        

# Lista que contem as tarefas
tarefas = []
controle = True
while controle:
    print("""
            CRIAR TAREFA     ( 1 )
            EXIBIR TAREFAS   ( 2 )
            CONCLUIR TAREFA  ( 3 )
            EXCLUIR TAREFA   ( 4 )
            SAIR             ( 0 )
          """)
    opcao = input("Digite a Opção: ")
    
    match opcao:
        case '1':
          print('='*30)
          print('CRIAR TAREFA')
          codigo_tarefa = input('Entre com o codigo da Tarefa: ').strip()
          descricao_tarefa = input('Digite a Descrição da Tarefa: ').strip().upper()          
          prioridade_tarefa = input('Digite a Prioridade da Tarefa: ').strip().upper()
          categoria_tarefa = input('Entre com a categoria da Tarefa: ').strip().upper()
          if criar_tarefa(codigo_tarefa, descricao_tarefa, prioridade_tarefa, categoria_tarefa) == True:
            print('Tarefa criada com Sucesso!!!')
          else:
            print('Já existe este codigo na lista')                    
          print('='*30)    

        case '2':
          print('='*30)
          print('EXIBIR TAREFAS')
          tipo = input('Entre com a forma que deseja imprimir - (1-PRIORIDADE | 2-CATEGORIA | 3-TODAS): ').strip()
          exibir_tarefa(tarefas, int(tipo))
          print('='*30)

        case '3': 
          print('='*30)          
          print('CONCLUIR TAREFA')          
          if exibir_tarefa(tarefas,3) == True:
            print("Na lista, qual tarefa deseja concluir: ")
            codigo = input('Entre com o codigo da Tarefa: ')
            print(concluir_tarefa(tarefas, codigo))          
          print('='*30)

        case '4': 
          print('EXCLUIR TAREFA')
          if exibir_tarefa(tarefas,3) == True:
            print("Na lista, qual tarefa deseja concluir: ")
            codigo = input('Entre com o codigo da Tarefa: ')
            print(excluir_tarefa(tarefas, codigo))

        case '0':
          controle = False

        case _:
          print('OPÇÃO INVALIDA')
else:
  # print(tarefas)
  print('Saindo do Sistema')
