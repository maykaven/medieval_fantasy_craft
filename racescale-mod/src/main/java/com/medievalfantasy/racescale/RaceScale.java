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
 * and friends, and re-applies them on every login and respawn. Vanilla syncs
 * attribute modifiers to clients, so the same lookup works on both sides with no
 * packets of our own - and registering with Garrick is all the player has to do.
 *
 * This deliberately reads DAG's *observable game state* rather than its storage.
 * The race is persisted to world files under data/dagmod/players/ and DAG exposes
 * no API, so the alternatives were parsing its save format or mixing into its
 * private classes. If DAG ever renames these modifiers the behaviour degrades to
 * "human" instead of breaking.
 *
 * <h2>Cost</h2>
 *
 * This is called from Entity#getDimensions, which runs many times per tick, so
 * every identifier is allocated once up front rather than per lookup. Callers on
 * the hot path should still cache the result per tick - see EntityMixin.
 */
public final class RaceScale {
    public static final String OBJECTIVE = "racescale_race";
    private static final String DAG = "dagmod";

    /** Attributes DAG hangs race bonuses on; checked as a set rather than guessing which holds what. */
    private static final Holder<Attribute>[] CARRIERS = carriers();

    // Allocated once. Identifier.fromNamespaceAndPath validates its input, so
    // building these per call was pure waste on a very hot path.
    private static final Identifier[] DWARF = ids("dwarf_speed", "dwarf_health", "dwarf_mining");
    private static final Identifier[] ELF = ids("elf_speed", "elf_reach");
    private static final Identifier[] ORC = ids("orc_attack", "orc_health");

    private RaceScale() {
    }

    @SuppressWarnings("unchecked")
    private static Holder<Attribute>[] carriers() {
        return new Holder[] {Attributes.MOVEMENT_SPEED, Attributes.ATTACK_DAMAGE, Attributes.MAX_HEALTH};
    }

    private static Identifier[] ids(String... paths) {
        Identifier[] out = new Identifier[paths.length];
        for (int i = 0; i < paths.length; i++) {
            out[i] = Identifier.fromNamespaceAndPath(DAG, paths[i]);
        }
        return out;
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

        // Attributes on the outside: fetch each AttributeInstance once and test
        // every marker against it, rather than re-fetching per marker.
        for (Holder<Attribute> carrier : CARRIERS) {
            AttributeInstance instance = living.getAttribute(carrier);
            if (instance == null) {
                continue;
            }
            if (hasAny(instance, DWARF)) {
                return RaceShape.DWARF;
            }
            if (hasAny(instance, ELF)) {
                return RaceShape.ELF;
            }
            if (hasAny(instance, ORC)) {
                return RaceShape.ORC;
            }
        }
        return RaceShape.NONE;
    }

    private static boolean hasAny(AttributeInstance instance, Identifier[] markers) {
        for (Identifier marker : markers) {
            if (instance.hasModifier(marker)) {
                return true;
            }
        }
        return false;
    }
}
