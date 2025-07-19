import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
import xml.etree.ElementTree as ET


def remove_namespace(xml_root):
    for elem in xml_root.iter():
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

def parse_nfe(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    remove_namespace(root)

    emitente_cnpj = root.findtext(".//emit/CNPJ")
    emitente_razao = root.findtext(".//emit/xNome")
    destinatario_cnpj = root.findtext(".//dest/CNPJ")
    destinatario_razao = root.findtext(".//dest/xNome")
    data_emissao = root.findtext(".//ide/dhEmi")
    data_saida = root.findtext(".//ide/dhSaiEnt")

    produtos = []
    for prod in root.findall(".//det"):
        nome = prod.findtext(".//prod/xProd")
        codigo = prod.findtext(".//prod/cProd")
        qtde = prod.findtext(".//prod/qCom")
        unitario = prod.findtext(".//prod/vUnCom")
        total = prod.findtext(".//prod/vProd")

        produtos.append({
            "Emitente CNPJ": emitente_cnpj,
            "Emitente Razão": emitente_razao,
            "Destinatário CNPJ": destinatario_cnpj,
            "Destinatário Razão": destinatario_razao,
            "Data Emissão": data_emissao,
            "Data Saída": data_saida,
            "Produto": nome,
            "Código": codigo,
            "Quantidade": float(qtde),
            "Valor Unitário": float(unitario),
            "Valor Total": float(total)
        })

    return produtos

def escolher_pasta():
    pasta_xml = filedialog.askdirectory(title="Selecione a pasta com XMLs")
    if not pasta_xml:
        return

    relatorio_final = []

    for nome_arquivo in os.listdir(pasta_xml):
        if nome_arquivo.endswith(".xml"):
            caminho_arquivo = os.path.join(pasta_xml, nome_arquivo)
            try:
                dados = parse_nfe(caminho_arquivo)
                relatorio_final.extend(dados)
                print(f"[OK] {nome_arquivo}")
            except Exception as e:
                print(f"[ERRO] {nome_arquivo}: {e}")

    if relatorio_final:
        df = pd.DataFrame(relatorio_final)

        salvar_como = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                                   filetypes=[("Excel", "*.xlsx")],
                                                   title="Salvar relatório como")
        if salvar_como:
            df.to_excel(salvar_como, index=False, engine="openpyxl")
            messagebox.showinfo("Sucesso", f"Relatório salvo com sucesso:\n{salvar_como}")
    else:
        messagebox.showwarning("Aviso", "Nenhuma nota processada.")

# Interface
janela = tk.Tk()
janela.title("Exportador de NF-e")
janela.geometry("300x150")

btn = tk.Button(janela, text="Selecionar pasta de XMLs", command=escolher_pasta)
btn.pack(pady=50)

janela.mainloop()