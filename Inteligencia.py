import google.generativeai as genai

def detectar_ingredientes(chave, imagem):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = '''Liste quais são os ingredientes dessa imagem.
    Os ingredientes devem ser apresentados em uma lista separada por vírgula, como no exemplo a seguir.
    Nenhum texto adicional deve ser gerado como resposta além dos próprios ingredientes.
    # Exemplo de saída
    arroz, feijão, frango
    '''

    resposta = modelo.generate_content([prompt, imagem])

    ingredientes = resposta.text.split(",")
    return ingredientes

def possiveis_receitas(chave, ingredientes):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f'''Considerando a seguinte lista de ingredientes, gere uma lista de receitas culinárias que os utilizes.
    As receitas devem tentar incluir a maior parte dos ingredientes.
    Gere apenas uma lista com os nomes das receitas, separados por virgula.
    
    # Lista de Ingredientes
    {ingredientes}
    
    # Exemplo de saída
    Receita 1 (BOLO DE CENOURA), Receita 2 (TORTA DE LIMÃO), Receita 3 (MARRACONADA), ETC
    '''

    resposta = modelo.generate_content(prompt)

    receitas = resposta.text.split(",")
    return ingredientes


def receita_completa (chave, ingredientes, receita):
    genai.configure(api_key=chave)
    modelo = genai.GenerativeModel('gemini-1.5-flash')

    prompt = f''' Crie a receita para o prato: "{receita}".
    Inclua a maior quantidade possível dos ingreientes da lista de ingredientes.
    
    # Lista de ingredientes
    {ingredientes}
    '''

    resposta = modelo.generate_content(prompt)
    return resposta.text
