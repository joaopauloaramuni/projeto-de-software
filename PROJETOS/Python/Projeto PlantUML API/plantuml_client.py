import zlib
import requests
import base64

class PlantUMLClient:
    
    # Alfabetos de codificação
    BASE64_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    PLANTUML_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"


    def __init__(self, server_url="http://www.plantuml.com/plantuml/"):
        """
        Inicializa o cliente para a API do PlantUML.
        :param server_url: URL base do servidor do PlantUML.
        """
        self.server_url = server_url.rstrip("/") + "/"


    @staticmethod
    def _compress_plantuml_code(plantuml_code: str) -> bytes:
        """
        Compacta o código PlantUML usando o algoritmo Deflate.
        Remove cabeçalhos e rodapés zlib para compatibilidade com a API.
        
        :param plantuml_code: Código do PlantUML.
        :return: Bytes compactados (sem cabeçalhos e rodapés zlib).
        """
        compressed = zlib.compress(plantuml_code.encode("utf-8"))
        return compressed[2:-4]  # Remove cabeçalhos e rodapés


    @staticmethod
    def _encode_to_plantuml_format(data: bytes) -> str:
        """
        Codifica os bytes compactados para o formato PlantUML (6-bit encoding),
        usando base64 com uma tabela customizada.
        
        :param data: Bytes compactados.
        :return: String codificada no formato PlantUML.
        """
        # Codifica os dados em Base64
        b64_encoded = base64.b64encode(data).decode("utf-8")
        # Substitui caracteres do alfabeto Base64 pelo esquema personalizado do PlantUML
        translation_table = str.maketrans(
            PlantUMLClient.BASE64_ALPHABET,
            PlantUMLClient.PLANTUML_ALPHABET
        )
        return b64_encoded.translate(translation_table)


    def encode_plantuml(self, plantuml_code: str) -> str:
        """
        Compacta e codifica o código PlantUML para o formato esperado pela API.
        
        :param plantuml_code: Código do PlantUML.
        :return: String codificada.
        """
        compressed_data = self._compress_plantuml_code(plantuml_code)
        return self._encode_to_plantuml_format(compressed_data)


    def get_diagram_url(self, plantuml_code: str, diagram_type: str = "png") -> str:
        """
        Gera a URL do diagrama no formato especificado.
        :param plantuml_code: Código do PlantUML.
        :param diagram_type: Formato do diagrama (svg, png, etc.).
        :return: URL do diagrama.
        """
        encoded_code = self.encode_plantuml(plantuml_code)
        url = f"{self.server_url}{diagram_type}/{encoded_code}"
        print(f"URL gerada ({len(url)} caracteres):\n\n{url}")
        return url


    def fetch_diagram(self, plantuml_code: str, diagram_type: str = "png") -> bytes:
        """
        Busca o diagrama gerado a partir do código PlantUML.
        
        :param plantuml_code: Código do PlantUML.
        :param diagram_type: Formato do diagrama (svg, png, etc.).
        :return: Conteúdo binário do diagrama.
        """
        url = self.get_diagram_url(plantuml_code, diagram_type)
        response = requests.get(url)
        response.raise_for_status()
        return response.content
