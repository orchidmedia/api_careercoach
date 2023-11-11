## UPLOAD FILE PDF

## LOCAL
```
uvicorn main:app --reload --env-file .env

```
##
Base URL 
```
https://careercoach-b957c7cfa4b2.herokuapp.com/
```

```
curl --location 'http://127.0.0.1:8000/upload/csv' \
--form 'file=@"/Users/dortizvega/Downloads/HOJA DE VIDA 1.pdf"'
```

### request for carrier suggestion
```
curl --location 'http://127.0.0.1:8000/recommend' \
--header 'Content-Type: application/json' \
--data '{
    "recommend":"I would love to combine my current set of skills from the CV uploaded before with the fashion industry"
}'
```


### request for carrier challenges
```
curl --location 'http://127.0.0.1:8000/career' \
--header 'Content-Type: application/json' \
--data '{
    "recommend":"CTO VP"
}'
```