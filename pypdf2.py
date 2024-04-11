import os
from PyPDF2 import PdfReader

def extrair_texto_e_metadados(pdf_path):
    texto = ''
    metadados = {}

    with open(pdf_path, 'rb') as pdf_file:
        reader = PdfReader(pdf_file)
        
        # Extrair texto
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            texto += page.extract_text()

        # Extrair metadados
        metadados = reader.metadata

    return texto, metadados

def salvar_em_txt(texto, txt_path):
    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(texto)

def excluir_pdf(pdf_path):
    os.remove(pdf_path)

def main():
    # Caminho do PDF
    pdf_path = 'teste.pdf'
    
    # Extrair texto e metadados
    texto, metadados = extrair_texto_e_metadados(pdf_path)
    
    # Imprimir texto e metadados
    print('Texto extraído do PDF:')
    print(texto)
    print('\nMetadados do PDF:')
    print(metadados)
    
    # Salvar o texto extraído em um arquivo de texto
    txt_path = 'texto_extraido.txt'
    salvar_em_txt(texto, txt_path)
    print(f'\nTexto extraído salvo em "{txt_path}"')
    
    # Excluir o arquivo PDF
    excluir_pdf(pdf_path)
    print(f'\nPDF "{pdf_path}" excluído com sucesso.')

if __name__ == "__main__":
    main()
