import csv #improtando csv

# Função para carregar os dados do csv:
def load_data(file_path):
    try:
        with open(file_path, newline='', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return []  # vazio

#Função para calular a média.

def calculate_average_rating(data_lines, company):
    company_movies = [float(movie["Rate"]) for movie in data_lines if movie["Company"] == company]
    return sum(company_movies) / len(company_movies) if company_movies else 0

# Função para calular o orçamento.

def calculate_total_budget(data_lines, company):
    return sum(int(movie["Budget"]) for movie in data_lines if movie["Company"] == company)

#Função para calular o faturamento.

def calculate_total_gross(data_lines, company):
    return sum(int(movie["Gross Worldwide"]) for movie in data_lines if movie["Company"] == company)

def main():
    file_path = input("Informe o caminho do arquivo CSV: ")
    data_lines = load_data(file_path)
    
    while True:
        print("\nOpções:")
        print("1. Na avaliação do público, quem vence esse duelo?")
        print("2. Em relação ao orçamento, quem vence esse duelo?")
        print("3. Em relação ao faturamento, quem vence esse duelo?")
        print("4. Filtrar filmes por avaliação")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            marvel_avg = calculate_average_rating(data_lines, 'Marvel')
            dc_avg = calculate_average_rating(data_lines, 'DC')
            winner = "Marvel" if marvel_avg > dc_avg else "DC"
            print(f"Média de avaliação: Marvel - {marvel_avg:.2f}, DC - {dc_avg:.2f}")
            print(f"Quem tem a maior nota é a : {winner}")
        
        elif choice == '2':
            marvel_budget = calculate_total_budget(data_lines, 'Marvel')
            dc_budget = calculate_total_budget(data_lines, 'DC')
            winner = "Marvel" if marvel_budget > dc_budget else "DC"
            print(f"Total de orçamento: Marvel - {marvel_budget:.2f}, DC - {dc_budget:.2f}")
            print(f"Quem tem mais orçamento é a : {winner}")
        
        elif choice == '3':
            marvel_gross = calculate_total_gross(data_lines, 'Marvel')
            dc_gross = calculate_total_gross(data_lines, 'DC')
            winner = "Marvel" if marvel_gross > dc_gross else "DC"
            print(f"Total de faturamento: Marvel : - {marvel_gross:.2f}, DC : - {dc_gross:.2f}")
            print(f"Quem tem mais faturamento é a: {winner}")
        
        elif choice == '4':
            rating_threshold = float(input("Informe a nota mínima para o filtro: "))
            print(f"Filmes com avaliação maior ou igual a: {rating_threshold}:")
            for movie in data_lines:
                if float(movie["Rate"]) >= rating_threshold:
                    print(f"Filme: {movie['Original Title']} | Avaliação: {movie['Rate']}")
        
        elif choice == '5':
            print("Encerrando o programa.")
            break
        
        else:
            print("Eita! opção errada, escolha novamente por favor.")

if __name__ == "__main__":
    main()
