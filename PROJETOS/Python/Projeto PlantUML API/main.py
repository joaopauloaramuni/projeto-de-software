from plantuml_client import PlantUMLClient
import os

def read_plantuml_code(file_name):
    """Lê o conteúdo do arquivo de código PlantUML."""
    try:
        with open(file_name, "r") as file:
            return file.read()
    except Exception as e:
        print(f"Erro ao ler o arquivo '{file_name}': {e}")
        return ""

def generate_use_case_diagram(client):
    """Gera um diagrama de casos de uso."""
    file_path = os.path.join("plantuml_code", "use_case_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "use_case_diagram.png")


def generate_class_diagram(client):
    """Gera um diagrama de classes."""
    file_path = os.path.join("plantuml_code", "class_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "class_diagram.png")


def generate_sequence_diagram(client):
    """Gera um diagrama de sequência."""
    file_path = os.path.join("plantuml_code", "sequence_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "sequence_diagram.png")


def generate_communication_diagram(client):
    """Gera um diagrama de comunicação."""
    file_path = os.path.join("plantuml_code", "communication_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "communication_diagram.png")


def generate_state_diagram(client):
    """Gera um diagrama de estados."""
    file_path = os.path.join("plantuml_code", "state_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "state_diagram.png")
    

def generate_component_diagram(client):
    """Gera um diagrama de componentes."""
    file_path = os.path.join("plantuml_code", "component_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "component_diagram.png")


def generate_deployment_diagram(client):
    """Gera um diagrama de implantação."""
    file_path = os.path.join("plantuml_code", "deployment_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "deployment_diagram.png")


def generate_package_diagram(client):
    """Gera um diagrama de pacotes."""
    file_path = os.path.join("plantuml_code", "package_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "package_diagram.png")


def generate_activity_diagram(client):
    """Gera um diagrama de atividades."""
    file_path = os.path.join("plantuml_code", "activity_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "activity_diagram.png")


def generate_entity_relationship_diagram(client):
    """Gera um diagrama de entidade-relacionamento."""
    file_path = os.path.join("plantuml_code", "entity_relationship_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "entity_relationship_diagram.png")


def generate_json_diagram(client):
    """Gera um diagrama baseado em estrutura JSON."""
    file_path = os.path.join("plantuml_code", "json_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "json_diagram.png")


def generate_wireframe_diagram(client):
    """Gera um diagrama de wireframe."""
    file_path = os.path.join("plantuml_code", "wireframe_diagram.puml")
    plantuml_code = read_plantuml_code(file_path)
    save_diagram(client, plantuml_code, "wireframe_diagram.png")


def save_diagram(client, plantuml_code, output_filename):
    """Gera e salva o diagrama no formato PNG."""
    try:
        # Cria a pasta 'plantuml_diagrams' caso ela não exista
        os.makedirs("plantuml_diagrams", exist_ok=True)
        
        # Define o caminho completo para salvar o arquivo
        output_path = os.path.join("plantuml_diagrams", output_filename)
        
        # Obtém o conteúdo do diagrama
        png_content = client.fetch_diagram(plantuml_code, "png")
        with open(output_path, "wb") as f:
            f.write(png_content)
        print(f"\nDiagrama salvo como '{output_filename}'")
    except Exception as e:
        print(f"Erro ao gerar o diagrama '{output_filename}': {e}")


def main():
    client = PlantUMLClient()

    print("*" * 150)
    print("Gerando diagramas...")
    print("*" * 150)
    generate_use_case_diagram(client)
    print("*" * 150)
    generate_class_diagram(client)
    print("*" * 150)
    generate_sequence_diagram(client)
    print("*" * 150)
    generate_communication_diagram(client)
    print("*" * 150)
    generate_state_diagram(client)
    print("*" * 150)
    generate_component_diagram(client)
    print("*" * 150)
    generate_deployment_diagram(client)
    print("*" * 150)
    generate_package_diagram(client)
    print("*" * 150)
    generate_activity_diagram(client)
    print("*" * 150)
    generate_entity_relationship_diagram(client)
    print("*" * 150)
    generate_json_diagram(client)
    print("*" * 150)
    generate_wireframe_diagram(client)
    print("*" * 150)
    print("Todos os diagramas foram gerados com sucesso.")
    print("*" * 150)


if __name__ == "__main__":
    main()
