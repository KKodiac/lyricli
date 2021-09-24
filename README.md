# Lyricli

Tmux 키고 터미널에서 작업하고 있는데 현재 틀어논 노래의 가사가 자주 궁금해져서 만들어봤습니다.

코로나 때문에 코노도 자주 못가는데 집에서라도 불러야죠. 🔥

터미널에서 원하는 가사를 보여줍니다. 

Simple script to display song lyrics on terminal.

## Resources 
 - Homepage: [https://github.com/KKodiac/lyricli](https://github.com/KKodiac/lyricli)
 - Issues: [https://github.com/KKodiac/lyricli/issues](https://github.com/KKodiac/lyricli/issues)
 - Python Package: [https://pypi.org/project/lyricli/0.0.9/](https://pypi.org/project/lyricli/0.0.9/)

## Requirements
 - Python 3.8+

## Installation 
 ```sh
python3 -m pip install lyricli==0.0.11
 ```
 
## Usage
![lyricli](https://user-images.githubusercontent.com/35219323/134548133-cfe5a138-1303-4c61-8b94-22525e499079.gif)

```sh
lyricli lyrics [-t, --title] {MUSIC-TITLE} [-r, --artist] {ARTIST-NAME}

# 위가 안되면 /usr/local/bin/ 에 lyricli 가 있는지 확인해주세요.
# if above doesn't work, please check if lyricli is visible in /usr/local/bin/ 
# alias 로 설정 하는 법 
alias lyricli="python3 -m lyricli"

```
## License

Contributor [Sean Hong](https://github.com/KKodiac)

Licensed under MIT License 
