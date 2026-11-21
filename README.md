# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/pytraaa9-ai/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/pytraaa9-ai/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

A program that writes one image summing up Saturday 21 November 2026 world news — a newspaper front page (1024×1024 PNG): lead story Russian missiles landing in Poland (the new 21 November development of the overnight assault on Ukraine), plus 37 more stories across six continents, a world map, and Friday's AI-driven market rout. Partial-day v1 edition — morning + afternoon news; a full-day v2 will supersede it.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## The day's news

- **Lead:** Russian missiles land in Poland — Two Kh-101 missiles and a jet-powered drone crash in south-east Poland during the overnight assault on Ukraine. PM Tusk calls it a deliberate provocation; NATO scrambles jets. No injuries reported; world leaders rally behind Warsaw.
- **Second story:** Houthi missiles downed — Coalition downs three ballistic missiles headed for Riyadh, the third night of alerts. Houthis threaten ports and a power station.
- UK–EU biggest post-Brexit deal: Burnham signs three deals: food trade, carbon markets, youth mobility for 100,000.
- Gen Z protests spread: Students march in 25 countries over living costs, rearmament and climate.
- Zecler verdict delivered: Three officers sentenced over 2020 racist beating of producer Michel Zecler.
- France probes Depardieu: Prosecutors open probe into alleged gang rape involving Depardieu and Houellebecq.
- Villepin runs for president: Ex-PM Dominique de Villepin announces French presidential candidacy.
- Spain heads to 29 Nov vote: PP's Feijóo gains after TV debate; housing costs central to campaign.
- Israeli strikes kill in Gaza: Six killed by strikes, seven by drones; settlers top 400 olive-harvest attacks.
- Hormuz attacks continue: Iran says it downed a US MQ-9 drone; US sanctions four oil trustees.
- Saudi–Japan oil deal: Japan to buy up to 8m barrels of Saudi crude to refill Hormuz-era reserves.
- Iraq enters militia stronghold: Forces move into Jurf al-Sakhar for first time in 12 years.
- Nigeria boat capsizes: Funeral boat overturns in Bayelsa; at least 4 dead, 300 feared missing.
- Tanzania: Lissu convicted: Opposition leader Tundu Lissu convicted of sedition; UK voices concern.
- Uganda Ebola curbs: Gatherings and travel curbed in 34 districts bordering DR Congo.
- Kenya starts oil drilling: First onshore crude drilling begins in Turkana's South Lokichar fields.
- Riemann proof claim: Anthropic mathematician releases claimed AI-assisted proof of the 1859 problem.
- Japan–China ties at low: 93% of Japanese call ties poor; Beijing scales down Takaichi welcome.
- South Korea impeachment move: Ruling party moves to impeach chief justice before martial-law anniversary.
- Nepal PM to visit India: Balendra Shah to visit India Nov 22–23, his first trip abroad as PM.
- India: tainted alcohol kills 11: 11 dead, 180+ hospitalised after drinking adulterated alcohol.
- COP31 runs past deadline: Antalya talks into overtime; draft drops fossil-fuel phase-out.
- AI rout: S&P −3.70%, Nasdaq −5.28%: Nasdaq erases all 2026 gains; S&P and Dow into correction.
- Trump wants Huang back: Trump says ousted Nvidia chief Jensen Huang deserves a second chance.
- FBI database hacked: CNN: FBI crime database breached; cyber chief fired after US outages.
- Palisades fire verdict: Jury convicts Jonathan Rinderknecht of arson; fire killed 12, razed 6,800 homes.
- Measles status lost: US, Mexico, Bolivia lose measles-free status; US counts 7,700 cases, 13 deaths.
- GTA VI $3.8bn day one: Rockstar launch beats every game and single-day film box-office record.
- Iowa lead blast halted: Judge halts Army plan to detonate tons of lead azide at Iowa plant.
- YouTube schools settlement: YouTube finalising multibillion-dollar deal with US schools over addiction claims.
- Peru quake 6.7–6.9: Strong quake shakes central Peru; no casualties at first; Lima flees outdoors.
- Bolsonaro hospitalised: Ex-president taken to Brasília hospital with intestinal obstruction.
- Haiti: Salvadoran troops killed: Two soldiers die handling explosives; first deaths since deployment.
- Argentina risk tops 1,000: Bonds fall into distressed territory; country risk passes 1,000 points.
- BepiColombo reaches Mercury: Twin probes enter Mercury orbit after 8 years and 10bn km.
- Pancreatic cancer pill: Daraxonrasib trial: tumours undetectable in 1 in 12 patients.
- CERN rare decay found: First evidence of ultra-rare particle decay after 40+ years.
- Voyager 1: 24 light-hours: NASA's farthest probe now 16.1bn miles away; light takes a day.

All stories were verified against at least two reputable sources
(Reuters, AP, AFP, BBC, Al Jazeera, UN News) on 21 November 2026.
This v1 entry covers the morning + afternoon of Saturday 21 November 2026;
a full-day v2 will supersede it before the deadline.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the
committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
(falling back to `/output/entry.png`). The copy is byte-for-byte, so two
runs always produce identical output.

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=x9vj0gh6&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
