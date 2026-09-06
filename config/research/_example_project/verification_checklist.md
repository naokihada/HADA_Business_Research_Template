# Verification Checklist — Example Project

Use this checklist when building candidate dossiers.

## Identity Verification

- [ ] Official website or product page located
- [ ] Vendor still operating (not acquired/shutdown without successor)
- [ ] Entity type confirmed (ORGANIZATION vs SERVICE)

## Gate Verification

| Gate ID | Check |
|---|---|
| currently_operating | Active service pages, recent updates, or official status |
| core_service_match | Backup is primary offering — not peripheral feature only |
| geographic_coverage | JP/US availability stated or verified |
| enterprise_sso | SSO/SAML/OIDC mentioned in official docs |
| api_integration | API docs or developer portal exists |
| contract_flexibility | Monthly or trial explicitly offered |

## Capability Verification

| Criterion ID | Check |
|---|---|
| backup_scope | What can be backed up |
| restore_options | Restore granularity |
| encryption | At rest and in transit |
| admin_console | Admin UX exists |
| api_available | API documented |
| sso_support | Enterprise auth documented |
| pricing_public | Pricing page or calculator |
| support_channels | Support options listed |

## Entity Resolution

- [ ] Duplicate listings identified
- [ ] Canonical entity selected
- [ ] Original directory values preserved if corrected
- [ ] canonical_candidate_id set for duplicate rows

## Before Scoring

- [ ] All material claims have classification and source
- [ ] UNKNOWN items listed in dossier unknowns section
- [ ] No inferred YES without evidence
