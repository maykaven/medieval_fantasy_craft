package com.medievalfantasy.racescale.mixin;

import com.medievalfantasy.racescale.RaceScale;
import com.medievalfantasy.racescale.RaceShape;
import net.minecraft.world.entity.Avatar;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityDimensions;
import net.minecraft.world.entity.Pose;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Unique;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Resizes the hitbox so physics agrees with what is drawn. Without this a
 * 20%-taller elf would still collide like a 1.8-block human.
 *
 * The head is deliberately not considered: keeping a natural head is a rendering
 * detail, and the collision box follows the body.
 *
 * <h2>Why the cache</h2>
 *
 * getDimensions is called many times per tick per entity - movement, collision
 * resolution, pose changes - so doing the race lookup on every call put the
 * server thread thousands of milliseconds behind. The shape can only change when
 * DAG adds or removes race modifiers, which happens on registration, login and
 * respawn, so recomputing once per game tick is far more often than necessary and
 * costs nothing measurable.
 */
@Mixin(Entity.class)
public abstract class EntityMixin {
    @Unique
    private RaceShape racescale$shape = RaceShape.NONE;

    @Unique
    private long racescale$shapeTick = Long.MIN_VALUE;

    @Inject(method = "getDimensions", at = @At("RETURN"), cancellable = true)
    private void racescale$resizeByRace(Pose pose, CallbackInfoReturnable<EntityDimensions> cir) {
        Entity self = (Entity) (Object) this;
        if (!(self instanceof Avatar)) {
            return;
        }

        long now = self.level().getGameTime();
        if (now != this.racescale$shapeTick) {
            this.racescale$shapeTick = now;
            this.racescale$shape = RaceScale.shapeFor(self);
        }

        RaceShape shape = this.racescale$shape;
        if (shape.isNatural()) {
            return;
        }

        // EntityDimensions.scale(widthFactor, heightFactor) is per-axis already.
        cir.setReturnValue(cir.getReturnValue().scale(shape.width(), shape.height()));
    }
}
