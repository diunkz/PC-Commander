import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
import os
import psutil

def desligar_pc():
    # Executa o comando para desligar o PC
    os.system("shutdown /s /t 1")

def processos_consumo_ram():
    # Obtém a lista de todos os processos em execução
    lista_processos = list(psutil.process_iter(attrs=['pid', 'name', 'memory_info']))

    # Filtra os processos que estão consumindo mais de 150MB de RAM
    processos_acima_150mb = [p for p in lista_processos if p.info['memory_info'].rss > 150 * 1024 * 1024]

    # Constrói a string com informações dos processos
    if processos_acima_150mb:
        info_processos = ""
        for processo in processos_acima_150mb:
            nome = processo.info['name']
            consumo_mb = processo.info['memory_info'].rss / (1024 * 1024)
            info_processos += f"Processo: {nome}, Consumo de RAM: {consumo_mb:.2f} MB\n"
    else:
        info_processos = "Não há processos consumindo mais de 500MB de RAM."

    return info_processos

# Função para processar as mensagens recebidas
def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        if command == '/start':
            # Mostra o menu de opções ao iniciar o bot
            show_menu(chat_id)
        elif command == 'Mostrar Processos abertos':
            bot.sendMessage(chat_id, processos_consumo_ram())
        elif command == 'Desligar PC':
            bot.sendMessage(chat_id, 'PC desligando...')
            desligar_pc()

# Função para mostrar o menu de opções com botões
def show_menu(chat_id):
    # Cria os botões para o menu
    button1 = KeyboardButton(text='Mostrar Processos abertos')
    button2 = KeyboardButton(text='Desligar PC...')

    # Cria o teclado com os botões
    keyboard = ReplyKeyboardMarkup(keyboard=[[button1], [button2]], resize_keyboard=True)

    # Envia a mensagem com o menu de opções
    bot.sendMessage(chat_id, 'Escolha uma opção:', reply_markup=keyboard)

# Token do seu bot do Telegram
diretorio_atual_token = os.path.dirname(os.path.abspath(__file__))
caminho_token = os.path.join(diretorio_atual_token, 'token.txt')

with open(caminho_token, 'r') as arquivo_token:
    TOKEN = arquivo_token.read().strip()

# Inicializa o bot
bot = telepot.Bot(TOKEN)
bot.message_loop(handle_message)

print('Programa iniciado!')
print()
print('Não é necessário fechar, apenas minimize')
print('Você também pode redimensionar a janela para ficar menor.')
print()
print('Pressione Ctrl+c para finalizar este programa.')
print()
print("\t\t\tFeito por Noah Diunkz! ;)")
print("\t\t\tgithub.com/diunkz")

# Variável de controle para saída do loop principal
ativo = True

# Loop principal
while ativo:
    try:
        # Mantém o programa rodando
        pass
    except KeyboardInterrupt:
        # Permite que o usuário interrompa o script com Ctrl+C
        ativo = False

print('Bot encerrado!')
