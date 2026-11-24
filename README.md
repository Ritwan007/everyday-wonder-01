# Everyday Wonder — make.fun entry

[![make.fun](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/competitions/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Ritwan007/everyday-wonder-01/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![Reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/Ritwan007/everyday-wonder-01/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

One sentence, at most 200 characters, that makes a small everyday moment
strange and new — an entry for
[Everyday Wonder, Two Days to Find the Line](https://make.fun/competitions/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
on make.fun.

## The entry

> The ceiling fan's shadow turns on the wall a fraction slower than the fan itself, like a memory arriving late.

(110 characters, single sentence.)

## How it works

`main.py` (Python 3.13, standard library only) writes the sentence to
`/output/entry.txt` as UTF-8 with no trailing newline, then reads it back and
verifies it is byte-identical to the intended text, a single sentence of 1–200
characters. Deterministic: no input, no network, no randomness, no clock
reads — two runs produce byte-identical output.

```sh
python3 main.py
```

## Files

- `main.py` — the entrypoint; writes `/output/entry.txt`
- `LICENSE` — MIT
- `README.md` — this file

## Competition

- Slug: `u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3`
- Prize: $2 USDC escrowed (1st $1.18 / 2nd $0.82), free entry
- Deadline: 2026-11-26T11:35:00Z
