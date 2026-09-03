package com.medievalfantasy.racescale;

/**
 * How a race's body differs from a human's.
 *
 * @param width         X/Z factor
 * @param height        Y factor
 * @param keepHeadSize  whether the head should stay its natural size instead of
 *                      following the body. Dwarves and elves keep a normal head,
 *                      which is what makes one read as stocky and the other as
 *                      elongated rather than simply small or large all over.
 */
public record RaceShape(float width, float height, boolean keepHeadSize) {
    /** Human, or race unknown. */
    public static final RaceShape NONE = new RaceShape(1.0F, 1.0F, false);

    /** 20% shorter, same breadth, natural head. */
    public static final RaceShape DWARF = new RaceShape(1.0F, 0.8F, true);

    /** 20% taller, same breadth, natural head. */
    public static final RaceShape ELF = new RaceShape(1.0F, 1.2F, true);

    /** 10% bigger all over, head included. */
    public static final RaceShape ORC = new RaceShape(1.1F, 1.1F, false);

    /** True when the body is unchanged and nothing needs doing. */
    public boolean isNatural() {
        return this.width == 1.0F && this.height == 1.0F;
    }
}
