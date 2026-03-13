# AGENTS.md - AI Clean Code Analyzer

## Opis aplikacji

AI Clean Code Analyzer to aplikacja webowa analizująca kod Python pod kątem zasad **Clean Code**.

Użytkownik może:

* wkleić kod Python lub przesłać plik `.py`
* otrzymać ocenę jakości kodu
* zobaczyć fragmenty wymagające poprawy
* otrzymać sugestie lepszej implementacji
* zaproponować własną poprawkę
* otrzymać feedback AI porównujący poprawkę z oryginałem

Projekt jest przeznaczony jako **projekt portfolio do CV**, dlatego priorytetem jest **prostota implementacji i czytelna architektura**.

---

# Stack technologiczny

## Backend

* **Runtime:** Python 3.10+
* **Framework:** FastAPI
* **AI Provider:** OpenAI API
* **HTTP Client:** httpx
* **Validation:** Pydantic
* **Environment variables:** python-dotenv
* **CORS:** fastapi.middleware.cors

---

## Frontend

Frontend jest napisany w **React**.

* **Framework:** React 18+
* **Build Tool:** Vite
* **Styling:** CSS
* **HTTP Client:** Fetch API
* **State Management:** React hooks (useState)

Frontend odpowiada jedynie za:

* wprowadzenie kodu
* wyświetlenie analizy
* wysłanie poprawki użytkownika

---

# Architektura aplikacji

```
clean-code-analyzer/

├── backend/
│
│   ├── app/
│   │
│   │   ├── main.py
│   │
│   │   ├── routers/
│   │   │   └── analyze.py
│   │
│   │   ├── services/
│   │   │   ├── ai_service.py
│   │   │   └── code_analysis_service.py
│   │
│   │   ├── models/
│   │   │   └── request_models.py
│   │
│   │   └── utils/
│   │       └── github_loader.py
│
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│
│   ├── src/
│   │
│   │   ├── components/
│   │   │
│   │   │   ├── CodeInput.jsx
│   │   │   ├── AnalysisResult.jsx
│   │   │   ├── FixInput.jsx
│   │   │
│   │   ├── services/
│   │   │   └── api.js
│   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│
│   ├── index.html
│   └── package.json
│
└── README.md
```

---

# Główne funkcjonalności MVP

## 1. Analiza kodu Python

Użytkownik wkleja kod Python w formularzu.

AI analizuje kod według zasad Clean Code:

* nazewnictwo zmiennych
* nazewnictwo funkcji
* długość funkcji
* złożoność
* czytelność
* Single Responsibility Principle
* duplikacja kodu

---

## 2. Ocena jakości kodu

AI zwraca ocenę:

```
1 - bardzo słaby kod
10 - idealny Clean Code
```

---

## 3. Wskazanie problematycznych fragmentów

AI zwraca listę problemów w kodzie:

* numer linii
* opis problemu
* sugestię poprawy

Przykład:

```
Line 14

Problem:
Function name is not descriptive.

Suggestion:
rename process() → process_user_data()
```

---

## 4. Sugestia poprawionej wersji kodu

AI generuje poprawioną wersję kodu zgodną z zasadami Clean Code.

---

## 5. Ocena poprawki użytkownika

Użytkownik może zaproponować własną poprawkę.

AI:

* porównuje ją z oryginalnym kodem
* ocenia jakość rozwiązania
* wyjaśnia różnice

---

# Endpointy API

## POST /api/analyze-code

Analizuje kod Python.

### Request

```json
{
  "code": "def test(): print('hello')"
}
```

### Response

```json
{
  "score": 6,
  "issues": [
    {
      "line": 1,
      "problem": "Function name is not descriptive",
      "suggestion": "Use a meaningful function name"
    }
  ],
  "improved_code": "def print_hello():\n    print('hello')"
}
```

---

# POST /api/review-user-fix

Ocenia poprawkę użytkownika.

### Request

```json
{
  "original_code": "...",
  "user_fix": "..."
}
```

### Response

```json
{
  "score": 8,
  "feedback": "Your solution improves readability but still violates SRP.",
  "comparison": "Your version is better because..."
}
```

---

# GET /api/health

Sprawdzenie statusu aplikacji.

Response:

```
{
  "status": "ok"
}
```

---

# Prompt dla AI – analiza kodu

```
You are a senior software engineer and Clean Code expert.

Analyze the following Python code according to Clean Code principles.

Focus on:

- meaningful naming
- small functions
- single responsibility principle
- readability
- avoiding duplication
- maintainability

Return JSON:

{
score: number from 1-10,
issues: [
{
line: number,
problem: "...",
suggestion: "..."
}
],
improved_code: "better version of code"
}

Code:
{code}
```

---

# Prompt dla AI – ocena poprawki

```
You are a Clean Code expert.

Compare the original code with the user's improved version.

Evaluate:

- readability
- naming
- function responsibility
- maintainability

Explain clearly why the user's version is better or worse.

Return JSON:

{
score: number,
feedback: "...",
comparison: "..."
}
```

---

# Uruchomienie aplikacji

## Wymagania

* Python 3.10+
* Node.js 18+
* OpenAI API key

---

# Backend – instalacja

```
cd backend

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

requirements.txt

```
fastapi
uvicorn
openai
python-dotenv
pydantic
httpx
```

---

# .env

```
OPENAI_API_KEY=your_api_key
```

---

# Uruchomienie backendu

```
uvicorn app.main:app --reload
```

API dostępne pod:

```
http://localhost:8000
```

Dokumentacja API:

```
http://localhost:8000/docs
```

---

# Frontend – instalacja

```
cd frontend

npm install
npm run dev
```

Frontend dostępny pod:

```
http://localhost:5173
```

---

# Komunikacja frontend → backend

Frontend wysyła zapytania do API:

```
POST http://localhost:8000/api/analyze-code
POST http://localhost:8000/api/review-user-fix
```

---

# Przyszłe rozszerzenia

Możliwe rozwinięcia projektu:

* analiza repozytorium GitHub
* upload plików `.py`
* analiza wielu plików jednocześnie
* AST analysis Python
* integracja z GitHub Pull Requests
* ranking jakości repozytorium

---

# Uwagi dla agentów AI

Priorytety projektu:

1. Prostota implementacji
2. Czytelność kodu
3. Minimalna liczba endpointów
4. Niski koszt zapytań do API

Projekt nie jest systemem produkcyjnym — jest to **projekt demonstracyjny do CV**.

Kod powinien być:

* prosty
* dobrze opisany
* łatwy do zrozumienia
