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
$ python twitter-bot.py example.txt 10
```

This will publish both tweets with ten seconds between each.

### Docker
If you want to run it in a Docker container to keep things clean,
please insert your twitter API credentials into the `config.py` file,
write your tweets into the provided `example.txt` file and run the following
two commands:

```bash
$ docker image build -t twitter-bot .
$ docker container run -it --rm --name twitter-bot twitter-bot
```

This will publish the tweets with a delay of ten seconds between each.

## To Do

- provide a way to specify the input file and delay via Docker `ARG`
and `ENV`
