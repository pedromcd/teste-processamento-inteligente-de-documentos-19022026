import pdfplumber
import re
import json
from pathlib import Path


class EnergyInvoiceExtractor:
    """
    Classe responsável por:
    1. Ler o PDF da fatura
    2. Extrair o texto completo
    3. Aplicar expressões regulares para capturar as informações solicitadas
    """

    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.text = self._extract_text()

    def _extract_text(self) -> str:
        """
        Extrai todo o texto do PDF utilizando pdfplumber.
        Retorna o texto concatenado de todas as páginas.
        """

        # Verifica se o arquivo existe antes de tentar abrir
        if not Path(self.pdf_path).exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.pdf_path}")

        full_text = ""

        # Abre o PDF e percorre todas as páginas
        with pdfplumber.open(self.pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"

        return full_text

    def _search(self, pattern, flags=0):
        """
        Função auxiliar para evitar repetição de código.
        Recebe um padrão regex e retorna o primeiro grupo encontrado.
        """
        match = re.search(pattern, self.text, flags)
        return match.group(1).strip() if match else None

    def extract_data(self) -> dict:
        """
        Extrai todas as informações solicitadas no teste
        e retorna um dicionário estruturado.
        """

        data = {}

        # ==============================
        # DADOS DO TITULAR
        # ==============================

        # Captura nome do titular (linha antes de "CPF")
        data["Titular"] = self._search(r"\n([A-Z\s]+)\nCPF")

        # Captura CPF
        data["Documento"] = self._search(r"CPF[:\s]+([\d\.\-]+)")

        # ==============================
        # ENDEREÇO
        # ==============================

        # Captura bloco de endereço após o nome
        endereco_match = re.search(
            r"\n[A-Z\s]+\n(.*?)\n\d{5}-?\d{3}",
            self.text,
            re.DOTALL
        )

        data["Endereço"] = (
            endereco_match.group(1).replace("\n", ", ")
            if endereco_match else None
        )

        # ==============================
        # INFORMAÇÕES DA INSTALAÇÃO
        # ==============================

        # Classificação da instalação (ex: Convencional B1 Residencial)
        data["Classificação da Instalação"] = self._search(
            r"CLASSIFICAÇÃO:\s*(.+)"
        )

        # Número da instalação (pode variar conforme concessionária)
        data["Número da Instalação"] = (
            self._search(r"Nº DA INSTALAÇÃO\s+(\d+)")
            or self._search(r"Conta Contrato N°\s*(\d+)")
        )

        # ==============================
        # VALORES PRINCIPAIS
        # ==============================

        # Valor total a pagar
        data["Valor a Pagar (R$)"] = self._search(
            r"Total a Pagar.*?([\d\.,]+)",
            flags=re.DOTALL
        )

        # Data de vencimento
        data["Data de Vencimento"] = self._search(
            r"Data de Vencimento\s+(\d{2}/\d{2}/\d{4})"
        )

        # Mês de referência (ex: OUT/23)
        data["Mês de Referência"] = self._search(
            r"\b([A-Z]{3}/\d{2})\b"
        )

        # ==============================
        # TARIFAS E CONSUMO
        # ==============================

        # Consumo total em kWh
        data["Consumo kWh"] = (
            self._search(r"Consumo.*?([\d\.]+)\s*kWh", flags=re.DOTALL)
        )

        # Saldo acumulado de energia (kWh)
        data["Saldo acumulado kWh"] = self._search(
            r"Saldo em Energia.*?([\d\.,]+)\s*kWh"
        )

        # ==============================
        # ENERGIAS COMPENSADAS
        # ==============================

        # Busca valores negativos (indicando compensação)
        compensadas = re.findall(r"([\d\.,]+)-", self.text)

        if compensadas:
            total_compensado = sum(
                float(valor.replace(".", "").replace(",", "."))
                for valor in compensadas
            )
            data["Somatório Energias Compensadas (R$)"] = round(total_compensado, 2)
        else:
            data["Somatório Energias Compensadas (R$)"] = None

        # ==============================
        # CONTRIBUIÇÕES E IMPOSTOS
        # ==============================

        # Contribuição de Iluminação Pública
        data["Contribuição Iluminação Pública"] = self._search(
            r"Contrib.*?IP.*?\s([\d\.,]+)"
        )

        # Alíquotas
        data["Alíquota ICMS (%)"] = self._search(r"Aliq\.\s*ICMS\s*([\d,]+)")
        data["Alíquota PIS (%)"] = self._search(r"PIS\s*([\d,]+)%")
        data["Alíquota COFINS (%)"] = self._search(r"COFINS\s*([\d,]+)%")

        # ==============================
        # LINHA DIGITÁVEL
        # ==============================

        linha_digitavel = re.search(
            r"(\d{10,}\s\d{10,}\s\d{10,}\s\d{10,})",
            self.text
        )

        data["Linha Digitável"] = (
            linha_digitavel.group(1) if linha_digitavel else None
        )

        return data


def print_formatted(data: dict, pdf_path: str):
    """
    Exibe os dados extraídos de forma organizada no terminal,
    indicando qual arquivo foi processado.
    """

    print("\n" + "=" * 60)
    print("PROCESSAMENTO DE FATURA DE ENERGIA")
    print("=" * 60)
    print(f"Arquivo analisado: {pdf_path}")
    print("=" * 60)

    for key, value in data.items():
        print(f"{key}: {value}")

    print("=" * 60 + "\n")



def main():
    """
    Função principal do programa.
    Define qual PDF será analisado e executa a extração.
    """

    pdf_path = "fatura_cpfl.pdf"  # Altere para testar outros PDFs

    extractor = EnergyInvoiceExtractor(pdf_path)
    data = extractor.extract_data()

    # Impressão formatada no terminal, comente a linha abaixo se não quiser visualizar no terminal:
    print_formatted(data, pdf_path)

    # Caso não queira visualizar como JSON, comente a linha abaixo:
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
