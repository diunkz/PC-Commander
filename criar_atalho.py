import os
import win32com.client

# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o programa script.py
program_name = "script.py"
program_path = os.path.join(current_directory, program_name)

# Obtém o nome de usuário atual do sistema
current_user = os.environ.get('USERNAME')

# Caminho completo para a pasta de inicialização do Windows
startup_folder = f"C:\\Users\\{current_user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

# Caminho completo para o atalho na pasta de inicialização
shortcut_path = os.path.join(startup_folder, "Diunkz PC Configurator.lnk")

# Cria o atalho na pasta de inicialização
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = program_path
shortcut.save()
