# YAPP

Yet Another Python Project in the university.

## Getting Started

### Linux

1. Clone and navigate to this repo.
2. `bash init.sh`
3. Visit `http://localhost:5000/`.

### Window

1. Clone and navigate to this repo.
2. `init.bat`
3. Visit `http://localhost:5000/`.

## Measurements

> Caveat: Ensure you are running the app before measuring whatever.

### Measure performance between encryption functions

```shell
py yapp/performance.py # record the performances
py yapp/show_performance.py # show performance graph
```

### Measure accuracies between descryption functions

```shell
py yapp/accuracy.py # record the accuracies
py yapp/show_accuracy.py # show accuracy graph
```

## TODOs

- Actually signed in user and show user specific content? (Mess with session cookie)
- Style the website
- Rewrite encryption functions
