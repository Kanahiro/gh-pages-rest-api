## What is this
This make a virtual REST API server on GitHub repository.
By analyzing JSON files, the script makes directories and some files.
User can access datas of JSON file as if REST API server

## Sample
Now sample.json is in ./json and have following structure.

```json

{
    "data": [
        {
            "no": "1",
            "date": "2020-01-28T00:00",
            "place": "japan",
            "age": "22",
            "sex": "female"
        },
        {
            "no": "2",
            "date": "2020-02-14T00:00",
            "place": "australia",
            "age": "50",
            "sex": "male"
        }
    ],
    "last_update": "2020-03-14T23:14:01.849130+09:00"
}
```

The script loads JSON files in ./json .

Now only 'sample.json' is in ./json . When main.py runs and loads sample.json, it makes files as you can access like following.

|  data you want  |  REST API URL  |
| ---- | ---- |
|  all of sample.json  |  https://kanahiro.github.io/gh-pages-rest-api/sample  |
|  last_update of sample.json  |  https://kanahiro.github.io/gh-pages-rest-api/sample/last_update  |
|  data[0] of sample.json  |  https://kanahiro.github.io/gh-pages-rest-api/sample/data/0  |
|  data[1] of sample.json  |  https://kanahiro.github.io/gh-pages-rest-api/sample/data/1  |
|  data[1]['no'] of sample.json  |  https://kanahiro.github.io/gh-pages-rest-api/sample/data/1/no  |

## Usage
1. Fork this repo
2. Activate GitHub Actions and Pages (gh-pages)
3. Set JSON files in ./json
4. Push to master and fire Actions, then start hosting.