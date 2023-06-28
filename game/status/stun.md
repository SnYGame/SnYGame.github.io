---
title: Stun / Freeze
layout: "status"
parent: Statuses
grand_parent: Gameplay Documentation
---

# Stun / Freeze
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Stun** / **Freeze** is a status.

| **Alignment** | Bad |
| **Class** | Action Modifiers: Crowd Control |
| **Boss Immune** | Yes |
| **Other Names** | Slow, Paralysis, Paralyzed, Paralyze |

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

**Stun** / **Freeze [n%]**: The affected has an **n**% chance for their current move to be skipped. **Quick Effects** cannot be used until their next move.

---

## Development

Both Stun, Freeze, and Slow / Paralysis were added some time during v0, all with the same effect of preventing actions. Stun had a duration of 1 to 3 turns while Freeze and Slow / Paralysis had a duration of 5 turns. Slow / Paralysis only had a 50% chance of triggering. Stun, Freeze, and Paralysis were merged into one status while Slow gained a new effect. Freeze also temporarily gained a new effect as an alias as Petrify. Paralysis and its variations were eventually removed as an alias, leaving only Stun and Freeze.

---

## Origin

Stun, freeze, and paralysis are common statuses effects found in RPGs. Units under these effects have a chance to not be able to act. The slow effect in games typically slows down movement, but in some turn based games, it may instead lower hit rate or reduce the amount of moves that can be used.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](/game/changelog/v4.html#v4.8.0) | Now skips moves and prevents usage of Quick Effects. |
| [4.7.0](/game/changelog/v4.html#v4.7.0) | Classified as Action Modifiers: Crowd Control. |
| [4.6.0](/game/changelog/v4.html#v4.6.0) | Bosses are now immune to Stun / Freeze. |
| [1.6.13](/game/changelog/v1.html#v1.6.13) | Paralyze was removed as an alias. |
| [1.6.5](/game/changelog/v1.html#v1.6.5) | Now had a default activation chance of 100%. |
| [1.6.1](/game/changelog/v1.html#v1.6.1) | Freeze was merged with Stun / Paralyze. |
| [1.3.4](/game/changelog/v1.html#v1.3.4) | The [1.3.3](/game/changelog/v1.html#v1.3.3) changes to Freeze were reverted. |
| [1.3.3](/game/changelog/v1.html#v1.3.3) | Freeze was given a [new effect](/game/status/petrify). |
| [1.3.0](/game/changelog/v1.html#v1.3.0) | Stun and Paralyzed (renamed to Paralyze) were merged and now allow for a variable activation chance. Freeze kept the original effect. They were now considered bad statuses. |
| [1.2.0](/game/changelog/v1.html#v1.2.0) | Statuses no longer have restricted durations. Stun and Freeze were merged. The Paralysis status was brought back with the new name of Paralyzed while Slow was given a new effect. |
| [1.0.1](/game/changelog/v1.html#v1.0.1) | Paralysis was removed as an alias for Slow. |
| [1.0.0](/game/changelog/v1.html#v1.0.0) | Stun, Freeze, and Slow / Paralysis were already in the game at the start of [v1.0.0](/game/changelog/v1.html#v1.0.0). Stun had the effect: `Makes a target be unable to act for 1 to 3 turns unless specified.` Freeze had the effect: `Makes a target be unable to act for 5 turns.` Slow / Paralysis had the effect: `Has a 50% chance of actually acting for the next 5 turns.` |

---

## See also

- Slow
- [Perfect Freeze](/game/status/perfectfreeze)
- [Petrify](/game/status/petrify)