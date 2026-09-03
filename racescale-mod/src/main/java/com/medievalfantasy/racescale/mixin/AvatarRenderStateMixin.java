package com.medievalfantasy.racescale.mixin;

import com.medievalfantasy.racescale.RaceScaledState;
import com.medievalfantasy.racescale.RaceShape;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Unique;

/** Carries the race shape on the player's render state. */
@Mixin(AvatarRenderState.class)
public abstract class AvatarRenderStateMixin implements RaceScaledState {
    @Unique
    private RaceShape racescale$shape = RaceShape.NONE;

    @Override
    public void racescale$setShape(RaceShape shape) {
        this.racescale$shape = shape;
    }

    @Override
    public RaceShape racescale$shape() {
        return this.racescale$shape;
    }
}
