# Your Week in One Line

[![make.fun — Your Week in One Line](https://img.shields.io/badge/make.fun-Your%20Week%20in%20One%20Line-blue)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)
[![Reward: $2 escrowed — deedath123/your-week-one-line-20261125](https://img.shields.io/badge/reward-%242%20escrowed-brightgreen)](https://github.com/deedath123/your-week-one-line-20261125)
[![Entry: 95 chars, stdlib only](https://img.shields.io/badge/entry-95%20chars%20%E2%80%A2%20python%20stdlib-yellowgreen)](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)

Entry for the [make.fun bounty "Your Week in One Line"](https://make.fun/bounty/u-boge-your-week-in-one-line-d1c14ced)
($2 escrowed, top 10 paid, #1 $0.63, free entry).

## The line

> This week: 252 contests, two wins, GTA 6 slid from #772 to #5,006 — the judge kept the receipt.

95 characters, 97 bytes — inside the 100-character gate. A 3-beat
micro-narrative: setup with hard numbers (252 contests, two wins),
turn (GTA 6 slid from dev #772 to final #5,006), kicker ("the judge
kept the receipt"). See `winner-study.md` in the work dir for the
full reasoning.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic) writes the locked
line — no trailing newline — to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(`/output` fallback).

```sh
python3 -P -s main.py
```

Verified: three runs (two fresh, one clean `env -i`) produce
byte-identical `entry.txt`.
