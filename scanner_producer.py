class ScannerProducer(object):
    def __init__(self, afd, name, tokens):
        # Constructor de la clase ScannerProducer
        # Inicializa los atributos con los valores proporcionados
        self.afd = afd          # Autómata finito determinista
        self.name = name        # Nombre para el archivo de salida
        self.tokens = tokens    # Diccionario de tokens y acciones asociadas
        self.scannerConstructor()  # Llama al método para construir el escáner
        
    def scannerConstructor(self):
        # Método para generar el archivo del escáner
        file = open(f"./{self.name}.py", "w")  # Abre un archivo en modo escritura en la ruta especificada
        file.write("from token_definition import *\n")  # Importa las definiciones de tokens
        file.write("from scanner_simulator import *\n\n")  # Importa el simulador de escáner
        file.write("class AFD(object):\n")  # Define la clase para el autómata finito determinista
        file.write("    def __init__(self):\n")
        file.write(f"        self.regex = {self.afd.regex}\n")  # Inicializa la expresión regular del AFD
        file.write(f"        self.states = {self.afd.states}\n")  # Establece los estados del AFD
        file.write(f"        self.transitions = {self.afd.transitions}\n")  # Establece las transiciones del AFD
        file.write(f"        self.initial_state = '{self.afd.initial_state}'\n")  # Establece el estado inicial del AFD
        file.write(f"        self.final_states = {self.afd.final_states}\n")  # Establece los estados finales del AFD
        file.write(f"        self.symbols = {self.afd.symbols}\n\n")  # Establece los símbolos del alfabeto del AFD
        
        file.write("def tokenScanner(token):\n")  # Define la función tokenScanner
        for i in self.tokens:
            file.write(f"\tif(token == '{i}'):\n")  # Condiciones para cada token
            file.write(f"\t\t{self.tokens[i]}\n")  # Acción asociada al token
        
        file.write(f"\n\treturn ERROR\n\n")  # Devuelve ERROR si no se reconoce el token
        
        file.write("afd = AFD()\n")  # Crea una instancia del AFD
        file.write("simulation('./tests/token_test.txt', tokenScanner, afd)")  # Ejecuta la simulación con el archivo de prueba
        file.close()  # Cierra el archivo después de escribir
