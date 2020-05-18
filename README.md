# sentiment-api
A Python API using the nltk library to analyse sentiment in text


## Request format
Supports both JSON and Multipart form requests.

```
{
    "text": "my text 123!",
    "sentiment_threshold": 0.1
}
```
- **text:** The plain text you want analysed. Non-alphabetic characters will be ignored and every word will be assessed (must be space seperated like a typical paragraph).
- **sentiment_threshold (optional):** Minimum sentiment value (Default is 0.1). 
A greater sentiment value will reduce the number of returned words only keeping those with strong positive & negative sentiment.

## Returned format
Returns a JSON

```
{
  "words": {
    "cool": {
      "occurances": 1,
      "score": 0.3182
    }...
  }
}
```
Returns a dictionary of `words` containing each word with a sentiment greater than the `sentiment_threshold`. This word contains its number of occurances in your text and it's sentiment score.

A positive value means the word has positive meaning and visa versa. A greater value means the word has greater sentiment.
