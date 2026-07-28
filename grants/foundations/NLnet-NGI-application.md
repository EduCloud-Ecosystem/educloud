# Application Draft — NLnet Foundation (NGI / Commons Fund)

*Audience: NLnet's open-call grant funds (open standards, privacy, interoperability; €5,000–€50,000; funds individuals and entities worldwide)*
*Format: structured to NLnet's actual application form fields · Status: **2027** — a targeted component ask, not core operations · Grantee: project/maintainer directly (NLnet does not require a 501(c)(3))*

---

**Project name:** Open Classroom Interop: a metadata standard and privacy-preserving federation protocol for educational object registries

**Requested amount:** €42,000

**Abstract** *(NLnet caps this field at ~1,200 characters — current draft ≈900)*

Course infrastructure is re-centralizing: when GitHub Classroom retired in 2026, thousands of institutions migrated to closed platforms because no open interoperability layer existed. This project builds that layer, not another platform. We will specify and reference-implement (1) an open metadata standard for educational objects — courses, assignments, datasets, computational artifacts — with license-aware fields, so any registry can describe and exchange them; and (2) a privacy-preserving federation protocol through which independent, self-hosted registries discover and mirror each other's public objects without any central index and without exchanging personal data (identities are platform usernames only; rosters never federate). Both emerge from EduCloud, a working open-source (AGPL/Apache-2.0) classroom platform, but are deliberately specified so Forgejo, Moodle, or any LMS can implement them independently. Deliverables: the specifications, two interoperating implementations, a conformance test suite, and documentation.

**Have you been involved with projects or organisations relevant to this project before?**
EduCloud (open-source GitHub Classroom successor; founder); training/EOT lead for MESA, an NSF open-science cyberinfrastructure program; Carpentries instructor community. Co-applicant Ben Markwart maintains the EduCloud Registry and brings research-software-engineering and nonprofit-governance experience.

**Explain what the requested budget will be used for**
Specification work and public RFC process (~€14K); the second, independent implementation plus conformance suite — the proof of interoperability (~€16K); privacy review of the federation protocol (~€6K); documentation and community engagement with Forgejo/Codeberg and LMS communities (~€6K). No hardware; no overheads.

**Compare your own project with existing or historical efforts**
LTI standardizes launching *into* commercial tools, not describing or federating open objects; OAI-PMH federates *publication* metadata, not executable coursework; SCORM/xAPI describe content packaging and telemetry, not version-controlled, autogradable artifacts. Nothing currently lets two self-hosted classroom platforms discover each other's openly licensed courses without a central broker. We reuse rather than reinvent where possible (DCAT vocabulary alignment; ActivityPub evaluated as transport — adopted if it fits, documented if not).

**What are significant technical challenges you expect to solve?**
Federation without surveillance: object discovery across registries while structurally preventing roster or learner-activity leakage (the protocol carries no personal data by construction, not by policy). Conformance that means something: a test suite strict enough that "implements the standard" guarantees actual interop. Versioned metadata for *executable* artifacts whose grading environments evolve.

**Describe the ecosystem of the project, and how you will engage with relevant actors**
EduCloud's pilot institutions (community colleges through R1s) provide real registries; the Forgejo/Codeberg community is a second natural implementer (outreach already drafted); the open-education community (OER catalogs) is the consumer of license-aware search. The RFC process runs in public; results presented to open-education and self-hosting communities.

---

*[Before sending: pick the open NLnet call (Commons Fund vs. thematic), re-check field labels and character limits against the live form, and decide applicant of record (maintainer vs. sponsored entity).]*
