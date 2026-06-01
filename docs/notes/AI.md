# AI Helper Guidelines

This file describes how AI-based review and editing should be applied to this forecasting project.

## Purpose
- Keep project changes traceable.
- Support notebook-based forecasting analysis.
- Help reviewers validate that the notebook follows the subject rubric.

## Editing Guidelines
- Use `tasks.md` as the primary checklist for project requirements.
- Use `report_structure.md` to shape the final report narrative.
- Add a short entry to `log.md` for each meaningful code or documentation change.
- Preserve notebook structure and cell metadata when editing `src/FMTS_v2.ipynb`.

## Review Focus
- Confirm all model diagnostics are present (ACF, PACF, Ljung-Box, residuals).
- Verify 95% prediction intervals are generated and saved.
- Ensure cross-validation / walk-forward methods are clearly described.
- Check that COVID interruption handling is justified and documented.

## Output Expectations
- Edits should be minimal and focused on completing missing project items.
- Avoid broad refactors unless they improve clarity or correctness.
- Prefer explicit file updates rather than free-form text edits in notebook cells.
