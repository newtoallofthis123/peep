
<img style="width: 50%" src="/docs/static/header_raw.svg" alt="Header">

## Personalized Environment and Execution Prompt

PEEP is the friendly assistant we have all been looking for. It lives in the command line and loves to improve your command line experience.

## Installation

For now, there is no pypi package for peep but there are plans to make one in the future. For now, you can install peep by cloning the repository and installing the requirements. If you don't know how to do so, you can download a zip from the github repository and extract it. Then, open the folder and run  `start.py`

Using start.py installs all the dependencies and bootstraps the package to act as a cli. It also adds it to the alias. If you want to do this manually, you can add the alias to your bashrc or zshrc file. To set alias, run  `alias peep=$pwd/src/main.py`

```shell
git  clone  [https://github.com/newtoallofthis123/peep.git](https://github.com/newtoallofthis123/peep)  
cd  peep  
pip  install  -r  requirements.txt  
python3  start.py`
```

## Usage

Peep uses plain english to help you. The syntax is very human-readable hence there is no need to remember weird command line flags. Most of all commands in peep have a basic syntax of  `peep  {primary command} {action} {query}`

This makes it very easy to navigate. For example, if you have to use the editor command for a python file, you can simply type  `peep  editor hello.py python`  and peep will open the file hello.py in the python editor.

All these command syntaxes are included in the package by default. You can access them by typing  `peep  run commands`  in the command line. Or you can open this webpage and read the documentation.

`peep  {primary command} {action} {query}  
  
// Example  
peep  editor hello.py python`

## Commands

Peep has a lot of commands. You can access them by typing  `peep  run commands`  in the command line. Or you can open this  [webpage](#commands)  and read the documentation.

### Editor

The editor command is used to open files in the editor of your choice. To use the editor command, you can simply enter  `peep  editor {file} {language}`

List of supported Languages

- python
- javascript
- html
- css
- c/c++
- java
- markdown
- json

The language parameter is optional. If you don't specify the language, peep will try to guess the language of the file. If it can't guess the language, it will open the file in the default editor.

### Search

This editor command is one of the simplest commands in peep. It is used to search the web. To use the search command, you can simply enter  `peep  search {search_engine} {query}`

List of supported search engines

- Google
- Duckduckgo
- StartPage
- YouTube
- GitHub

### Markdown Editor

This command is used to open a markdown file in the markdown editor. To use the markdown editor command, you can simply enter  `peep  md {file}`

![Md Example](/docs/static/md_example.png)

### Ai (Work in progress)

You are welcome to contribute on  [github](https://github.com/newtoallofthis123/peep/tree/main/src/service/ai)

### QRCodes

This command is used to generate qrcodes. All QRCodes are stored in the  `~/.peep/qr`  directory. To use the qrcode command, you can simply enter  `peep  qrcode {action} {filename} {text}`

Possible Actions Include

- make: make a qrcode
- read: reads the info a qrcode
- open: opens a qrcode
- list: lists generated QRCodes
- delete: deletes a qrcode by name

### YouTube

Provides a wide variety of commands related to youtube. To use, simply enter  `peep  yt {action} {query}`

List of Actions

- search: accepts a query and prints out the search results
- stream: opens the video stream in your browser
- download: downloads the video in best quality locally
- video: accepts url and gets the info

### Music

Accepts music name and plays it in the browser. Results and stream is provided by YouTube. To use, simply enter  `peep  music {action} {music_name}`

List of Actions

- stream: opens audio stream in your browser
- download: downloads the audio in best quality

### Run

Handy command to change how peep behaves.
