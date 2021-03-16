# Introduction
![](CleanShot%202021-03-15%20at%2022.57.20.gif)
Animal Crossing turnip.exchange CLI, because why not?!

# Description
This is a CLI to search for open islands in Animal Crossing - New Horizons that are open for you to join!

# Installation
This package is not yet published anywhere; To install this package you'd need to clone this repository first and setup from source:

```
git clone https://github.com/gcarrarom/turnip-exchange-automator.git
cd turnip-exchange-automator
pip install .
```

After installed, you will have now the new `turnip` command in your terminal `$PATH`.

## Requirements
The requirements of this CLI are suppposed to be installed automatically by the installation process, but the list of packages necessary are available in the [requirements](requirements.txt) file.

# Usage
To get started, all you need to do is run `turnip` from the command line and that shall give you a list of islands available and their turnip prices:
![](CleanShot%202021-03-15%20at%2022.47.55@2x.png)

For more capabilities, you can always run `turnip --help`:
```
turnip-exchange-automator at ☸️ docker-desktop ()
⌁ turnip --help
Usage: turnip [OPTIONS]

Options:
  --minimum INTEGER    Minimum tulip price to show
  --threshold INTEGER  Threshold where the price is green
  --watch              Whether or not to watch for the islands constantly
  --help               Show this message and exit.
```

# Roadmap
1. Console printout visual revamp
2. Multiple output types
3. Support for island notification
4. Support for joining islands' queues automatically
5. Support for abstracting the queueing interface completely - No more heavy page-loads
6. Querying for fees (that's going to be tricky)
7. Make it easier to install (Could be prioritized if someone else is using it :laugh:)