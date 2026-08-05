
# 📘 Assignment: Jogo da Forca em Python

## 🎯 Objective

Construa um jogo da forca em Python usando strings, loops, condicionais e entrada de dados do usuário. O jogador deverá adivinhar letras para revelar uma palavra oculta antes que as tentativas acabem.

## 📝 Tasks

### 🛠️ Estruturar o loop principal do jogo

#### Descrição
Implemente a lógica central do jogo da forca, incluindo a escolha de uma palavra secreta, leitura de palpites e atualização da palavra exibida a cada rodada.

#### Requisitos
O programa concluído deve:

- Selecionar uma palavra aleatória de uma lista predefinida usando `random.choice()`.
- Aceitar um palpite de uma única letra por rodada com `input()`.
- Mostrar o progresso atual no formato com sublinhados, por exemplo: `_ _ _ _ _`.
- Atualizar o progresso sempre que a letra estiver na palavra secreta.
- Repetir o ciclo até o jogador adivinhar toda a palavra ou esgotar as tentativas.

### 🛠️ Controlar vitória, derrota e feedback

#### Descrição
Adicione a contagem de tentativas incorretas e as mensagens finais para deixar o jogo completo e claro para o jogador.

#### Requisitos
O programa concluído deve:

- Definir um número máximo de tentativas incorretas (exemplo: `6`).
- Diminuir as tentativas restantes apenas quando o palpite estiver incorreto.
- Encerrar o jogo imediatamente quando a palavra for completamente revelada.
- Exibir mensagem de vitória quando o jogador acertar a palavra.
- Exibir mensagem de derrota quando as tentativas acabarem.
- Informar a palavra correta ao final da partida em qualquer cenário.