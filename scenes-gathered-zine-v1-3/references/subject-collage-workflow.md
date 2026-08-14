# Subject-led collage workflow

Read this reference for every image transformation. It contains the detailed rules behind the short control plane in `SKILL.md`.

## Scene Card

Before prompting, record:

- **Core subject:** the 1–2 forms that make the image identifiable and carry the visual weight.
- **Joint subject:** forms that must stay together because their relationship is the subject, such as a building and bridge, a mural and chair row, or a person and the object being used.
- **Supporting context:** only the 2–3 environmental elements needed for scale, attachment, grounding, direction, or place.
- **Spatial invariants:** relative position, overlap, scale, perspective, horizon, path, silhouette, and dominant gesture.
- **Visual weight:** area, darkness, saturation, texture, isolation, edge tension, and subject contrast.
- **Native colors:** dominant hue family, temperature, value range, saturation, and meaningful minor colors.
- **Source contours:** silhouettes, structural edges, shadows, rhythms, or color boundaries that can continue into paper.
- **Semantic minimum:** the smallest set of subject forms and relationships that still identifies this particular photo.

Treat the photo as factual evidence. Treat paper and illustration as an interpretation of that evidence.

## Semantic subject mask

The semantic subject mask controls the photo crop, torn boundary, paper extension, color placement, and eye path.

1. Select the core subject before selecting the canvas. Do not infer the subject from the largest visible area.
2. Keep a joint subject in one mask when the relationship is aesthetically or semantically essential. A mural without its chair row, or a building without its bridge, may lose the point of the image.
3. Add a minimal context halo, normally 3–12% around the subject envelope, only to show scale, attachment, grounding, or direction.
4. Exclude low-information ceiling, floor, sky, blank wall, room edges, signs, and incidental foreground unless they are part of the semantic minimum.
5. Use a narrow grounding strip when feet, chair legs, wheels, foundations, or shadows need contact with the scene. Do not keep an entire floor just because it is visible.
6. Use a narrow sky, wall, or horizon strip only when it explains the subject's placement. Do not keep a large empty region as automatic padding.
7. The boundary must follow real subject contours: outer silhouette, overlap, attachment line, bench line, roofline, shoreline, path, or structural edge. A rectangular crop is not a subject boundary.
8. Keep the subject measured and readable at thumbnail size. If it is too large, remove incidental edges and low-value context; if it is too small, enlarge the subject-derived contour rather than adding environment.
9. When the first reading of the result is “room,” “sky,” “floor,” or “background,” rebuild the mask before changing color or texture.

## Orientation and allocation

- Preserve portrait, landscape, or square orientation and the source's approximate aspect feeling. Do not default to vertical 3:5, rotate the source, or force a landscape scene into a portrait poster.
- Start with photographic subject content at roughly 55–80% of the final image when the source subject depends on color and detail. Use 45–70% only when a smaller subject and stronger paper intervention are clearly justified.
- Keep paper and graphic interventions at roughly 20–45% of the final image. Keep low-activity breathing space normally within 10–30%, but do not leave a broad paper zone visually dead or perfectly solid; paper grain alone is not a line transition.
- Let photo fragments be one main fragment or two overlapping fragments. Every fragment must contain core subject information.
- Correct the allocation by visual weight, not by hitting a percentage. A dark mural or large building may need less area than a pale sky even when their pixel areas are equal.
- Keep paper active around the subject, but do not let the paper, border, or added hue become the focal subject.

## Abstraction and contour provenance

Choose one primary grammar and at most one supporting grammar:

- **Silhouette-led:** one broad mass for strong profiles, buildings, roofs, trees, or figures.
- **Contour-led:** a few broken structural lines for architecture, paths, gestures, and edges.
- **Field-led:** one restrained field for atmosphere, ground, water, haze, or shadow.
- **Rhythm-led:** sparse repeated marks for chairs, posts, windows, waves, steps, or branches.
- **Cut-paper-led:** one or two simplified source shapes for strong organic or geometric hierarchies.

For every structural paper mark, answer: “Which visible subject contour, silhouette, shadow, rhythm, or color boundary does this come from?” Delete or simplify the mark if the answer is unclear. In a broad paper zone with no usable subject contour, a secondary fallback line is allowed only to make a natural transition: keep it sparse, irregular, curved or broken, varied in pressure, and clearly subordinate to the photo.

- Preserve no more than 1–2 defining forms or relationships in each illustrated section.
- Merge repeated detail into large masses or sparse directional gestures. Dense detail in the photo is a reason to simplify the paper layer, not to print more.
- In foliage, vines, or intricate patterns, remove most leaves, fine twigs, tiny curls, cells, and repeated marks; keep the source-specific lean, opening, overlap, or direction.
- Paper extensions may cross the photo seam, but they must remain attached to or visibly continued from the subject.
- Do not fill empty corners with dense generic linework, repeated decorative arcs, pattern fields, arbitrary halftone patches, or unrelated botanical forms. If an empty corner would otherwise read as a dead solid field, add only a few quiet transition curves or broken strokes as fallback filler; do not make a pattern, symbol, frame, or new subject.

## Paper-field activation

- Inspect every broad paper zone after the subject mask is set. A textured paper field may stay quiet, but it must not become a visually dead solid block.
- First extend the source's visible structural language: rooflines, cables, branches, folds, paths, chair rhythms, window verticals, shadows, water ripples, or color boundaries.
- If a zone has no readable source structure, use a small amount of natural random filler: asymmetrical curves, broken parallel strokes, offset fragments, and pressure variation. Keep the density low and the marks separate from one another.
- Do not let fallback filler touch the photographic subject as if it were a new object, overpower the subject, form lettering, or become a repeated wallpaper pattern. Remove it if it changes the first reading from the subject to the paper.

## Photo-to-paper boundary

- Make the primary transition a visibly hand-torn, asymmetric contour that follows the semantic subject envelope.
- Use a narrow exposed-fiber fringe, slight abrasion, broken emulsion, and flat scan behavior; avoid lifted-paper depth and heavy shadows.
- Let the tear affect roughly 35–70% of the visible photographic perimeter, varying pressure and contour rather than making a uniform frame.
- Use speckles, crumbs, or ghost marks only at one or two pressure points and only when they support the subject boundary.
- Use neutral off-white or very lightly warm paper. The paper tone belongs to the paper sections and must not become a global photo filter.

## Photographic color protection

- Treat the selected photographic subject as color-locked: preserve white balance, saturation, contrast, local color relationships, texture, and material cues.
- Never apply a global yellow, sepia, cream, faded, or vintage wash to make photo and paper match.
- Create visual conflict through juxtaposition: high-fidelity photo against neutral paper, charcoal/black contours, and one localized structural hue.
- Keep the added hue outside the photo, at the seam, or in a clearly source-derived underprint. It may intensify a source color but may not cover, muddy, or repaint the subject.
- Use the lower end of the added-hue area range when the photo already contains vivid reds, blues, greens, or other strong colors.
- Choose one integration mode only: source continuation, selective replacement, underprint passage, counterform, or directional rhythm. The hue must touch or cross the subject and change balance, movement, figure-ground, continuity, or meaning.
- Do not use a detached rectangle, corner patch, generic circle, isolated brush swatch, arbitrary bright dot, or color added after the composition is solved.

## Text suppression

- Default output contains no generated words, keywords, micro-text, captions, labels, dates, metadata, logos, watermarks, social handles, pseudo-writing, or decorative symbols.
- Ignore text and watermarks present in style references; do not copy them.
- Preserve unavoidable source signage only as subordinate photographic context when removing it would damage the supplied scene. Do not sharpen, translate, or add signage.
- If the user explicitly supplies exact text, reproduce only that text and no subtitle, attribution, or extra copy.

## Prompt compiler

Compile four compact paragraphs:

1. **Subject, canvas, and attention geometry:** semantic mask, joint-subject relationship, context exclusions, source orientation, subject scale, photo/paper allocation, and eye path.
2. **Scene fidelity:** core forms, spatial invariants, native colors, and exactly what stays photographic.
3. **Contour collage, color, and boundary:** source contours to retain/merge/omit/transform, one primary grammar, contour provenance, one hue and its integration mode, subject-following tear, and explicit no-text policy.
4. **Reproduction and avoids:** neutral paper, flat scan, color protection, mood, subject hierarchy, and hard avoids.

Use decisive visible-pixel instructions. Do not put analysis notes, file paths, metadata, or design theory in the final generation prompt.

## Targeted correction

Regenerate at most once, changing only the observed failure:

- **Orientation error:** restore the source orientation and approximate aspect feeling.
- **Weak subject:** rebuild the semantic mask and remove low-information context.
- **Subject too large:** remove incidental subject edges and context; do not add blank paper.
- **Subject too small:** enlarge the subject-derived contour or main photographic fragment without adding environment.
- **Context dominance:** remove ceiling, floor, sky, blank wall, room edges, or signage that compete with the subject.
- **Arbitrary line fill:** delete dense, decorative, or repeated marks that cannot be traced to the subject; sparse fallback transition lines are allowed only in otherwise dead paper.
- **Dead paper field:** extend subject contours first; if no contour is available, add sparse irregular transition curves or broken strokes, then reduce density until the paper remains subordinate.
- **Global color wash:** restore photographic white balance, saturation, contrast, and material texture.
- **Decorative color:** attach the hue to a source contour or seam and reduce its area if it competes with the subject.
- **Text failure:** remove all generated text unless exact user wording was supplied.
- **Damaged photography:** restore natural perspective, color, texture, and recognizable subject detail.

## Final quality gate

Before returning, confirm:

- input orientation is preserved;
- the semantic subject and joint-subject relationships read immediately at thumbnail size;
- low-information context is excluded or limited to a minimal halo/grounding strip;
- photographic subject color and texture are truthful and not globally tinted;
- structural paper marks are source-derived; fallback transition marks are sparse, natural, and limited to otherwise dead paper;
- the torn boundary follows the subject envelope and remains tactile but subordinate;
- broad paper zones contain restrained structural extensions or fallback transition marks rather than visually dead solid space;
- fallback marks are sparse, natural, non-repeating, and do not become a new subject;
- the added hue is singular, localized, source-derived, and structurally useful;
- no generated text, watermark, metadata, logo, or pseudo-writing is present by default;
- the output is a flat, tactile, non-commercial collage with no glossy, 3D, or cinematic treatment.
