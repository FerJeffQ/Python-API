## Deploy FastAPI on Reder
```
gunicorn -w 4 -k uvicorn.workers.UvicornWorker app.app:app
```
Base de datos interna
```
 DEBUG=true
 ENVIRONMENT=development
 DATABASE_URL=sqlite+aiosqlite:///project.db
```