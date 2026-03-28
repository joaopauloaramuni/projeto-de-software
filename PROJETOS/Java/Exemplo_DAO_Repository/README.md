# Exemplo_DAO_Repository

## 📌 Descrição

Este projeto demonstra a utilização dos padrões **DAO (Data Access
Object)** e **Repository** em Java, evidenciando a separação de
responsabilidades e boas práticas de arquitetura.

A aplicação mostra como desacoplar a lógica de acesso a dados da lógica
de negócio, tornando o código mais organizado, testável e escalável.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Java 17
-   Programação Orientada a Objetos (POO)
-   Padrões de Projeto (DAO e Repository)

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

-   `User` → Entidade de domínio
-   `UserDAO` → Interface de acesso a dados
-   `UserDAOImpl` → Implementação do DAO
-   `UserRepository` → Interface de repositório
-   `UserRepositoryImpl` → Implementação do repositório
-   `Main` → Classe principal para execução

------------------------------------------------------------------------

## 🧠 Conceito de DAO

O padrão **DAO (Data Access Object)** é responsável por **abstrair e
encapsular o acesso a fontes de dados**, como bancos de dados, APIs ou
arquivos.

### 🎯 Objetivo

Separar a lógica de persistência da lógica de negócio.

### ✅ Vantagens

-   Reduz acoplamento
-   Facilita manutenção
-   Permite troca de banco de dados sem impactar o restante do sistema
-   Melhora testabilidade

### 💡 Exemplo no projeto

A interface `UserDAO` define operações como: - salvar (`save`) - buscar
(`findById`) - atualizar (`update`) - deletar (`delete`)

A classe `UserDAOImpl` implementa essas operações.

------------------------------------------------------------------------

## 🧱 Conceito de Repository

O padrão **Repository** atua como uma camada acima do DAO, fornecendo
uma interface mais alinhada ao domínio da aplicação.

### 🎯 Objetivo

Centralizar regras de acesso a dados e orquestrar chamadas aos DAOs.

### 💡 Diferença principal

-   DAO → Focado em acesso direto ao banco
-   Repository → Focado no domínio da aplicação

------------------------------------------------------------------------

## ▶️ Como Executar

1.  Compile o projeto:

``` bash
javac Main.java
```

2.  Execute:

``` bash
java Main
```

------------------------------------------------------------------------

## 📚 Documentação e Links Úteis

-   https://docs.oracle.com/en/java/javase/17/
-   https://refactoring.guru/design-patterns/dao
-   https://martinfowler.com/eaaCatalog/repository.html

------------------------------------------------------------------------

## 📄 Licença

Este projeto está licenciado sob a licença MIT.

------------------------------------------------------------------------

## 👨‍🏫 Autor

Projeto didático para ensino de Engenharia de Software.
