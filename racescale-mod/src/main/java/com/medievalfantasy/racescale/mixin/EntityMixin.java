package com.medievalfantasy.racescale.mixin;

import com.medievalfantasy.racescale.RaceScale;
import com.medievalfantasy.racescale.RaceShape;
import net.minecraft.world.entity.Avatar;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.entity.EntityDimensions;
import net.minecraft.world.entity.Pose;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfoReturnable;

/**
 * Resizes the hitbox so physics agrees with what is drawn. Without this a
 * 20%-taller elf would still collide like a 1.8-block human.
 *
 * The head is deliberately not considered here: keeping a natural head is a
 * rendering detail, and the collision box follows the body.
 */
@Mixin(Entity.class)
public abstract class EntityMixin {

    @Inject(method = "getDimensions", at = @At("RETURN"), cancellable = true)
    private void racescale$resizeByRace(Pose pose, CallbackInfoReturnable<EntityDimensions> cir) {
        Entity self = (Entity) (Object) this;
        if (!(self instanceof Avatar)) {
            return;
        }

        RaceShape shape = RaceScale.shapeFor(self);
        if (shape.isNatural()) {
            return;
        }

        // EntityDimensions.scale(widthFactor, heightFactor) is per-axis already.
        cir.setReturnValue(cir.getReturnValue().scale(shape.width(), shape.height()));
    }
}
