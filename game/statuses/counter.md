---
title: Countercommand
---

# {{page.title}}
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Countercommand** is a status.

| **Alignment** | Good |
| **Class** | Command Modifier |
| **Boss Immune** | No |
| **Other Names** | Counterattack |

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

**Countercommand \[n%\]**: When the affected would be hit by an enemy effect, the affected has an **n**% chance to perform the specified command without using an action after the hit has been registered. If **Counter** does not specify a command, the affected can choose which command to use. Commands that may target the effect’s source must do so - a **Counterattack** must target the enemy that hit you.

---

## Development

Counterattack was added to allow the affected unit to attack an enemy that hit them for extra damage. Later, it was given a variable activation chance. The extra damage was removed to reduce the amount of things that a single status would do. After that, it was generalized to allow the countering with any commands.

---

## Origin

A counterattack in games is an attack done in response to getting attacked. This is sometimes done automatically or with manual input after a dodge or parry. In some cases, counterattacks will do more damage than a normal attack.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](v4#v4.8.0) | Generalized to Countercommand to allow countering with any command. Classified as Command Modifier. |
| [4.7.0](v4#v4.7.0) | Classified as Action Modifiers / Crowd Control Effects. |
| [2.0.2](v2#v2.0.2) | No longer deals increased damage. |
| [1.4.8](v1#v1.4.8) | Now deals 1d30 damage instead of extra damage. |
| [1.3.1](v1#v1.3.1) | Now allows for a variable activation chance. |
| [1.3.0](v1#v1.3.0) | Now considered a good status. |
| [1.2.1](v1#v1.2.1) | Spread Amulets was added with the effect: `When hit successfully, will counterattack with extra damage.` |