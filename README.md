# Language Assistant

## Description
This repository lets you converse with an AI agent in a language of your choice (almost!). Currently should work well for English and German.

## Broad specification

There are three components to this:
1. Speech to Text
    - language detection
    - text transcription
2. NLU
    - interpretting the text
    - suitable response to the text
3. Text to Speech
    - reading out the text depending on the respondent

## Technical details

The code base is primarily Python and builds on the shoulders of giants!

## Requirements

In Linux environment, install some of the voice dependencies:

```
sudo apt update && sudo apt install espeak ffmpeg libespeak1
sudo apt install libttspico-utils
```