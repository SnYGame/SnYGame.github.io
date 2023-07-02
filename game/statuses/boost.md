---
title: Command Boost
---

# {{page.title}}
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Command Boost** is a status.

| **Alignment** | Situational |
| **Class** | Triggered Effect: When Acting |
| **Boss Immune** | No |
| **Other Names** | Sword, Enchantment, Enhancement, Blockade, Supercharge, Revival, Enchant |

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

**Command Boost \[X\]**: When the affected performs Command, **X** is also applied to the targets of Command. **X** is applied after the Command is processed. **Attack Boost \[X\]** may be referred to as **X Sword**. **Spell Boost \[X\]** may be referred to as **X Enchant**. **Defend Boost \[X\]** may be referred to as **X Blockade**. **Concentrate Boost \[X\]** may be referred to as **X Supercharge**. **Extend Boost \[X\]** may be referred to as **X Revival**.

---

## Development

Sword was added to cause basic Attacks to have a chance apply status effects. Initially the chance was 25% with the potency field indicating the duration of the applied status before changing to be the variable activation chance. Enchantment was added as an alias later on, but was later changed to trigger on Spells instead of Attack. These were later generalized as Command Enhancement and the corresponding names for the other commands are Blockade, Supercharge, and Revival for Defend, Concentrate, and Extend. To avoid confusion between Enhancement and Enchantment, Enhancement was renamed to Boost and Enchantment was renamed to Enchant.

---

## Origin

The Sword status was inspired by the [Elemental Saber Spells](https://mana.fandom.com/wiki/Elemental_Saber_Spells) from the Mana series, which granted extra effects to weapon attacks. Enchantment, Enhancement, Blockade, Supercharge, Revival, and Enchant do not have any inspiration from other games.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.2](v4#v4.8.2) | Enhancement was renamed to Boost. Enchantment was renamed to Enchant. |
| [4.8.0](v4#v4.8.0) | Guard / Charge / Extend Enhancement \[X\] may now be referred to as X Blockade / Supercharge / Revival. Classified as Triggered Effect: When Acting. |
| [4.7.0](v4#v4.7.0) | Classified as both Triggered Effects: When Hitting and Action Modifiers / Crowd Control Effects. |
| [4.1.3](v4#v4.1.3) | Sword / Enchantment were readded to be shorthand for Attack / Spell Enhancement \[X\]. |
| [4.1.2](v4#v4.1.2) | Sword and Enchantment was merged into a generalized status called \[Action\] Enhancement \[X\]. There is no longer a variable activation chance. |
| [4.0.2](v4#v4.0.2) | Sword and Enchantment were separated into separate statuses. Enchantment now only triggers on Spells. |
| [3.0.3](v3#v3.0.3) | Description now specifies that the status is applied after the attack. |
| [1.6.1](v1#v1.6.1) | No longer has a parameter for the status duration. Now considered a situational status. |
| [1.4.0](v1#v1.4.0) | Now has a new parameter d for the duration of the status inflicted. |
| [1.3.0](v1#v1.3.0) | Enchantment was added as an alias. Now considered a good status. |
| [1.2.1](v1#v1.2.1) | X Sword \[n\] was added with the effect: `On normal attacks, has 25% chance of inflicting a specified status effects for n turns.` It was changed on the same day to have n be the activation chance instead. |

---

## Trivia

- X Sword \[n\] was the first status to have two variables.
- X Sword / X Enchantment \[n, d\] was the first status to have three variables.