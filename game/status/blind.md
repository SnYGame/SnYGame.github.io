---
title: Blind
layout: "status"
parent: Statuses
grand_parent: Gameplay Documentation
---

# Blind
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Blind** is a status.

| **Alignment** | Bad |
| **Class** | Trigger Modifier |
| **Boss Immune** | Yes |
| **Other Names** | Failure |

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

**Blind [n%]**: When the affected would perform a command on a different team, there is an **n**% chance that it will not be received by the specified target. Roll for **Blind** once per hit performed.

---

## Development

In [1.1.2](/game/changelog/v1.html#v1.1.2), [Blind](/game/status/block) was introduced as a status that prevents Attacks and had a chance for damaging spells to fail. Since Blind already existed at the time, Failure was added as the inverse of Evasion instead, that causes attacks to have a chance of failing, though Evasion had a fixed potency of 50% at the time. Failure was later changed to only affect the Attack and Guard command before getting removed without seeing any use. In [1.6.1](/game/changelog/v1.html#v1.6.1), Blind was changed to have the original effect of Failure, though it now specifies that it affects offensive commands rather than attacks.

---

## Origin

Failure has no origin from any other sources. Blind is a common status effect used in games that reduces accuracy or prevents attacks from hitting. In some games this only affects physical attacks and have no effect on magic attacks.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](/game/changelog/v4.html#v4.8.0) | Now affects all commands that affect enemies. |
| [4.7.0](/game/changelog/v4.html#v4.7.0) | Classified as Trigger Modifier. |
| [4.6.0](/game/changelog/v4.html#v4.6.0) | Bosses are now immune to Blind. |
| [1.6.5](/game/changelog/v1.html#v1.6.5) | Blind was given a default activation chance of 100%. No longer overwrites [Berserk](/game/removed/berserk). |
| [1.6.1](/game/changelog/v1.html#v1.6.1) | Blind's effect was changed to the original Failure effect, but affecting all offensive commands. |
| [1.3.1](/game/changelog/v1.html#v1.3.1) | Now overwrites [Berserk](/game/removed/berserk). |
| [1.3.0](/game/changelog/v1.html#v1.3.0) | Failure was removed. Blind was now considered a bad status. |
| [1.2.10](/game/changelog/v1.html#v1.2.10) | Failure can now also cause Guard to fail. |
| [1.2.8](/game/changelog/v1.html#v1.2.8) | Failure [n] was added with the following description: `Attacks done by the target have a n% chance to miss.` |
| [1.2.2](/game/changelog/v1.html#v1.2.2) | Blind's chance to cause spellcards to not deal damage was increased to 50%. |
| [1.2.0](/game/changelog/v1.html#v1.2.0) | Statuses no longer have restricted durations. |
| [1.1.2](/game/changelog/v1.html#v1.1.2) | Blocked was renamed to Blind with the following description: `The target is unable to attack for 1 to 5 turns. Spellcards which damage enemies have 25% chance to damage the enemy.` |

---

## See also

- [Command Block](/game/status/block)
- Evasion