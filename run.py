# project/run.py
import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='158.85.190.238', port=port)