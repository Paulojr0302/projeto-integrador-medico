#  Assistente Médico Inteligente (Gerador de Prontuário SOAP)

> **Projeto Integrador - Engenharia da Computação**
> Sistema web de IA para transcrição e estruturação automática de consultas médicas.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google%20gemini&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)

## 📌 Sobre o Projeto
O preenchimento manual de Prontuários Eletrônicos do Paciente (PEP) consome um tempo significativo dos profissionais de saúde, muitas vezes comprometendo o contato visual e a atenção direta ao paciente durante a consulta. 

Este projeto visa solucionar esse problema através de uma arquitetura "Ambient Clinical Intelligence". O sistema capta o áudio do diálogo entre médico e paciente em tempo real, transcreve a conversa e utiliza Inteligência Artificial Generativa para estruturar os dados clínicos automaticamente no padrão **SOAP** (Subjetivo, Objetivo, Avaliação e Plano).

### ✨ Funcionalidades
- **Captura de Áudio no Navegador:** Gravação via `Web Audio API` sem necessidade de instalação de aplicativos de terceiros.
- **Processamento Edge/Local:** Transcrição de áudio assíncrona utilizando o modelo **Whisper** (base), garantindo privacidade na etapa de *Speech-to-Text*.
- **Estruturação por LLM:** Integração inteligente com a API do **Google Gemini** via *Prompt Engineering* especializado em contextos médicos.
- **Human-in-the-Loop:** Interface interativa que permite ao médico editar, revisar e validar o prontuário gerado antes de copiá-lo para o sistema do hospital.

---

## 🛠️ Tecnologias Utilizadas

**Frontend:**
- HTML5, CSS3 (Variáveis nativas e design responsivo)
- JavaScript Vanilla (Web Audio API, Fetch API)

**Backend:**
- Python 3.x
- [FastAPI](https://fastapi.tiangolo.com/) & Uvicorn (Roteamento assíncrono e servidor ASGI)
- `python-multipart` (Recebimento de arquivos de áudio)

**Inteligência Artificial:**
- [OpenAI Whisper](https://github.com/openai/whisper) (Modelo `base` para STT)
- [Google Generative AI](https://aistudio.google.com/) (Modelo `gemini-2.5-flash` para estruturação SOAP)

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos
1. **Python 3.8+** instalado na máquina.
2. **FFmpeg** instalado e configurado nas variáveis de ambiente do Windows/Linux (Necessário para o Whisper processar os áudios).
3. Uma chave de API válida do **Google AI Studio** (Gemini).

### Passo a Passo da Instalação

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Paulojr0302/projeto-integrador-medico.git](https://github.com/Paulojr0302/projeto-integrador-medico.git)
   cd projeto-integrador-medico
