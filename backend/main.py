import os
import shutil
import whisper
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

# --- 1. CONFIGURAÇÃO DA API ---
CHAVE_API_GEMINI = "AIzaSyB8kNG7BAeLFsQWl_YU7_Cf03E76pzfhw0" 
genai.configure(api_key=CHAVE_API_GEMINI)

# --- 2. FUNÇÃO DE CONEXÃO INTELIGENTE COM O GEMINI ---
def carregar_modelo_gemini():
    modelos_para_testar = [
        'gemini-2.5-flash',
        'models/gemini-2.5-flash',
        'gemini-flash-latest'
    ]
    
    print("Testando conexão com o Google Gemini...")
    for nome in modelos_para_testar:
        try:
            modelo = genai.GenerativeModel(nome)
            resposta_teste = modelo.generate_content("Responda apenas 'OK'.")
            if resposta_teste.text:
                print(f"✅ Sucesso! Conectado ao modelo: {nome}")
                return modelo
        except Exception as e:
            continue
    return genai.GenerativeModel('gemini-2.5-flash')

model_gemini = carregar_modelo_gemini()

# --- 3. CONFIGURAÇÃO DO SERVIDOR ---
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print("Carregando modelo Whisper... Aguarde.")
modelo_whisper = whisper.load_model("base")
print("✅ Whisper carregado com sucesso!")

# --- 4. ROTA PRINCIPAL ---
@app.post("/transcrever/")
async def processar_consulta(file: UploadFile = File(...)):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    texto_transcrito = ""
    try:
        print(f"Transcrevendo áudio: {file.filename}...")
        result = modelo_whisper.transcribe(file_location, fp16=False, language="pt")
        texto_transcrito = result["text"]
        print(f"Texto extraído: {texto_transcrito}")

        print("Enviando para o Gemini estruturar...")
        # --- AQUI ESTÁ A MÁGICA NOVA ---
        prompt = f"""
        Você é um assistente médico de IA. A transcrição abaixo é um DIÁLOGO de uma consulta real entre um Médico e um Paciente.
        O texto pode não identificar quem está falando, mas você deve inferir pelo contexto da conversa.
        Extraia as informações desse diálogo e monte um prontuário impecável no formato SOAP.
        
        S (Subjetivo): Queixas do paciente, sintomas relatados por ele e histórico.
        O (Objetivo): Achados do médico, exames físicos mencionados ou sinais vitais (ex: pressão, temperatura).
        A (Avaliação): Hipótese diagnóstica ou conclusão clínica feita pelo médico.
        P (Plano): Conduta, remédios prescritos, orientações e exames solicitados.

        Transcrição do diálogo da consulta:
        "{texto_transcrito}"
        """
        
        response = model_gemini.generate_content(prompt)
        prontuario_final = response.text
        print("✅ Prontuário gerado com sucesso!")

    except Exception as e:
        print(f"❌ Erro detectado: {e}")
        prontuario_final = f"Erro no processamento da IA: {str(e)}"
        if not texto_transcrito:
            texto_transcrito = "Erro na transcrição do áudio."
        
    finally:
        if os.path.exists(file_location):
            os.remove(file_location)
    
    return {
        "mensagem": "Processamento concluído",
        "texto_original": texto_transcrito,
        "prontuario": prontuario_final
    }