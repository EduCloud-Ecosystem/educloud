# Self-hosted answer engines — evaluating Vane for the science lane

*2026-08-04. Assessed against the S3 Perplexity retirement, HB-1's SearXNG
plan, and the CC-P1 `verifier.science` profile. Conclusion: read it, don't
adopt it — and the reason clarifies what the science lane actually is.*

---

## 1. What Vane is

**Vane is Perplexica, renamed.** Same repository, same git history, same
author — the rename landed in commit `39c0f19` on 2026-03-09, and
`github.com/ItzCrazyKns/Perplexica` now redirects to `/Vane`. The 36k stars and
1,008 commits are inherited. It is not a successor project, and the XDA article
identifies this correctly.

Architecture: a single Next.js monolith. Classify query → SearXNG search →
Playwright scrape → embed and rank chunks in memory → LLM writes an answer with
inline `[n]` markers. SQLite for history, no vector store, MIT licensed.

## 2. Three disqualifying facts

**It is dormant.** Last commit on master: **2026-04-11**. Zero commits in
roughly four months, after 157 commits in December alone. The XDA article was
published 2026-08-02, four months after development stopped, and does not
mention this.

**It has no authentication, and that is not a missing feature — it is an open
key leak.** `GET /api/config` returns the full config verbatim, including every
provider API key in plaintext, with no auth and no redaction. Reported as issue
#1155 on 2026-06-26; no maintainer reply, no label, unassigned. The `POST` on
the same route accepts arbitrary config changes, and `POST /api/providers`
accepts arbitrary base URLs (SSRF). README's "Upcoming Features" lists
"Adding authentication" — unchecked.

Issue #1144, also unanswered: a user reports **a $3,000 OpenRouter bill** after
auto-video-search fired frontier calls unattended. On a machine holding a
LiteLLM master key and an OpenRouter key, this combination is not acceptable.

**It does not verify citations, and its prompt actively works against
grounding.** From `src/lib/prompts/search/writer.ts`:

> "Ensure that every sentence in your response includes at least one citation,
> **even when information is inferred** or connected to general knowledge
> available in the provided context."

That instruction manufactures citation pressure rather than checking support.
Nothing in the codebase tests whether source `[n]` entails the claim. The
project's own architecture doc is candid: *"We prompt the model to cite the
references it used. The UI then renders those citations alongside the
supporting links."*

Two smaller notes worth having on record: it ships a **privacy leak** —
`MessageSources.tsx` fetches favicons from `s2.googleusercontent.com`, sending
every retrieved source URL to Google from the user's browser, in a
privacy-focused product. And its whole pipeline depends on **strict structured
output** (`response_format: json_schema, strict: true`) in the classifier,
source picker, content extractor and widgets — a backend without strict schema
support breaks it rather than degrading it.

## 3. Why this does not replace Perplexity for us

Line P's S3 does not say "replace the Perplexity interface." It says:

> Perplexity retires when the **science lane's citation verifier** ships.

The thing being retired is not a search box. It is a claim about
trustworthiness. Vane provides Perplexity's *interface* without the property
that would justify the retirement — and its "cite every sentence, even when
inferred" prompt makes its citations *less* trustworthy than the product it
imitates, not more.

CC-P1 Step 3 already specifies what the retirement actually requires:

> `verifier.science` — every citation in the candidate resolves to a live
> document whose title matches, every rubric key in the context is present with
> a source, and every number is traceable to a fetched source or to included
> code. Emit `citation_resolvability` and `hallucinated_citation_rate` as
> evidence fields.

**Our roadmap is more demanding than Vane is.** That is the finding.

## 4. On model swapping — a correction

Vane's provider registry does allow multiple models configured and selected
per-request. That sounds like it helps, and it is the wrong layer.

Portage already does model swapping: `research_synthesis` has an ordered
failover group in the registry, and the LiteLLM router executes it. Letting a
search UI carry a second routing table above that would violate the
one-source-of-truth rule (`portage-scale-mapping` §4.4) and put model IDs in a
third place, against the two-manifest rule.

**Whatever surface we use should be pointed at one alias —
`research_synthesis` — and left to do no routing at all.** Model swapping is
the registry's job.

One integration fact if we ever wire an OpenAI-compatible surface to the proxy:
Vane's `openai` provider does expose a `baseURL` field, so LiteLLM works, but
`getDefaultModels()` returns empty whenever `baseURL` is not OpenAI's — models
must be enumerated by hand. Its `lmstudio` provider *does* auto-discover via
`GET {baseURL}/models` but **hardcodes `apiKey: 'lm-studio'`**, so it cannot
authenticate against our master key. Neither is fatal; both are friction.

There is also a direct collision with the edge research: Vane depends on strict
constrained decoding throughout its pipeline, and *The Constraint Tax*
(arXiv:2605.26128) measured that regime producing **88.9% wrong-but-schema-
valid** output. Vane has the exact failure mode that research documents, and no
verifier to catch it.

## 5. On student-facing search — yes to the idea, no to this tool

The concept is right and it is already in the roadmap. Vane specifically is
disqualified for a student deployment on four independent grounds: no
authentication for a multi-user tool; source URLs leaked to Google from the
student's browser; unbounded cost exposure from student-triggered searches; and
no citation verification.

That last one is the pedagogical objection and it is the strongest. **A tool
that manufactures citations without checking them teaches students to trust
citations that were never verified** — the precise habit a platform built on
"no module trusts a model's self-report" exists to counter.

The guard-railed version is a composition we are already most of the way to:

```
SearXNG  →  research_synthesis alias (Portage)  →  verifier.science (CC-P1)
   ↑                                                        ↓
HB-1 Step 3, already specified              citation_resolvability,
                                            hallucinated_citation_rate
   surfaced through Open WebUI (has auth, RBAC — HB-1 already plans it)
```

Every component is either built, specified, or scheduled. Nothing new is
required.

**The stretch worth taking: show students the verifier output.** Displaying
`citation_resolvability` and `hallucinated_citation_rate` beside the answer —
"4 of 7 citations resolved; 2 could not be verified" — converts a search tool
into an information-literacy instrument. No commercial product does this,
because no commercial product wants to advertise its own hallucination rate. It
is measurable, which makes it bench-able and therefore grant-able, and it is a
distinctive contribution rather than a reimplementation.

## 6. If we ever want an answer-engine UI

Not now — HB-1's Open WebUI plus SearXNG already covers the surface, and Open
WebUI has the authentication and RBAC that any multi-user deployment requires.

If a dedicated Perplexity-shaped UI later becomes worth having, the maintained
option is **Morphic** (Apache-2.0, committing as of today, four search backends
including SearXNG, OpenAI-compatible providers as a documented feature rather
than an incidental `baseURL` field). It costs Postgres and Supabase auth, which
is heavier than Vane's SQLite. **Farfalle is two years dead; do not consider
it.**

## 7. What Vane is genuinely worth

It is MIT-licensed and readable, and two things in it are worth an hour:

- Its `baseSearch.ts` embed → dedupe (cosine > 0.75) → rank (> 0.5) flow is a
  sane reference implementation of the retrieval step, at roughly 300 lines.
- Its `/api/search` response shape — `{message, sources[{content,
  metadata{title, url}}]}` — is a reasonable model for what the science lane
  should emit, and it is exactly the input `verifier.science` needs.

Adopting a dormant, unauthenticated project with an unpatched key-leak as
infrastructure would also sit badly with a platform whose maintenance thesis is
`KNOWN_GOOD_VERSIONS`, drift watch, and the CC-P2 rails. **Read it, take the
two ideas, and build the lane we already specified.**

---

*Sources: direct clone and source inspection of `ItzCrazyKns/Vane@7dc5d08`;
issues #1144, #1155; XDA, "I made my own Perplexity locally and only lost the
monthly bill" (2026-08-02); `miurla/morphic`; `open-webui/open-webui`;
`rashadphz/farfalle`. Retrieved 2026-08-04.*
