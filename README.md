# music-gen-cli

A cli wrapper around Meta's Audiocraft with tuning for smaller GPUs

# USAGE

```
music-gen-cli -k keyword1 ([-k keywordn]+) -f [fileprefix|fileprefix] (-p) (-m [small(*default*)|medium|melody|large)
```

- -k *keyword* |  --keyword=*keyword* - provide multiple prompts for music generation. eg. 'speed metal'
- -f *prefix* | --fileprefix=*prefix* - provide a prefix for the generated file
- -m *model* | --modelname=*model* - provide the audiocraft model (small|medium|melody|large)
- -p  - Plays the generated composition from your audio device when generated

## EXAMPLES

This will generate some industrial metal in a file called `metal-out.wav`:

```
python ./music-gen-cli -k dark -k guitar -k industrial -f metal-out
```

This will generate gothic classical music in a file called `classical-out.wav` and *play it out loud*

```
python ./music-gen-cli -k piano -k cello -k piano -k classical -f classical-music -p

```


# Requires CUDACUDACUDa

- Tested on a 4GB GTX 1650 Super and NVIDIA 4070
- Uses Audiocraft's small model
- Keen samples on a 4GB card to under 15 seconds

# Building

`pip install .`


# Using within Nix

Slightly over-engieered on purpose as I'm learning Nix-expression.

Note that `python310Full`'s fails silently with `sounddevice` due to Python's `ctype.util.find_library` having
an explicit depenency on `ld`. To work around this in Nix I have added binutils to the shell as it's not in the upstream python.
TODO: PR

You'll also need to ensure that you can include cuda deps with non-free licenses.

```
 echo "{ allowUnfree = true; }" >> ~/.config/nixpkgs/config.nix
```

## nix-shell

```
nix-shell ./music-gen-cli-shell.nix
```

## nix flakes

First set `allowUnfree` as above and then:


```
nix develop --impure
```

As not `audiocraft` is not avaiable for via nix pkgs, you should then:

```
pip install . --user
```

## EXAMPLE AUDIO


- [metal-out.wav](./examples/metal-out.wav)
- [classical-out.wav](./examples/classical-out.wav)
