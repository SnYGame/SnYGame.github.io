---
title: Command Block
---

# {{page.title}}
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Command Block** is a status.

| **Alignment** | Bad |
| **Class** | Action Modifiers: Crowd Control |
| **Boss Immune** | Yes |
| **Other Names** | Guard Break, Silence, Blocked, Blind |

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

**Command Block**: The affected cannot perform the specified command. **Spell Block** may be referred to as **Silence**. **Guard Block** may be referred to as **Guard Break**. If the affected has replaced the specified command with something else (e.g. through their passive), the replacement cannot be performed instead.

---

## Development

Guard Break and Silence were added some time in v0, with the current effect of preventing usage of Defend (called Guard at the time) and Spells. Blocked was added as an equivalent for the Attack command, though all three had a different range of allowed durations. Blocked was later renamed to Blind and given an extra effect of having a 25% chance for Spells to fail, which was later increased to 50%. In [1.6.1](v1#v1.6.1), Blind was then changed to have a chance to fail instead, but the status returned in [1.7.1](v1#v1.7.1) as Attack Block when all three were generalized as the Command Block status.

---

## Origin

Guard Break (or Guard Crush) is based on fighting games where attacks are able to hit through a guard. This specific effect was inspired by [Immaterial and Missing Power](https://en.touhouwiki.net/wiki/Immaterial_and_Missing_Power), where a Guard Crush would instantly drain the fighter's spirit and weaken blocks. Silence is a common status in games that prevents casting spells or other actions that require speech. Blocked has no origin from any other sources. Blind is a common status effect used in games that reduces accuracy or prevents attacks from hitting. In some games this only affects physical attacks and have no effect on magic attacks.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](v4#v4.8.0) | Classified as Action Modifiers: Crowd Control. |
| [4.7.0](v4#v4.7.0) | Classified as Action Modifiers / Crowd Control Effects. |
| [4.6.0](v4#v4.6.0) | Bosses are now immune to Action Block. |
| [3.0.7](v3#v3.0.7) | Action Block now affects custom commands if the original was blocked. |
| [1.7.1](v1#v1.7.1) | Guard Break and Silence were merged into a generalized status called Action Block. |
| [1.6.1](v1#v1.6.1) | Blind was given a [new effect](blind). |
| [1.3.0](v1#v1.3.0) | Now considered a bad status. |
| [1.2.2](v1#v1.2.2) | Blind's chance to cause spellcards to not deal damage was increased to 50%. |
| [1.2.0](v1#v1.2.0) | Statuses no longer have restricted durations. |
| [1.1.2](v1#v1.1.2) | Blocked was renamed to Blind and now causes damaging spells to only have a 25% chance to deal damage. |
| [1.0.1](v1#v1.0.1) | Blocked was added with the following description: `The target is unable to attack for 1 to 5 turns.` |
| [1.0.0](v1#v1.0.0) | Guard Break and Silence were already in the game at the start of [v1.0.0](v1#v1.0.0). Guard Break had the effect: `Makes a target be unable to guard for 1 to 3 turns.` Silence had the effect: `Makes a target be unable to cast any sort of spellcard for the next 3 turns.` |

---

## See also

- [Blind](blind)
- Command Encore