# v2 Job Discovery & Curation

Objective: Implementar búsqueda interactiva de propuestas, persistencia de decisiones (interesa/no interesa), recomendación básica y generación desde jobs seleccionados, reutilizando la abstracción de fuentes, `JobData`, LLM/skills y almacenamiento existente.

Branch: v2
Delivery strategy: ask-on-risk

## Specs

- S1. **Persistencia/índice (Fase 1)**: almacenamiento liviano en `output_dir/index/` para búsquedas y decisiones por job (`pending|interested|rejected`), con identidad estable de job (`job_id` o fallback). Permite listar resultados y recuperar contexto; compatible en lo posible con cache legacy.
- S2. **Backend búsqueda y curación (Fase 2)**: endpoints web para ejecutar búsqueda (filtros: query, num_pages, country, remote_only, date_posted, employment_types, source), listar/historial, listar jobs con estado, y marcar decisión. Valida API key de la fuente y usa `JobSearchAdapter`.
- S3. **Generación desde job seleccionado (Fase 5)**: endpoint para generar un skill (jobsynthesis/createcv/presentationletter/interviewquestions) a partir de un `JobData` guardado (no texto pegado), reutilizando `LLMService`, skills y guardado de outputs; guarda contexto del job (`job.md`/metadatos) junto a la salida.
- S4. **UI pestaña “Buscar propuestas” (Fase 4)**: nueva pestaña con formulario de filtros, resultados, acciones me interesa/no me interesa/pendiente, vistas por estado, y acceso a generación/ver detalle desde jobs.
- S5. **Recomendación básica (Fase 3)**: scoring/orden heurístico local usando CV + datos del job (keywords/afinidad simple) expuesto en listado/UI; LLM opcional queda para etapa posterior.

## Tasks

| ID | S# | Route | Status | Commit | Notes |
|---|---|---|---|---|---|
| T1 | S1 | inline | done | 22e86db | Store/index de búsquedas y decisiones (`src/laburator/store.py`) |
| T2 | S2 | inline | done | 22e86db | Endpoints `/api/search`, `/api/searches*`, `/api/discovery/jobs`, `/api/discovery/decision`, `/api/discovery/job/*` |
| T3 | S3 | inline | done | c6f6759 | Endpoint `/api/discovery/generate` genera skill desde job indexado y guarda salida/job.md |
| T4 | S4 | inline | pending | - | Pestaña UI de búsqueda y curación |
| T5 | S5 | inline | pending | - | Scoring heurístico y orden/recomendación básica |

## Log

L1. [2026-11-15] User request (verbatim):
> "segui con las etapas planteadas"

Contexto: Etapa 1 (abstracción JobSearch, commit 7f7ded2) completada en branch `v2`. Continuar con etapas v2 por incrementos con commits, sin push. Sin tests (prototipo).

L2. [2026-11-15] T1+T2: creado `store.py` (índice JSON en `output_dir/index/`, búsquedas, decisiones pending/interested/rejected, lookup de jobs, cache legacy `cache/<slug>/jobs.json`). Agregados endpoints web de búsqueda/listado/decisión usando `JobSearchAdapter` y fuente `openninja`. Verificación: `py_compile` y carga de rutas con `.venv` OK. Commit 22e86db. Risk: none.

L3. [2026-11-15] T3: refactor helpers de generación web y agregado `/api/discovery/generate` para ejecutar skills sobre `JobData` indexado, guardando output y `job.md` en carpeta por empresa-puesto. Verificación: `py_compile` y rutas cargadas OK. Commit c6f6759. Risk: none.
