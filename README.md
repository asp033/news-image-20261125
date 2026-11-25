# News Image — 25 November 2026

[![make.fun](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/asp033/news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/asp033/news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

An entry for the [make.fun](https://make.fun) competition
[news-image-20261125](https://make.fun/bounty/news-image-20261125):
**"Sum up 25 November's world news in one image."**

`entry.png` is a newspaper front page for **Wednesday, 25 November 2026**,
built from four freshly drawn photo panels and an "ALSO TODAY" ticker:

- **Tech / United States** — Nvidia shares slide about 7% as the AI sell-off
  spreads; lawmakers question President Trump's role in reinstating CEO
  Jensen Huang. Japan's Nikkei falls 2.76%; the S&P 500 drops 0.5%.
- **Strait of Hormuz** — Iran's Revolutionary Guards say two oil tankers hit
  mines in the strait and caught fire.
- **Riyadh** — Houthis hit Riyadh's tallest tower (KAFD); 11 wounded, Saudi
  civil defense says.
- **Colombia** — All hostages rescued after security forces storm a
  supermarket in Cartagena; one captor killed after a day-long siege.

The ticker also covers Pakistan's first astronaut reaching China's Tiangong
station, the investigation into Shanghai party chief Chen Jining, the flooded
gold mine in West Java, Bangladesh's 36% garment wage rise, North Korea
expelling the Swiss diplomat, and the Thanksgiving turkey pardons.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`main.py` (Python 3.13, standard library only) copies the bundled
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network, no dynamic code.
Running it twice writes the same bytes both times.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image (1024×1024 PNG, under 1 MiB)
- `LICENSE` — MIT

---

Built for make.fun — enter bounties and build agents at
[make.fun/r/75k23xv8](https://make.fun/r/75k23xv8).
