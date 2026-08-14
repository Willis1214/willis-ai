---
name: scenes-gathered-zine-v1-3
description: "Transform a supplied photo into a source-faithful tactile paper collage preserving orientation, aspect feeling, semantic subject boundaries, and colors. Use for photo-plus-paper collage with hand-torn seams, subject-derived contour or halftone extensions, and restrained natural transition lines; keep the photo dominant, activate broad blank paper with structure-first lines and sparse fallback curves, and add no generated text, captions, metadata, logos, or watermarks. Do not use for text-led posters, global filters, or arbitrary decorative pattern fill."
---

# 拾景纸刊 · Subject-led Gathered Scenes Zine

Transform a supplied photo into a calm, tactile collage where the factual photograph remains the visual anchor and paper, contour, halftone, and one localized structural hue create a controlled visual conflict.

Read [`references/subject-collage-workflow.md`](references/subject-collage-workflow.md) before every generation. It contains the detailed subject-mask, allocation, color, boundary, text, correction, and quality rules.

## Use when

- The user wants a real photo combined with torn paper, source-derived contours, halftone, cut-paper, or restrained print texture.
- The user wants the source scene and its main subject to remain recognizable and color-faithful.
- The user wants a flat, non-commercial collage poster or page-like image.

Do not use for a text-led poster, a global photo filter, a generic illustration unrelated to a supplied photo, or arbitrary decorative pattern filling. Treat the supplied photo as the only source unless the user supplies additional references.

## Core contract

- Preserve the input orientation and approximate aspect feeling. Portrait stays portrait; landscape stays landscape; square stays square. Do not default to vertical 3:5.
- Define a semantic subject mask before choosing the layout. A joint relationship can be one subject unit, such as a mural plus its chair row or a building plus its bridge.
- Keep only a minimal context halo for scale, attachment, grounding, or direction. Exclude low-information ceiling, floor, sky, blank wall, room edges, signage, and incidental clutter by default.
- Let the photo remain visually dominant, normally about 55–80% of the final image when color and detail matter. Keep low-activity paper controlled, normally about 10–30%; paper grain alone does not count as a transition, and no broad paper field should read as untouched solid space.
- Make photo fragments and torn boundaries follow the subject's real silhouette, overlap, attachment line, bench line, roofline, shoreline, path, or other structural contour. A rectangular crop is not a subject boundary.
- Preserve photographic white balance, saturation, contrast, material texture, perspective, and meaningful local colors. Never apply a global yellow, sepia, cream, faded, or vintage wash.
- Use one primary illustration grammar and at most one supporting grammar. Structural marks must trace or continue a visible subject contour, silhouette, shadow, rhythm, or color boundary.
- Activate broad paper fields in two levels: extend the subject's real structure first; when no usable structure exists, allow a small amount of low-density, irregular, natural curved or broken random filler to make a transition. Filler must stay subordinate and must not become a repeated pattern, symbol, or new subject.
- Use one localized added hue only. Keep it at the seam, outside the photo, or in a clearly source-derived underprint; never let it repaint or muddy the photographic subject.
- Use neutral off-white or very lightly warm paper, flat scan behavior, matte fibers, restrained grain, and no artificial 3D depth.
- Add no generated words, keywords, captions, dates, metadata, logos, watermarks, social handles, pseudo-writing, or decorative symbols by default. Honor only exact text explicitly supplied by the user.

## Subject boundary gate

Before prompting, answer these questions:

1. What 1–2 forms carry recognition and visual weight?
2. Which forms must stay together because their relationship is the subject?
3. What is the smallest context halo needed to show scale, attachment, grounding, or direction?
4. Which visible areas are merely background and must be removed?
5. Which real contours can define the photo edge and continue into paper?

If the first reading of the result is “room,” “sky,” “floor,” or “background,” rebuild the mask. If a structural paper line cannot be traced to the selected subject, replace it with restrained fallback transition filler only when the surrounding paper would otherwise read as dead flat.

## Workflow

1. Inspect the supplied photo and build a Scene Card: core subject, joint subject, spatial invariants, dominant gesture, visual weight, native colors, source contours, and semantic minimum.
2. Build the semantic subject mask and minimal context halo. Set explicit exclusions before choosing a canvas or crop.
3. Lock orientation and approximate aspect feeling to the source. Allocate photo, paper, and context by visual weight rather than a fixed poster template.
4. Choose one primary illustration grammar: silhouette-led, contour-led, field-led, rhythm-led, or cut-paper-led.
5. Build the abstraction map: retain defining forms, merge repeated detail, omit clutter, transform only source-derived shapes, and expose controlled paper.
6. Choose one source-derived hue and one integration mode. Apply the structural-removal test: removing the hue must weaken balance, movement, figure-ground, continuity, or meaning.
7. Build the hand-torn boundary around the semantic subject envelope. Activate broad paper zones with subject structure first, then sparse natural fallback curves or broken strokes where no structure is available; keep all marks subordinate.
8. Apply the text-suppression rule. Preserve unavoidable source signage only as subordinate context; add nothing new unless exact user text was supplied.
9. Compile four concise prompt paragraphs: subject/canvas/attention, scene fidelity, contour collage/color/edge/text policy, and reproduction/avoids.
10. Generate with the supplied photo as reference. Inspect at normal and thumbnail scale, then regenerate at most once for one targeted failure.

## Output contract

Return the generated image plus one brief Chinese creative rationale describing the selected subject boundary, source-derived paper extension, and structural role of the added hue. Do not reveal the full generation prompt or turn the rationale into a parameter checklist unless the user asks.

Do not save source or generated images into project files unless the user asks. Do not browse, share, commit, or upload the supplied source material elsewhere.

## Quality gate

Before returning, verify:

- orientation and approximate aspect feeling are preserved;
- the semantic subject and any joint-subject relationship read immediately at thumbnail size;
- low-information context is excluded or limited to a narrow useful halo/grounding strip;
- the photographic subject remains high-fidelity, naturally colored, and not globally tinted;
- structural paper marks and added hue are traceable to the subject; fallback linework appears only in otherwise dead paper, remains sparse and natural, and does not fill areas arbitrarily;
- the torn edge follows the subject envelope and remains tactile but subordinate;
- broad paper zones are not visually dead or perfectly solid, and line density does not turn the paper field into the focal subject;
- no generated text, watermark, metadata, logo, or pseudo-writing is present by default;
- the result is flat, tactile, source-derived, non-commercial, and free of glossy, 3D, cinematic, or generic decorative treatment.

For failure correction, use the targeted correction table in [`references/subject-collage-workflow.md`](references/subject-collage-workflow.md). 
