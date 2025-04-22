SUMMARIZE_PR_INSTRUCTION = (
    'Based on the following code changes (git diff), generate a concise and informative pull request description. '
    'The description should clearly explain the **purpose** (why the change was made) and the **summary** (what was changed) in natural language. '
    'Structure the output logically for readability. '
    'Format the entire result as a single markdown block.'
)

REVIEW_CHANGES_INSTRUCTION = (
    'Act as an **expert Senior Software Engineer** performing a **critical code review** of the following changes (git diff). '
    'Your primary focus is on identifying potential issues related to **performance** (e.g., bottlenecks, inefficient algorithms, resource leaks) and **security** (e.g., vulnerabilities like injection, data exposure, insecure dependencies, auth issues). '
    'However, also scrutinize for **code quality, maintainability, potential bugs, edge cases, and adherence to best practices**. '
    'Be meticulous and detail-oriented in your analysis. Provide **actionable feedback**, clearly explaining the issue, its potential impact, and suggesting specific improvements or alternatives. '
    '**Prioritize significant findings** – do not simply list every minor change or style preference unless it impacts functionality, security, or performance significantly. '
    'Structure your review clearly, perhaps using bullet points grouped by file or severity. '
    'Format the entire result as a single markdown block.'
)

GENERATE_COMMIT_INSTRUCTION = (
    'Generate a single conventional commit message for the following changes (git diff). '
    'Adhere strictly to the Conventional Commits specification (v1.0.0). '
    'Use the format: `<type>: <description>`\n\n'
    'Common types: `feat` (new feature), `fix` (bug fix), `refactor` (code change that neither fixes a bug nor adds a feature), '
    '`test` (adding/updating tests), `docs` (documentation only), `revert` (reverts a previous commit).\n\n'
    'The `<description>` must be concise (imperative, present tense, max ~50 chars) and accurately reflect the core change. '
    'Only generate the single commit message line. Do not add explanations before or after.'
)

GENERATE_DOCS_INSTRUCTION = (
    'Act as a technical writer analyzing the following code changes (git diff) to determine necessary documentation updates. '
    '**Ignore code comments and docstrings.** Your focus is on user-facing documentation.\n\n'
    '1.  **README Updates:** Examine if the changes affect project setup, installation, usage examples, API contracts, core concepts, or configuration described in the main README file(s). If so, suggest specific updates or additions to the relevant sections. Provide the suggested markdown content.\n'
    '2.  **New Documentation Files:** If the changes introduce a significant new feature, a complex workflow, or a distinct architectural component that warrants detailed explanation, suggest creating a **new markdown file** within a `/docs` directory (e.g., `/docs/my-new-feature.md`). Outline the key sections this new file should cover and provide introductory content if possible.\n'
    '3.  **Diagrams (Mermaid):** If the changes introduce or significantly alter a workflow, state machine, data flow, or component interaction that would benefit from visualization, **generate a Mermaid diagram** (using appropriate `mermaid` markdown code blocks) to illustrate it. Suggest where this diagram should be placed (e.g., in the README or a relevant `/docs` file).\n'
    '4.  **Output:** Present your findings and suggestions clearly, organized by file (README, new files). Provide concrete markdown content for updates and diagrams. If no documentation updates seem necessary based on the diff, state that explicitly. Format the entire result as a single markdown block.'
)
