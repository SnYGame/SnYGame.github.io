---
title: Blind
---

# {{page.title}}
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

**Blind \[n%\]**: When the affected would perform a command on a different team, there is an **n**% chance that it will not be received by the specified target. Roll for **Blind** once per hit performed.

---

## Development

In [1.1.2](v1#v1.1.2), [Blind](block) was introduced as a status that prevents Attacks and had a chance for damaging spells to fail. Since Blind already existed at the time, Failure was added as the inverse of Evasion instead, that causes attacks to have a chance of failing, though Evasion had a fixed potency of 50% at the time. Failure was later changed to only affect the Attack and Guard command before getting removed without seeing any use. In [1.6.1](v1#v1.6.1), Blind was changed to have the original effect of Failure, though it now specifies that it affects offensive commands rather than attacks.

---

## Origin

Failure has no origin from any other sources. Blind is a common status effect used in games that reduces accuracy or prevents attacks from hitting. In some games this only affects physical attacks and have no effect on magic attacks.

---

## History

| Version | Changes |
| :---: | --- |
| [4.8.0](v4#v4.8.0) | Now affects all commands that affect enemies. |
| [4.7.0](v4#v4.7.0) | Classified as Trigger Modifier. |
| [4.6.0](v4#v4.6.0) | Bosses are now immune to Blind. |
| [1.6.5](v1#v1.6.5) | Blind was given a default activation chance of 100%. No longer overwrites [Berserk](berserk). |
| [1.6.1](v1#v1.6.1) | Blind's effect was changed to the original Failure effect, but affecting all offensive commands. |
| [1.3.1](v1#v1.3.1) | Now overwrites [Berserk](berserk). |
| [1.3.0](v1#v1.3.0) | Failure was removed. |
| [1.2.10](v1#v1.2.10) | Failure can now also cause Guard to fail. |
| [1.2.8](v1#v1.2.8) | Failure [n] was added with the following description: `Attacks done by the target have a n% chance to miss.` |

---

## See also

- [Command Block](block)
- Evasion