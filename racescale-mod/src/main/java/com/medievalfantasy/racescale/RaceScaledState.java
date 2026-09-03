package com.medievalfantasy.racescale;

/**
 * Duck interface for carrying a race shape on a render state.
 *
 * Deliberately NOT in the mixin package: Mixin refuses to class-load a
 * non-mixin type from a declared mixin package (IllegalClassLoadError).
 *
 * Entity rendering has been state-based since 1.21.2 and the state holds no
 * reference to the entity, so the shape has to be attached while the state is
 * being extracted and read back later during rendering.
 */
public interface RaceScaledState {
    void racescale$setShape(RaceShape shape);

    RaceShape racescale$shape();
}
