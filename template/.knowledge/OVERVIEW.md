# Overview — <project>

*The platform in plain language — written for product, marketing and anyone new, not for developers. What
the parts are and how something moves through them. Follow a link to learn what a part guarantees.*

## The platform

<A diagram of the real shape of the system — the parts a person would name, and what flows between them.
Draw what matters, not everything: if a box has no bearing on how the platform behaves, leave it out.>

```mermaid
flowchart LR
  subgraph Group["<a layer, named as the business names it>"]
    A["<a part>"] --> B["<the next part>"]
  end
  B --> C["<something not built yet>"]
  classDef planned stroke-dasharray: 4 3;
  class C planned;
  %% use ·partial and a second classDef for components that half-exist
```

## How it works

<Every component on the diagram, in the order things flow through them. **One short line each** — what it
is and what it hands on. A reader should scan the whole list in under a minute and understand the flow.
Link each to its contract; anything living in `prd-drafts/` is planned rather than live.>

- **<Component>** — <what it is, in a dozen words>. [contract](./prd/<file>.md)
- **<Component>** — <what it is>. *Planned.* [contract](./prd-drafts/<file>.md)

## What governs it

<The rules that decide what is allowed to happen, and who sets them — the terms both sides agreed, the
limits, the obligations that pause things when unmet. A stakeholder can watch a demo and learn the flow;
they cannot see the governance, which is why it is written here. One line each, linked.>

- **<The rule>** — <who sets it, and what it prevents>. See [`prd/<file>.md`](./prd/<file>.md).

---
*Editing this file? Follow the standard first: [`guides/docs-overview.md`](./guides/docs-overview.md).*
