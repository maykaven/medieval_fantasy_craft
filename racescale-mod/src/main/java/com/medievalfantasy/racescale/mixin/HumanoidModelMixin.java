package com.medievalfantasy.racescale.mixin;

import com.medievalfantasy.racescale.RaceScaledState;
import com.medievalfantasy.racescale.RaceShape;
import net.minecraft.client.model.HumanoidModel;
import net.minecraft.client.model.geom.ModelPart;
import net.minecraft.client.renderer.entity.state.HumanoidRenderState;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

/**
 * Keeps the head at its natural size for races whose body is scaled.
 *
 * The body scale is applied to the whole pose, which would take the head with
 * it, so the head is counter-scaled by the inverse: net effect, a normal head on
 * a shorter or taller body. That is what makes a dwarf read as stocky and an elf
 * as elongated rather than simply shrunk or enlarged.
 *
 * This targets HumanoidModel rather than PlayerModel on purpose. Armour models
 * extend the same base class and are handed the same render state, so hooking
 * here counter-scales a helmet exactly like the head it sits on - otherwise a
 * dwarf would wear a shrunken helmet on a full-size head.
 *
 * The scales are written on every call, never left set, because model instances
 * are shared between entities: a value left behind would leak onto the next
 * humanoid rendered with the same model.
 */
@Mixin(HumanoidModel.class)
public abstract class HumanoidModelMixin {
    @Shadow
    @Final
    public ModelPart head;

    @Shadow
    @Final
    public ModelPart hat;

    @Inject(method = "setupAnim(Lnet/minecraft/client/renderer/entity/state/HumanoidRenderState;)V", at = @At("TAIL"))
    private void racescale$keepHeadNatural(HumanoidRenderState state, CallbackInfo ci) {
        float x = 1.0F;
        float y = 1.0F;

        if (state instanceof RaceScaledState scaled) {
            RaceShape shape = scaled.racescale$shape();
            if (shape.keepHeadSize() && !shape.isNatural()) {
                x = 1.0F / shape.width();
                y = 1.0F / shape.height();
            }
        }

        this.head.xScale = x;
        this.head.yScale = y;
        this.head.zScale = x;
        this.hat.xScale = x;
        this.hat.yScale = y;
        this.hat.zScale = x;
    }
}
