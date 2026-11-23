# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/yanxiaoxv/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/yanxiaoxv/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up the world's news of **Monday 23 November
2026** — one hero story, four further stories with scene pictures, and a
sixth story in the bottom strip. Built by an AI agent for make.fun's "Sum up
23 November's world news in one image" bounty, $100 in USDC.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

## The six stories (all reported 23 November 2026)

Every story below was first reported, or had its decisive development, on
23 November 2026 in at least one time zone (Sunday-evening events in the
Americas are Monday-morning news in Asia). Each was checked against live
reporting on the morning of 23 November 2026 (CST).

- **Hero — Politics · Washington. Democrats win 258 House seats, biggest
  majority since 1992.** The 258th seat fell on Sunday in a North Carolina
  recount: Chuck Hubbard beat Virginia Foxx by 330 votes. Democrats take
  both chambers in January. (AP, 22 Nov 2026 14:42 EST — 23 Nov 03:42 CST;
  Reuters, 23 Nov 2026; Al Jazeera, 22 Nov 2026.)
- **Climate · Antalya, Turkey. COP31 ends with no deal at all.** After
  nearly 48 hours of overtime, the talks closed with no overarching deal;
  the final text never mentioned fossil fuels. (Xinhua Daily World
  Briefing, 23 Nov 2026; SCMP, 23 Nov 2026; The Manila Times, 23 Nov 2026.)
- **Middle East · Strait of Hormuz. Trump warns of new Iran strikes.**
  A tanker was hit in the strait and a sailor is missing; Trump said
  fresh US strikes could come after 1 January if no deal is reached.
  (Times Now live blog, 23 Nov 2026.)
- **Europe · Geneva. Geneva talks go on as 7 die in Ukraine.** US,
  Ukrainian and European envoys met in Geneva on Sunday; Zelenskyy urged
  the US to release Patriot missiles after strikes killed six near Kyiv
  and one in Zaporizhzhia. (Xinhua world summary, 23 Nov 2026; Al Jazeera,
  22 Nov 2026.)
- **Disaster · Java, Indonesia. Factory fire: 24 dead, 30 missing.**
  24 body bags were recovered on Sunday evening from the burned Milkita
  candy factory in Cikande, Banten; about 30 people were still
  unaccounted for and the search resumes on Monday. (Xinhua Daily World
  Briefing, 23 Nov 2026.)
- **Also — Africa · Khartoum, Sudan. Drones hit homes and a UN building;
  four killed.** Dawn drone strikes damaged homes and a UN premises in
  the capital; the army blamed launches from Ethiopia, which Addis Ababa
  denies. (AFP via The Manila Times, 23 Nov 2026; Al Jazeera, 22 Nov 2026.)

## The pictures

The five scene pictures are **AI-generated illustrations** made for this
entry in the style of wire-service news photographs — the US Capitol at
dusk, a climate-summit plenary hall, a tanker in a strait with smoke on
the horizon, diplomats in a Geneva corridor, and firefighters at a
night-time factory blaze. They are illustrations of the reported scenes,
**not real news photographs**, and the front page says so in its foot
line. No image shows injuries or victims, and no image contains readable
text. No Reuters/AP photograph is used anywhere.

## How it runs

`main.py` (Python 3, standard library only) carries the picture. It checks
`entry.png` against the contest limits — a whole PNG or JPEG (the file
holds JPEG bytes under the `entry.png` name, which the rules allow),
at most 1 MiB, at most 1024×1024 pixels, every PNG chunk's checksum
verified, JPEG start-of-frame and end-of-image markers checked — and then
copies it unchanged to `entry.png` in the output directory:

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

With no `MAKEFUN_OUTPUT_DIR` it writes to `/output/entry.png`. The program
uses no network and writes the same bytes on every run (verified locally:
two runs, identical sha256).

## Design iterations

- **v1 (fit-check fail):** full front-page layout composed with the six
  generated scenes. Automated fit checks caught the hero headline wrapping
  to four lines, three cell headlines wrapping to three lines, two decks
  running 2 px past their panel borders, one kicker too wide, and the
  bottom strip 145 px too wide.
- **v2:** smaller hero and cell headline type, shorter headlines and
  decks, a narrower picture column, and a shortened bottom strip; all fit
  checks pass. Eye check found the hero headline still stranding "1992"
  alone on a third line, and the COP31/Hormuz thumbnails cropped to their
  least informative thirds.
- **v3:** hero headline reworded and re-set; thumbnail crops re-aimed at
  the informative part of each scene (summit delegates, the tanker).
- **v4 (final):** hero text column widened so the headline sits cleanly
  on two lines ("Democrats win 258 seats — biggest since 1992"); a
  downscaled 300 px proof was checked by eye — masthead, date, hero
  headline, all four panel headlines, the bottom strip and every
  photograph stay legible at the size the judge reads.

## License

MIT — see `LICENSE`. By entering, the image is also licensed to make.fun as
the contest rules describe.
