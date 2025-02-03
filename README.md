# RAG-Chat: Retrieval-Augmented Chatbot

RAG-Chat is a Flask-based chatbot application that leverages Retrieval-Augmented Generation (RAG) to answer user queries by retrieving relevant documents and generating informed responses. The system includes multiple components for document loading, text extraction, text normalization, embedding generation, and retrieval.

## Features

- **Document Loader:** Loads text documents from the designated folder.
- **PDF Processing:** Extracts and cleans PDF elements.
- **Text Chunking & Normalization:** Splits and normalizes text for effective processing.
- **Embeddings Generation:** Integrates with Jina AI to generate text embeddings.
- **Document Retrieval:** Uses cosine similarity to fetch the most relevant documents.
- **LLM Integration:** Generates conversational responses with context using an external API.
- **API Endpoint:** Provides RESTful interface for chatbot communication.

## Project Structure

- **data/**
    - `loaders.py` – Loads text files from the `data/documents` directory.
    - Document files under `data/documents/` containing sample texts.

- **utils/**
    - `text_chunker.py` – Chunking documents into context-aware pieces.
    - `text_normalizer.py` – Normalizing text elements.
    - `text_extractor.py` – Extracting elements from PDFs.
    - `text_cleaner.py` – Cleaning and filtering text elements.
    - `embedder.py` – Generating embeddings via Jina AI API.
    - `retriever.py` – Retrieves documents based on query relevance.
    - `generator.py` – Integrates with Codestral LLM for response generation.

- **routes/**
    - `api.py` – Defines API endpoints for interacting with the chatbot.

- **tests/**
    - Contains unit tests for various modules to ensure functionality.

- **app.py**
    - Entry point to create and run the Flask application.

- **README.md**
    - This file.

- **requirements.txt**
    - List of Python dependencies for the project.

## Setup and Installation

1. **Clone the Repository:**
     ```bash
     git clone https://github.com/yourusername/RAG-chat.git
     cd RAG-chat
     ```

2. **Create and Activate Virtual Environment:**
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use: venv\Scripts\activate
     ```

3. **Install Dependencies:**
     ```bash
     pip install -r requirements.txt
     ```

4. **Environment Variables:**
     Create a `.env` file in the project root with the required keys:
     ```dotenv
     API_KEY=your_codestral_api_key
     JINA_API_KEY=your_jina_api_key
     ```

## Running the Application

Start the Flask server by running:
```bash
python app.py
```
The application will be accessible at [http://localhost:5000](http://localhost:5000).

## API Usage

- **Chat Endpoint:**
    - **URL:** `/api/chat`
    - **Method:** POST
    - **Payload:**
        ```json
        {
            "message": "your query here",
            "session_id": "unique-session-id"
        }
        ```
    - **Response:**
        ```json
        {
            "response": "chatbot generated response"
        }
        ```

## Running Tests

Unit tests are provided to verify the functionality. To run tests, use:
```bash
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please fork the repository and submit your pull requests.

## License

This project is licensed under the terms specified in the LICENSE file.

## Contact

For any questions, please open an issue in the repository.
