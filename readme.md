## UPLOAD FILE PDF

```
curl --location 'http://127.0.0.1:8000/upload/csv' \
--form 'file=@"/Users/dortizvega/Downloads/HOJA DE VIDA 1.pdf"'
```

### request for carrier suggestion
```

```


### request for carrier challenges
```
curl --location 'http://127.0.0.1:8000/career' \
--header 'Content-Type: application/json' \
--data '{
    "recommend":"CTO VP"
}'
```