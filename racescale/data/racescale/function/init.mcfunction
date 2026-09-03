# Race body scaling - initialisation (runs on #minecraft:load)
# racescale_race : chosen race  1=human 2=dwarf 3=elf 4=orc
# racescale_pick : /trigger input, usable WITHOUT cheats/op
# racescale_deaths: deathCount, so we can re-apply after respawn
scoreboard objectives add racescale_race dummy
scoreboard objectives add racescale_pick trigger
scoreboard objectives add racescale_deaths deathCount
