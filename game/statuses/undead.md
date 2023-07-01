---
title: Undead
---

# {{page.title}}
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Undead** is a status.

| **Alignment** | Bad |
| **Class** | Healing Modifier: Healing Mitigator |
| **Boss Immune** | No |

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

**Undead \[n\]**: If the affected would gain HP, their HP is decreased by up to **n** instead. If **n** is not specified, there is no limit on how much the affected's HP can be decreased by. If the affected has multiple **Undeads**, evaluate only the **Undead** with the highest potency during damage calculations.

---

## Development

Undead / Zombie was added in early v1 with the effect of taking damage when healed. It was given then extra interactions with Poison, Burn, and Vampire, though those effects were removed to reduce overloading statuses with too many effects. The Zombie name was removed later on. In order to weaken the effect to allow more players to use it, the status was given a variable cap on the amount of damage it can deal.

---

## Origin

Zombies are undead creatures in popular media. In games with damage types, they tend to be weak against fire and holy (healing) and resistant or immune to poison. Final Fantasy in particular has a Zombie status effect that applies the Undead damage interactions to a unit.

---

## History

| Version | Changes |
| :---: | --- |
| [4.7.0](v4#v4.7.0) | Classified as Healing Modifier: Healing Mitigator. |
| [4.5.2](v4#v4.5.2) | Now has an optional damage limit. |
| [1.6.13](v1#v1.6.13) | Zombie was removed as an alias. |
| [1.6.8](v1#v1.6.8) | Now deals true damage instead of subtracting HP. True damage does not have an official definition at this point but defines it as damage that cannot be reduced by means that aren’t Mitigator. |
| [1.6.7](v1#v1.6.7) | Now subtracts HP instead of dealing damage. |
| [1.4.13](v1#v1.4.13) | Status order switched to Zombie / Undead. Now considered a bad status. |
| [1.3.3](v1#v1.3.3) | No longer interacts with Poison / Burn or Vampire. |
| [1.3.0](v1#v1.3.0) | Now considered a weird status. |
| [1.2.5](v1#v1.2.5) | Now overwritten by Vampire. |
| [1.2.2](v1#v1.2.2) | Now negates [Poison](dot) damage and doubles [Burn](dot) damage. |
| [1.2.0](v1#v1.2.0) | Undead / Zombie was added with the effect: `Healing magic hurts you.` |