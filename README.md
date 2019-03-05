# Python Twitter Bot
## Description
A easy build and lightweight twitter bot written in Python. For this project I also created batch-files
to run the script in background and to start it easily globally via the terminal, but I decided not to
publish it in this repo.

Feel free to use it.

## Usage
Simply create some text-file w/ the tweets in it separated by `§§§`. Run the script with:<br>
`twitter-bot.py <file> <number of seconds to wait>`

Given the `example.txt` file containing two sample tweets, you can call
the script as follows:

```bash
python twitter-bot.py example.txt 10
```

This will publish both tweets with ten seconds between each.