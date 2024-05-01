# Moments finder

1. Developed a cutting-edge moments finder tool capable  of identifying thematic segments within media content. 
2. Leveraged advanced techniques including speech transcription and GPT-powered sentiment analysis to achieve accurate results

# Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/video-transcript-analyzer.git
   ```

2. Navigate to the project directory:
   ```
   cd video-transcript-analyzer
   ```
   
3. Install dependencies using pip:
   ```
   pip install -r requirements.txt
   ```
4. Set up MongoDB:
   - Install MongoDB on your system if you haven't already.
   - Create a MongoDB database and collection to store video transcripts.
   - Update the MongoDB connection settings in main.py to point to your database.
     
5. Obtain OpenAI API key:
   - Sign up for OpenAI API and obtain an API key.
   - Update the OPENAI_API_KEY variable in main.py with your API key.
  
6. Run the application
   ```
   python3 api/main.py
   ```
   The API will be available at http://localhost:8000.

# Usage

# API Endpoint
    
- Endpoint: /analyze
- Method: POST
- Request Body: JSON object with the following format:
  ```
  {
    "title": "title of the transcript in the db",
    "genre": "genre which needs to be analyzed"
  }
  ```
- Response: JSON object with the scene information:
  ```
  {
    "prompt response" : "exact second where the genre is seen in the content"
  }
  ```

# Example Usage

```
curl -X 'POST' \
  'http://localhost:8000/api/v1/analyze' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "race 3 ka salman khan",
    "genre": "action"
  }'
```

