# Projeto PlantUML API

Este projeto foi desenvolvido para facilitar a interação com a API do PlantUML, permitindo a geração automática de diagramas a partir de código UML. O objetivo é proporcionar uma interface simples para codificação, compactação e requisição de diagramas diretamente a partir de arquivos `.puml`.

## Sobre o PlantUML

O PlantUML é uma ferramenta open-source criada em 2009 com o propósito de gerar diagramas UML de forma programática, utilizando uma linguagem de marcação simples. Ele é amplamente utilizado para diagramas de classes, sequências, casos de uso, entre outros, e é suportado por várias ferramentas de desenvolvimento. O projeto PlantUML utiliza a biblioteca Graphviz para renderização gráfica, sendo uma solução poderosa e flexível para documentação e modelagem de software.

---

## Capturas de Tela

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/activity_diagram.png" alt="activity_diagram"/> |
|:---------------------:|
| activity_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/class_diagram.png" alt="class_diagram"/> |
|:---------------------:|
| class_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/communication_diagram.png" alt="communication_diagram"/> |
|:---------------------:|
| communication_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/component_diagram.png" alt="component_diagram"/> |
|:---------------------:|
| component_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/deployment_diagram.png" alt="deployment_diagram"/> |
|:---------------------:|
| deployment_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/entity_relationship_diagram.png" alt="entity_relationship_diagram"/> |
|:---------------------:|
| entity_relationship_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/json_diagram.png" alt="json_diagram"/> |
|:---------------------:|
| json_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/package_diagram.png" alt="package_diagram"/> |
|:---------------------:|
| package_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/sequence_diagram.png" alt="sequence_diagram"/> |
|:---------------------:|
| sequence_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/state_diagram.png" alt="state_diagram"/> |
|:---------------------:|
| state_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/use_case_diagram.png" alt="use_case_diagram"/> |
|:---------------------:|
| use_case_diagram |

| <img src="https://joaopauloaramuni.github.io/python-imgs/PlantUML_API/plantuml_diagrams/wireframe_diagram.png" alt="wireframe_diagram"/> |
|:---------------------:|
| wireframe_diagram |

---

## Funções

### Funções Implementadas

1. **Compressão de Código UML** (`_compress_plantuml_code`)
   - Compacta o código PlantUML utilizando o algoritmo Deflate, removendo cabeçalhos e rodapés para compatibilidade.

2. **Codificação em Formato Customizado** (`_encode_to_plantuml_format`)
   - Converte os bytes compactados para um formato customizado utilizado pelo PlantUML (6-bit encoding).

3. **Compactação e Codificação** (`encode_plantuml`)
   - Compacta o código UML e o converte para o formato esperado pela API do PlantUML.

4. **Geração de URLs** (`get_diagram_url`)
   - Gera URLs de diagramas para acesso direto em formato PNG, SVG ou outros suportados.

5. **Requisição HTTP** (`fetch_diagram`)
   - Faz requisições HTTP para a API do PlantUML e obtém o conteúdo binário do diagrama gerado.

6. **Leitura de Arquivos** (`read_plantuml_code`)
   - Lê o conteúdo de arquivos `.puml` para serem processados e transformados em diagramas.

7. **Geração e Salvamento de Diagramas** (`save_diagram`)
   - Gera e salva os diagramas em formato PNG a partir do código UML lido de arquivos.

8. **Geração de Tipos Específicos de Diagramas**
   - Diagramas específicos são gerados pelas funções:
     - `generate_use_case_diagram` (Diagrama de Casos de Uso)
     - `generate_class_diagram` (Diagrama de Classes)
     - `generate_sequence_diagram` (Diagrama de Sequência)
     - `generate_communication_diagram` (Diagrama de Comunicação)
     - `generate_state_diagram` (Diagrama de Estados)
     - `generate_component_diagram` (Diagrama de Componentes)
     - `generate_deployment_diagram` (Diagrama de Implantação)
     - `generate_package_diagram` (Diagrama de Pacotes)
     - `generate_activity_diagram` (Diagrama de Atividades)
     - `generate_entity_relationship_diagram` (Diagrama de Entidade-Relacionamento)
     - `generate_json_diagram` (Diagrama Baseado em JSON)
     - `generate_wireframe_diagram` (Diagrama de Wireframe)

Essas funções permitem a geração de diversos diagramas UML e diagramas específicos baseados em código PlantUML.

---

## Links para Arquivos `.puml`

- [activity_diagram.puml](plantuml_code/activity_diagram.puml)
- [class_diagram.puml](plantuml_code/class_diagram.puml)
- [communication_diagram.puml](plantuml_code/communication_diagram.puml)
- [component_diagram.puml](plantuml_code/component_diagram.puml)
- [deployment_diagram.puml](plantuml_code/deployment_diagram.puml)
- [entity_relationship_diagram.puml](plantuml_code/entity_relationship_diagram.puml)
- [json_diagram.puml](plantuml_code/json_diagram.puml)
- [package_diagram.puml](plantuml_code/package_diagram.puml)
- [sequence_diagram.puml](plantuml_code/sequence_diagram.puml)
- [state_diagram.puml](plantuml_code/state_diagram.puml)
- [use_case_diagram.puml](plantuml_code/use_case_diagram.puml)
- [wireframe_diagram.puml](plantuml_code/wireframe_diagram.puml)

---

## Documentação Adicional

- [PlantUML Language Reference Guide](plantuml_language_reference_guide_en/PlantUML_Language_Reference_Guide_en.pdf)

---

## Dependências

As dependências do projeto estão listadas no arquivo `requirements.txt`.

### Instalação das Dependências

1. Crie um ambiente virtual:
   ```bash
   python -m venv .venv
   ```

2. Ative o ambiente virtual:
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/MacOS**:
     ```bash
     source .venv/bin/activate
     ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

---

## Links Úteis

- [PlantUML Site Oficial](https://plantuml.com/)
- [PlantUML Download](https://plantuml.com/download)
- [PlantUML API](https://www.plantuml.com/plantuml/uml)
- [PyPI - Requests](https://pypi.org/project/requests/)
---

## Licença

Este projeto está sob a Licença MIT.
