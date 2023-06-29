---
title: Confused
layout: "status"
parent: Statuses
grand_parent: Gameplay Documentation
---

# Confused
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Confused** is a status.

| **Alignment** | Bad |
| **Class** | Action Modifiers: Crowd Control |
| **Boss Immune** | Yes |
| **Other Names** | Confuse |

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

**Confused**: If the affected can act, the command they perform must be chosen at random. All subsequent requirements for acting (choosing a spell if the **Spell** command is chosen, choosing a target/targets, etc.) are performed as normal.

---

## Development

Confuse or Confused was added some time during v0, causing the affected unit to randomly perform a basic command against a random target or casting an enemy spell based on the result of a 1d20. A later update changed how it interacts with Berserk with a chance to crit on a 20. It later had its effect changed to that of Dizzy due to the high variance nature of the effect until it was eventually removed. The status was brought back with a much simpler effect later in [4.8.0](v4#v4.8.0).

---

## Origin

Confuse, confused, or confusion is a status used in many games. Usually the effect randomizes movement or actions including a chance to use abilities or attacks on an unintended target.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](v4#v4.8.0) | Re-added with the current effect. |
| [1.6.11](v1#v1.6.11) | Removed. |
| [1.6.1](v1#v1.6.1) | Renamed to Confused and given the effect of Dizzy. |
| [1.3.1](v1#v1.3.1) | Description now clarifies that if the command is blocked by Blind, Silence, or Guard Break, the command will still fail. |
| [1.3.0](v1#v1.3.0) | Now considered a weird status. |
| [1.2.4](v1#v1.2.4) | Rolls now have different results when combined with Berserk:<br>`1 - 12 - Attacks an ally (or yourself)`<br>`13 - 19 -Attacks a random enemy`<br>`20 - Attacks a random enemy with 30 dmg.` |
| [1.0.0](v1#v1.0.0) | Confuse was already in the game at the start of [v1.0.0](v1#v1.0.0). It had the effect:<br>`Makes a target not perform the desired command for 1 to 3 turns.`<br>`1 - Attacks an ally (or yourself)`<br>`2 to 8 - Guard state`<br>`9 to 13 - Charges`<br>`14 to 19 - Attacks a random enemy`<br>`20 - Casts a spellcard which is not from your spellcard deck but from a boss.`<br>`The desired command will be replaced by "Nothing happens"` |

---

## See also

- Dizzy
- [Berserk](berserk)