# 🤖 WhatsApp AI Assistant

Serviço backend para automação de conversas no WhatsApp utilizando Google Gemini como motor de inteligência artificial.

Este projeto integra a WhatsApp Cloud API com um webhook em FastAPI para processar mensagens recebidas, gerar respostas com IA e enviá-las automaticamente ao usuário em tempo real.

---

## 📌 Visão Geral

O sistema recebe eventos via webhook da WhatsApp Cloud API, extrai a mensagem do usuário, envia o conteúdo para um modelo de linguagem (Google Gemini) e retorna a resposta gerada através da Meta Graph API.

A arquitetura foi pensada para ser simples, extensível e pronta para evolução.

Possíveis aplicações:

- 💬 Automação de atendimento
- 🧠 Assistente virtual para empresas
- 🎯 Qualificação automática de leads
- 🏢 Ferramentas internas conversacionais
- 🔄 Interfaces baseadas em chat

---

## 🏗 Arquitetura

```
Usuário (WhatsApp)
        ▼
WhatsApp Cloud API (Meta)
        ▼
Webhook FastAPI (Render)
        ▼
Google Gemini API
        ▼
Resposta enviada via Meta Graph API
```

O sistema é orientado a eventos e opera exclusivamente via webhook.

---

## 🛠 Stack Tecnológica

- 🐍 Python 3.10+
- ⚡ FastAPI
- 📲 WhatsApp Cloud API (Meta Graph API v19+)
- 🧠 Google Gemini API
- 🚀 Uvicorn
- ☁️ Render (deploy em nuvem)

---

## 📂 Estrutura do Projeto

```
.
├── main.py          # Webhook + integração com WhatsApp
├── llm.py           # Camada de integração com Gemini
├── requirements.txt
└── README.md
```

---

## 🔐 Variáveis de Ambiente

Configure via `.env` (ambiente local) ou diretamente no provedor de nuvem:

```
WHATSAPP_TOKEN=seu_token_permanente_meta
VERIFY_TOKEN=seu_token_de_verificacao
PHONE_NUMBER_ID=seu_phone_number_id
GEMINI_API_KEY=sua_chave_gemini
```

### Descrição

- 🔑 `WHATSAPP_TOKEN`: Token permanente gerado via Usuário do Sistema no Meta Business
- 🔎 `VERIFY_TOKEN`: Token definido para validação do webhook
- 📞 `PHONE_NUMBER_ID`: Disponível no painel da WhatsApp Cloud API
- 🧠 `GEMINI_API_KEY`: Gerado no Google AI Studio

---

## ▶ Execução Local

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie o servidor:

```bash
uvicorn main:app --reload
```

Endpoints:

```
GET  /webhook   → Verificação
POST /webhook   → Recebimento de mensagens
```

---

## ☁ Deploy (Exemplo com Render)

**Build Command**
```
pip install -r requirements.txt
```

**Start Command**
```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Configure as variáveis de ambiente no painel do serviço.

---

## 📲 Configuração da WhatsApp Cloud API

1. Criar App na Meta
2. Adicionar produto WhatsApp
3. Conectar conta Business
4. Configurar URL do webhook
5. Gerar token permanente via Usuário do Sistema
6. Conceder permissões:
   - `whatsapp_business_messaging`
   - `whatsapp_business_management`

---

## ⚙ Observações Operacionais

- ⏱ Respostas livres são permitidas dentro da janela de 24h após a última mensagem do usuário.
- 📄 Fora dessa janela, é necessário utilizar templates aprovados.
- 🔔 A API funciona via webhook; não há consulta de histórico.
- 💤 Em planos gratuitos de hospedagem pode haver cold start.

---

## 📈 Possíveis Evoluções

- 🗄 Persistência em banco de dados (PostgreSQL)
- 🧩 Gerenciamento de contexto de conversa
- 👥 Suporte multi-tenant
- 📊 Observabilidade (logs estruturados e métricas)
- 🔄 Processamento assíncrono com fila (Redis / Celery)
- 📦 Containerização com Docker
- 🔁 Pipeline de CI/CD

---

## 🔒 Segurança

- 🔐 Tokens armazenados como variáveis de ambiente
- ✔ Verificação de webhook via token
- 🚫 Nenhuma persistência de dados sensíveis por padrão
- 🏢 Token permanente gerado via Usuário do Sistema (produção)

---

## 📌 Status

Base funcional pronta para produção e evolução arquitetural.

---

## 👨‍💻 Autor

Lussandro  
Projeto backend de integração entre WhatsApp Cloud API e modelos de linguagem (LLM).
