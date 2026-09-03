# Orc -> scale 1.1 (10% bigger overall)
scoreboard players set @s racescale_race 4
function racescale:apply
tellraw @s {"text":"Heritage registered: Orc (body scale 1.1).","color":"gold"}
