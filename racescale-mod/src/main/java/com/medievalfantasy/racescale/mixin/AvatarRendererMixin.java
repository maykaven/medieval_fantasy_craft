package com.medievalfantasy.racescale.mixin;

import com.medievalfantasy.racescale.RaceScaledState;
import com.medievalfantasy.racescale.RaceScale;
import com.medievalfantasy.racescale.RaceShape;
import com.mojang.blaze3d.vertex.PoseStack;
import net.minecraft.client.renderer.entity.player.AvatarRenderer;
import net.minecraft.client.renderer.entity.state.AvatarRenderState;
import net.minecraft.world.entity.Avatar;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Applies the body scale inside AvatarRenderer#scale, the hook that runs before
 * the player model and before every one of its render layers. Armour is drawn as
 * layers within that same pose, so it stretches with the body and keeps fitting.
 * That is the whole reason for hooking here rather than scaling the model.
 *
 * Target descriptors matter here: AvatarRenderer is generic over
 * {@code AvatarlikeEntity extends Avatar & ClientAvatarEntity}, so the real
 * method erases to (Avatar, AvatarRenderState, float). The LivingEntity and
 * Entity overloads that javap also lists are bridge methods and must not be
 * targeted.
 */
@Mixin(AvatarRenderer.class)
public abstract class AvatarRendererMixin {

    @Inject(
        method = "extractRenderState(Lnet/minecraft/world/entity/Avatar;Lnet/minecraft/client/renderer/entity/state/AvatarRenderState;F)V",
        at = @At("TAIL")
    )
    private void racescale$captureRace(Avatar entity, AvatarRenderState state, float partialTick, CallbackInfo ci) {
        ((RaceScaledState) state).racescale$setShape(RaceScale.shapeFor(entity));
    }

    @Inject(
        method = "scale(Lnet/minecraft/client/renderer/entity/state/AvatarRenderState;Lcom/mojang/blaze3d/vertex/PoseStack;)V",
        at = @At("TAIL")
    )
    private void racescale$applyScale(AvatarRenderState state, PoseStack poseStack, CallbackInfo ci) {
        RaceShape shape = ((RaceScaledState) state).racescale$shape();
        if (!shape.isNatural()) {
            poseStack.scale(shape.width(), shape.height(), shape.width());
        }
    }
}
