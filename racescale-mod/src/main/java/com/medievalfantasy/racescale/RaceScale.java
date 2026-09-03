package com.medievalfantasy.racescale;

import net.minecraft.core.Holder;
import net.minecraft.resources.Identifier;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.LivingEntity;
import net.minecraft.world.entity.ai.attributes.Attribute;
import net.minecraft.world.entity.ai.attributes.AttributeInstance;
import net.minecraft.world.entity.ai.attributes.Attributes;
import net.minecraft.world.scores.Objective;
import net.minecraft.world.scores.ReadOnlyScoreInfo;
import net.minecraft.world.scores.Scoreboard;

/**
 * Works out a player's race, and therefore their body shape.
 *
 * <h2>How the race is detected</h2>
 *
 * Primarily from DAG Mod's own race bonuses. When you register a heritage with
 * Innkeeper Garrick, DAG applies attribute modifiers named
 * {@code dagmod:dwarf_speed}, {@code dagmod:elf_speed}, {@code dagmod:orc_attack}
 * and friends. Vanilla syncs attribute modifiers to clients automatically, so the
 * same check works on both sides with no packets of our own - and picking a race
 * with Garrick is all the player has to do.
 *
 * This deliberately reads DAG's *observable game state* rather than its storage.
 * The race is persisted to world files under data/dagmod/players/ and DAG exposes
 * no API, so the alternatives were parsing its save format or mixing into its
 * private classes. Reading modifiers that vanilla already replicates couples us to
 * nothing but a handful of identifier strings, and if DAG ever renames them the
 * behaviour degrades to "human" instead of breaking.
 *
 * <h2>Manual override</h2>
 *
 * If the optional racescale datapack is installed, a non-zero {@code racescale_race}
 * score wins. That keeps a way to force a shape for testing, and to use the mod in
 * worlds without DAG at all.
 */
public final class RaceScale {
    public static final String OBJECTIVE = "racescale_race";
    private static final String DAG = "dagmod";

    // Attributes DAG hangs its race bonuses on. Checked as a set rather than
    // assuming which bonus lives on which attribute.
    private static final Holder<Attribute>[] CARRIERS = carriers();

    private static final String[] DWARF_MARKERS = {"dwarf_speed", "dwarf_health", "dwarf_mining"};
    private static final String[] ELF_MARKERS = {"elf_speed", "elf_reach"};
    private static final String[] ORC_MARKERS = {"orc_attack", "orc_health"};

    private RaceScale() {
    }

    @SuppressWarnings("unchecked")
    private static Holder<Attribute>[] carriers() {
        return new Holder[] {Attributes.MOVEMENT_SPEED, Attributes.ATTACK_DAMAGE, Attributes.MAX_HEALTH};
    }

    public static RaceShape shapeFor(Entity entity) {
        RaceShape override = fromScoreboard(entity);
        if (override != null) {
            return override;
        }
        return fromDagBonuses(entity);
    }

    /** Explicit override from the optional datapack, or null when unset. */
    private static RaceShape fromScoreboard(Entity entity) {
        Scoreboard scoreboard = entity.level().getScoreboard();
        Objective objective = scoreboard.getObjective(OBJECTIVE);
        if (objective == null) {
            return null;
        }

        ReadOnlyScoreInfo info = scoreboard.getPlayerScoreInfo(entity, objective);
        if (info == null) {
            return null;
        }

        return switch (info.value()) {
            case 1 -> RaceShape.NONE;
            case 2 -> RaceShape.DWARF;
            case 3 -> RaceShape.ELF;
            case 4 -> RaceShape.ORC;
            default -> null;
        };
    }

    /** Race inferred from the attribute modifiers DAG applies for each heritage. */
    private static RaceShape fromDagBonuses(Entity entity) {
        if (!(entity instanceof LivingEntity living)) {
            return RaceShape.NONE;
        }

        if (hasAnyMarker(living, DWARF_MARKERS)) {
            return RaceShape.DWARF;
        }
        if (hasAnyMarker(living, ELF_MARKERS)) {
            return RaceShape.ELF;
        }
        if (hasAnyMarker(living, ORC_MARKERS)) {
            return RaceShape.ORC;
        }
        return RaceShape.NONE;
    }

    private static boolean hasAnyMarker(LivingEntity living, String[] paths) {
        for (String path : paths) {
            Identifier id = Identifier.fromNamespaceAndPath(DAG, path);
            for (Holder<Attribute> carrier : CARRIERS) {
                AttributeInstance instance = living.getAttribute(carrier);
                if (instance != null && instance.hasModifier(id)) {
                    return true;
                }
            }
        }
        return false;
    }
}
