class Pagina:
    def __init__(self, url, titulo):
        self.url = url
        self.titulo = titulo
        self.proxima_pagina = None
        self.pagina_anterior = None

class HistoricoNavegacao:
    def __init__(self):
        self.pagina_atual = None

    def adicionar_pagina(self, url, titulo):
        # Cria uma nova página com a URL e o título fornecidos
        nova_pagina = Pagina(url, titulo)
        # Se já houver uma página atual, ajusta as referências para adicionar a nova página ao final do histórico
        if self.pagina_atual:
            nova_pagina.pagina_anterior = self.pagina_atual
            self.pagina_atual.proxima_pagina = nova_pagina
        # Define a nova página como a página atual
        self.pagina_atual = nova_pagina

    def inserir_no_inicio(self, url, titulo):
        # Cria uma nova página com a URL e o título fornecidos
        nova_pagina = Pagina(url, titulo)
        # Define a próxima página da nova página como a página atual
        nova_pagina.proxima_pagina = self.pagina_atual
        # Se já houver uma página atual, ajusta a página anterior da página atual para a nova página
        if self.pagina_atual:
            self.pagina_atual.pagina_anterior = nova_pagina
        # Define a nova página como a página atual
        self.pagina_atual = nova_pagina

    def remover(self, titulo):
        atual = self.pagina_atual

        # Caso especial: remoção do primeiro elemento
        if atual and atual.titulo == titulo:
            self.pagina_atual = atual.proxima_pagina   # Atualizando a página atual para o próximo nó
            return

        # Busca pela página a ser removida
        anterior = None
        while atual and atual.titulo != titulo:
            anterior = atual
            atual = atual.proxima_pagina

        # Se a página não foi encontrada, não há nada a fazer
        if not atual:
            return

        # Remove a página, atualizando as referências da página anterior
        if anterior:
            anterior.proxima_pagina = atual.proxima_pagina

    def imprimir_historico(self):
        pagina = self.pagina_atual
        # Percorre o histórico, imprimindo cada página
        while pagina:
            print("Título:", pagina.titulo, "| URL:", pagina.url)
            pagina = pagina.proxima_pagina 

# Exemplo de uso
historico = HistoricoNavegacao()

# Adiciona páginas ao histórico
historico.inserir_no_inicio("https://www.google.com", "Google")
historico.inserir_no_inicio("https://www.openai.com", "OpenAI")
historico.inserir_no_inicio("https://www.python.org", "Python")

print("Lista original:")
# Imprime o histórico original
historico.imprimir_historico()

# Insere uma página no início do histórico
historico.inserir_no_inicio("https://www.example.com", "Exemplo")
print("\nInserção no início:")
# Imprime o histórico após a inserção
historico.imprimir_historico()

# Remove uma página do histórico
historico.remover("OpenAI")
print("\nRemoção do elemento 'OpenAI':")
# Imprime o histórico após a remoção
historico.imprimir_historico()
