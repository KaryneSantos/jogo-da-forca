import random

def sortear_palavra():
    palavras = ["python", "linguagem", "computacao", "programacao", "tecnico"]
    return random.choice(palavras)

def forca(palavra):
    palavra_oculta = ["_"] * len(palavra)
    tentativas = 6
    letras_incorretas = []

    while tentativas > 0 and "_" in palavra_oculta:
        letra = input("Digite uma letra:").lower()

        if letra in palavra:
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
            print("Palavra:", " ".join(palavra_oculta))
        else:
            tentativas -= 1
            letras_incorretas.append(letra)
            print(f"Letras erradas: {', '.join(letras_incorretas)}")
            print(f"Tentativas restantes: {tentativas}")

    if "_" not in palavra_oculta:
        print("Parabéns! Você ganhou!")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

palavra_aleatoria = sortear_palavra()
print("Jogo da Forca - Tente adivinhar a palavra:")
forca(palavra_aleatoria)
