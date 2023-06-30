---
title: Repel
layout: "status"
parent: Statuses
grand_parent: Gameplay Documentation
---

# Repel
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Repel** is a status.

| **Alignment** | Situational |
| **Class** | Target Modifier |
| **Boss Immune** | No |
| **Other Names** | Reverse Spellcard, Reflect |

</div>
<div class="column toc" markdown="1">
<details open markdown="block">
<summary>
Contents
</summary>
{: .text-delta }
1. TOC
{:toc}
</details>
</div>
</div> 

---

## Effect

**Repel X**: When the affected would be targeted by **X**, the effects that would be applied to the affected are instead applied to the source of **X**. If the affected is the source of **X**, do not evaluate **Repel**.

---

## Development

Reverse Spellcard was added some time in v0 with the effect of reflecting attacks or statuses back at the source. This was later renamed to Reflect and changed to affect only spell effects. Later on, the status was changed to Repel in order to generalize the types of effects that can be reflected.

---

## Origin

Reverse Spellcard reference [Seija Kijin](https://en.touhouwiki.net/wiki/Seija_Kijin)'s ability to turn over anything. Reflect is a status or spell in RPGs that reflect spell effects. The status was also called Repel in some Final Fantasy games.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](v4#v4.8.0) | Renamed to Repel X and can now specify what kinds of effects to reflect. Now considered a situational status. |
| [4.7.0](v4#v4.7.0) | Classified as Target Modifier. |
| [4.1.2](v1#v4.1.2) | The [1.4.10](v1#v1.4.10) were reverted. |
| [1.4.10](v1#v1.4.10) | Now affects special effects. |
| [1.3.1](v1#v1.3.1) | Now only affects spells. |
| [1.3.0](v1#v1.3.0) | Now considered a good status. |
| [1.1.1](v1#v1.1.1) | Renamed to Reflect. |
| [1.0.0](v1#v1.0.0) | Reverse Spellcard was already in the game at the start of [v1.0.0](v1#v1.0.0). It had the effect: `Makes a target backfires attacks back to their owner for 3 to 5 turns. Can also reverse status effects inflicted back to their owner.` |