---
title: Haste
---

# {{page.title}}
{: .no_toc}

<div class="row">
<div class="column content" markdown="1">

**Haste** is a status.

| **Alignment** | Good |
| **Class** | Action Modifier |
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

**Haste \[n%\]**: The affected gains **n** more actions at the start of their move (defaults to 100%). Values that do not result in 'whole' actions instead describe a chance for an additional action (e.g. **Haste [150%]** is one extra action plus a 50% chance for a second extra action).

---

## Development

Haste was added some time in v0 with the effect of letting the affected unit act twice for 1 to 3 turns. Like other statuses, this was changed to allow variable duration, along with activation chance later on. Due to ambiguity when gaining the status in the middle of the move, it was clarified to only activate at the start of the move by default.

---

## Origin

The Haste status effect in games often increases the speed of actions. In games with a discrete turn system, it may instead increase the amount of actions that can be done in a single turn.

---

## History

| Version | Changes |
| :---: | --- |
| [4.9.0](v4#v4.9.0) | Now triggers at the start of the move. |
| [4.8.0](v4#v4.8.0) | Classified as Action Modifier. |
| [4.7.0](v4#v4.7.0) | Classified as Action Modifiers / Crowd Control Effects. |
| [4.1.2](v4#v4.1.2) | Now allows for activation chances greater than 100%, where each 100% is a guaranteed extra action. |
| [3.0.5](v3#v3.0.5) | Activation chance defaults to 100%. |
| [3.0.1](v3#v3.0.1) | Now allows for a variable activation chance. |
| [1.4.10](v1#v1.4.10) | No longer affected by [Sleep](sleep). |
| [1.3.1](v1#v1.3.1) | No longer takes effect if [Sleep](sleep) is active. |
| [1.3.0](v1#v1.3.0) | Now considered a good status. |
| [1.2.0](v1#v1.2.0) | Statuses no longer have restricted durations. |
| [1.0.0](v1#v1.0.0) | Haste was already in the game at the start of [v1.0.0](v1#v1.0.0). It had the effect: `Acts twice in a single turn for 1 to 3 turns.` |