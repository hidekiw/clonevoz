# Clonevoz

Clonar voz com arquivo de audio e conversor de texto para audio.

Só funciona com arquivos .wav

## Instalação

git clone https://github.com/hidekiw/clonevoz
cd clonevoz
pip install -r requirements
iniciar.bat
http:\\127.0.0.1:8085\docs

## 🧠 Git – Boas Práticas da Equipe

Bem-vindo(a)! Este repositório segue um conjunto de boas práticas para garantir organização, qualidade e colaboração fluida entre os membros da equipe.

---

## 🚀 Fluxo de Trabalho

Adotamos o modelo **GitHub Flow**, baseado em branches de funcionalidades, pull requests e revisões.

1. Sempre crie uma branch para cada funcionalidade ou correção.
2. Nunca trabalhe diretamente na `main`.
3. Toda mudança deve ser revisada por pelo menos uma pessoa.
4. Após aprovação, faça o merge via Pull Request.

---

## 🌱 Convenção de Nomes de Branch

Use prefixos para identificar o tipo de trabalho:

| Tipo      | Prefixo         | Exemplo                       |
|-----------|------------------|-------------------------------|
| Funcionalidade | `feature/`     | `feature/login-social`        |
| Correção  | `fix/`           | `fix/erro-validacao-email`    |
| Hotfix    | `hotfix/`        | `hotfix/seguranca-token`      |
| Refatoração | `refactor/`    | `refactor/cadastro-cliente`   |

---

## ✅ Mensagens de Commit

Use mensagens **claras, concisas e padronizadas** no formato:
A melhor forma de estruturar uma mensagem de commit é no formato de cabeçalho e corpo, separados por uma linha em branco.

Linha de Assunto (Cabeçalho): Deve ser uma breve e concisa descrição da mudança.

Limitação de Caracteres: Mantenha a linha de assunto em torno de 50 a 72 caracteres. Isso facilita a leitura em várias ferramentas e interfaces.

Imperativo: Escreva a mensagem como se estivesse dando uma ordem. Use verbos no infinitivo no presente. Em vez de "adicionou", "adicionando" ou "adiciona", use "Adicionar".

Exemplo Bom: feat: Adicionar autenticação de usuário

Exemplo Ruim: Adicionando a autenticação

Capitalização: Comece a linha de assunto com uma letra maiúscula.

Sem Ponto Final: Não termine a linha de assunto com um ponto final.

Corpo da Mensagem: Forneça detalhes adicionais sobre a mudança.

Explicação: O corpo da mensagem deve explicar o o quê e porquê da mudança.

Detalhes:

Qual é o problema que essa mudança resolve?

Quais foram as considerações ou decisões tomadas?

Existem efeitos colaterais ou impactos?

Quebra de Linha: Quebre as linhas do corpo da mensagem em torno de 72 caracteres para garantir a legibilidade.

## Resumo das Boas Práticas

1ª linha: Resumo claro e conciso (máximo de 50-72 caracteres).

Vazio: Deixe uma linha em branco após a primeira linha.

Corpo: Explique o porquê e o quê da mudança, detalhando os problemas resolvidos e as decisões tomadas.

Imperativo: Use verbos no infinitivo (ex: "Adicionar", "Corrigir").

Convenção: Use uma convenção como o Conventional Commits para padronizar o histórico.

Revisão: Sempre revise a mensagem antes de dar o commit.

