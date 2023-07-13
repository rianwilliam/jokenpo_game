import random

opcoes = {
    "1": "pedra",
    "2": "papel",
    "3": "tesoura",
}

print("Bem-vindo ao jogo de pedra papel tesoura")
print("[1] pedra  [2] papel  [3] tesoura")
jogada = opcoes[input()]

jogadaBot = opcoes[str(random.choice([1,2,3]))]

print(f"Jogada do Jogador: {jogada}, jogada do bot: {jogadaBot}")

if jogada == jogadaBot:
    print("Empate")
elif jogada == "pedra" and jogadaBot == "tesoura" or jogada == "papel" and jogadaBot == "pedra" or jogada == "tesoura" == jogadaBot == "papel":
    print("Jogador venceu")
else:
    print("jogador perdeu!!")
