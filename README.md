#music-gen

A cli wrapper around Meta's Audiocraft

# USAGE

```
music-gen-cli -k keyword1 ([-k keywordn]+) -f [fileprefix|fileprefix] (-p)
```

eg. `python ./music-gen-cli -k dark -k guitar -k industrial -f metal`


# Requires CUDACUDACUDa

- Tested on a 4GB GTX 1650 Super
- Uses Audiocraft's small model

# Building

`pip install .`


