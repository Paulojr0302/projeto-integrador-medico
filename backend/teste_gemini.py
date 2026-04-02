import google.generativeai as genai

# COLE A SUA CHAVE AQUI DENTRO DAS ASPAS:
CHAVE_API_GEMINI = "AIzaSyB8kNG7BAeLFsQWl_YU7_Cf03E76pzfhw0" 
genai.configure(api_key=CHAVE_API_GEMINI)

print("Buscando modelos disponíveis para a sua chave...")

try:
    # Pergunta diretamente ao Google quais modelos você tem permissão para usar
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Modelo liberado: {m.name}")
except Exception as e:
    print(f"Erro ao buscar modelos: {e}")