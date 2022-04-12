# Lyricli 

Simple API utilizing modules in lyricli

As far as this project is concerned, I know that no one besides me are using it. And utilizing its modules in some way seemed reasonable as of current situation of this package. It's being used for simple api with [this](https://github.com/KKodiac/menu_bar_lyrics) Mac OS menu bar application.

# Usage
Use it just like any other Flask application.
```py
export FLASK_APP='app'
flask run
```

## URL

There are two URL paths to utilize: 
```
localhost:5000/lyrics/<title>
localhost:5000/lyrics/<title>:<aritst>
```