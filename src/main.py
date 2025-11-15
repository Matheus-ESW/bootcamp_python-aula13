import schedule
import time
from lib.classes.CsvSources import CsvSources
from lib.classes.TxtSources import TxtSources
from lib.classes.JsonSources import JsonSources

# Função para verificar novos arquivos
def check_for_new_files():
    csv_source.check_for_new_files()  # Chama o método check_for_new_files da instância
    txt_source.check_for_new_files()
    json_source.check_for_new_files()

# Agendando a execução da função check_for_new_files() a cada segundo
schedule.every(10).seconds.do(check_for_new_files)

csv_source = CsvSources()
txt_source = TxtSources()
json_source = JsonSources()

# Executa o loop principal
while True:
    schedule.run_pending()
    time.sleep(1)  # Aguarda 1 segundo para que o loop não consuma muito processamento