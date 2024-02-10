from fastapi import FastAPI  # Corrected the module name to lowercase
import uvicorn
from fastapi.middleware.cors import CORSMiddleware  # Corrected the module path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def read_root():
    return {'status': 'active'}

@app.get('/test_endpoint')  # Updated to snake_case
def test_endpoint():  # Updated to snake_case
    return {'test status': 'successful'}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
