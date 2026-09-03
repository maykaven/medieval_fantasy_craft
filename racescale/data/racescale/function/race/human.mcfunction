# Human -> scale 1.0 (unchanged)
scoreboard players set @s racescale_race 1
function racescale:apply
tellraw @s {"text":"Heritage registered: Human (body scale 1.0).","color":"gold"}
