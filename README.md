# BuildRx | Engineering Portfolio

**MABRIG Technologies — AI-assisted software development**

[Explore BuildRx](https://www.buildrx.online) · [Developer profile](https://github.com/mabrig1) · [Contact](https://www.mabrigkorie.org)

BuildRx addresses the challenge of moving from an app idea to an editable software project through AI-assisted planning, implementation, preview and publishing workflows.

## Engineering competencies

| Area | Project focus |
|---|---|
| AI engineering | Multi-stage agent-assisted workflows and provider abstraction |
| Full-stack development | Next.js, React, TypeScript |
| Data and cloud | Supabase, MongoDB Atlas, Cloudflare R2 |
| Developer experience | Browser editing, project files and previews |
| Software quality | Validation, controlled publishing and failure handling |

## Explore the portfolio

- [Engineering case study](docs/case-study.md)
- [Conceptual system architecture](docs/architecture.md)
- [Standalone release-gate example](demo/release_gate.py)
- [Example automated tests](demo/test_release_gate.py)
- [CI workflow](.github/workflows/demo.yml)

Run the independent Python demonstration locally (Python 3.10+; no keys or dependencies):

```sh
python demo/release_gate.py
python -m unittest discover -s demo -v
```

## Evidence and scope

The technical stack and product capabilities are described in the production project's documentation. They are not represented as independently verified live functionality or performance metrics. The example demonstrates fail-closed release decisions using synthetic evidence; it is not extracted from the production engine.

## Technical interviews and collaboration

Recruiters may request a guided product demonstration or a scoped technical review via the contact website. Proprietary internals, credentials and customer data are excluded from this showcase.

## Intellectual property

See [NOTICE.md](NOTICE.md). This repository is a public portfolio, not a release of the commercial BuildRx source code.
