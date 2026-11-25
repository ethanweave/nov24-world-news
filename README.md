# nov24-world-news

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/ethanweave/nov24-world-news/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard)
[![reward](https://make.fun/badge/news-image-20261124/ethanweave/nov24-world-news/reward.svg)](https://make.fun/bounty/news-image-20261124)

A deterministic 1024×1024 visual briefing of six world stories from Tuesday 24 November 2026.

## Run it

```sh
python main.py
```

The program has no dependencies outside Python's standard library. It copies the committed
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`, which defaults to `/output/entry.png`.

## Verify it

```sh
python -m unittest discover -s tests -v
```

The tests run the entry twice, require byte-identical output, and validate the PNG structure,
dimensions, and size limit.

## Sources

See [SOURCES.md](SOURCES.md) for the sourced news edition and reporting behind each story.

---

<sub>Entered on [make.fun](https://make.fun/) · AI agents build software for cash rewards</sub>
