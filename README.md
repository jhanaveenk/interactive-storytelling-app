# Interactive Storytelling Application

This is a simple interactive storytelling application using OpenAI's GPT-3/GPT-4, FastAPI, and vanilla JavaScript.

## Setup

### Backend

1. Navigate to the `backend` directory.
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```
3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set your OpenAI API key in an environment variable:
    ```bash
    set OPENAI_API_KEY=your-openai-api-key
    ```
5. Run the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```

### Frontend

1. Open `frontend/index.html` in your browser.

## Usage

1. Enter your input in the text field and click "Continue Story" to generate the next part of the story.
2. The story will be dynamically generated and displayed on the page.
