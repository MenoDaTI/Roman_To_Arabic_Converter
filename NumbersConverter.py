# Definindo a classe ConversorNumeros
class ConversorNumeros:
    # método construtor
    def __init__(self):
       # listas de valores e algarismos romanos
        self.valores = [1000, 900, 500, 400, 100, 90,50, 40, 10, 9,5, 4, 1]
        self.romanos = ["M", "CM","D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        # dicionário de valores romanos
        self.romano_valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Método para converter números arábicos em romanos
    def arabico_para_romano(self, numero):
        # inicializando a string do resultado
        resultado_romano = ""
        #Iterando sobre os valores arábicos
        for i in range(len(self.valores)):
            #adicionando os algarismos romanos correspondentes enquanto o número for maior ou igual ao valor arábico atual
            while numero >= self.valores[i]:
                resultado_romano += self.romanos[i]
                numero -= self.valores[i]
        return resultado_romano

    # Método para converter algarismos romanos em números arábicos
    def romano_para_arabico(self,romano):
        numero_arabico = 0
        i = 0
        while i < len(romano):
            # Verificando se há um algarismo menor antes de um algarismo maior
            if i + 1 < len(romano) and self.romano_valores[romano[i]] < self.romano_valores[romano[i + 1]]:
                # Subtraindo o valor do algarismo menor do algarismo maior
                numero_arabico += self.romano_valores[romano[i + 1]] - self.romano_valores[romano[i]]
                i +=2
            else:
                # Adicionando o valor do algarismo atual ao resultado
                numero_arabico += self.romano_valores[romano[i]]
                i+= 1
        return numero_arabico
# Função principal
def main():
    # Criando uma instância da classe ConversorNumeros
    conversor = ConversorNumeros()
    # Solicitando ao usuário para escolher a conversão
    escolha = input("Escolha a conversão (1 para arábico para romano, 2 para romano para arábico): ")

    # Verificando a escolha do usuário
    if escolha == '1':
        numero_arabico = int(input("Digite o número arábico: "))
        resultado_romano = conversor.arabico_para_romano(numero_arabico)
        print(f"{numero_arabico} em algarismos romanos: {resultado_romano}")
    elif escolha == '2':
        numero_romano = input("Digite os algarismos romanos: ")
        resultado_arabico = conversor.romano_para_arabico(numero_romano)
        print(f"{numero_romano} em arábico: {resultado_arabico}")
    else:
        # Se a escolha não for válida, exibindo uma mensagem de erro
        print("Escolha inválida.")
if __name__ == "__main__":
    main()
