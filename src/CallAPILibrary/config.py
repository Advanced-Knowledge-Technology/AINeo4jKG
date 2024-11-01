SAVE_FOLDER_PATH="CallAPILibrary/results"
TEMP_SAVE_FOLDER_PATH="CallAPILibrary/results/temp"
TEMP_LOG_FOLDER_PATH="CallAPILibrary/logs/temp"
API_KEYS_PATH="CallAPILibrary/data/gemini_api_keys.json"
URL= "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"
MAX_CALL_COUNT = 2
SLEEP_TIME = 30
HEADERS='{"Content-Type": "application/json"}'

SAFETY_SETTINGS='''[
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
]'''

GENERATION_CONFIG='{"temperature": 0.3, "top_p": 0.5, "top_k": 1}'