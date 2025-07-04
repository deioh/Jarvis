# Ruby's Notes: Experiences & Learnings

**Core Principle:** Before executing any command or starting a complex task, I must first consult these notes to avoid repeating past mistakes.

---

This file logs my experiences with different commands, tools, and methods to ensure I learn from them and continuously improve my workflow.

## In-Sandbox Software Installation Limitations

**Date:** July 4, 2025

**Context:** We attempted to install the Ollama LLM service inside my sandbox environment.

**Observations:**
The installation failed due to limitations of my execution environment:
1.  **Missing Shells:** The standard `sh` shell is not available, preventing direct execution of shell scripts.
2.  **Missing Tools:** The `wget` utility is not installed.
3.  **`curl` Anomaly:** The `curl` command, while present, failed with an unusual "Port number was not a decimal number" error, suggesting a configuration or network issue within the sandbox.

**Conclusion:**
My sandbox environment is highly minimalistic and lacks the common tools required for arbitrary software installation. I cannot reliably download or install new applications or services.

**Actionable Insight:**
I will not attempt to install new software within my sandbox. Any required tools or services must either be pre-installed in my environment or be manageable through the existing, confirmed toolset (e.g., `npm`). This is a significant constraint on my ability to have an "assistant" or expand my capabilities.

---

## Filesystem Access Limitations

**Date:** July 4, 2025

**Context:** I attempted to access your Downloads folder (`C:\Users\1UP\Downloads`).

**Observation:**
All attempts to use the `dir` command on paths outside of my designated workspace (`D:\jarvis`) failed.

**Conclusion:**
My effective operational scope is strictly limited to the `D:\jarvis` directory.

**Actionable Insight:**
I will not attempt to access files or directories outside of the `D:\jarvis` workspace.

---

## Taskmaster AI Tooling Issues

**Date:** July 4, 2025

**Context:** We attempted to use the `taskmaster-ai` tool.

**Observations:**
The tool failed during `parse_prd`, `add_task`, and `set_task_status`.

**Conclusion:**
The `taskmaster-ai` tool is not reliable in this environment.

**Actionable Insight:**
I will avoid using `taskmaster-ai` for now.

---

## PowerShell Interaction Issue

**Date:** July 4, 2025

**Context:** We attempted to use PowerShell.

**Observation:**
Commands were echoed instead of executed.

**Conclusion:**
My environment has an issue with PowerShell.

**Actionable Insight:**
I will continue to use the standard command prompt.

---
## `run_shell_command` Directory Path

**Date:** July 4, 2025

**Context:** Executing an `npm` command in a subdirectory.

**Observation:**
The `directory` parameter failed with an absolute path.

**Conclusion:**
The `directory` parameter requires a relative path.

**Actionable Insight:**
I will always use relative paths for the `directory` parameter.
---

**Date:** 2025-07-04 10:36:49

"The_git_commit_command_fails_with_multi-line_messages._Using_the_-F_flag_with_a_temporary_file_is_the_most_reliable_workaround."

---

**Date:** 2025-07-04 10:45:54

My_shell_environment_does_not_support_quoted_multi-word_arguments.

---
## Handling Long-Running Commands (e.g., `npm install`)

**Date:** July 4, 2025

**Context:** Long-running commands like `npm install` were making me unresponsive.

**Problem:** My environment would block and wait for the command to complete, preventing me from interacting with the user.

**Solution:**
1.  **Execute in Background:** Use `start /b` on Windows to run the command as a non-blocking background process (e.g., `start /b npm install`).
2.  **Infer Completion:** Periodically check for the expected outcome of the command. For `npm install`, this is the creation of the `node_modules` directory.
3.  **Verify Success:** Once the outcome is detected, run a lightweight verification command. For `npm`, `npm list --depth=0` is a good choice to confirm the installation's integrity.

**Actionable Insight:** I will use this "launch, check, verify" method for all potentially long-running shell commands to remain responsive and ensure tasks complete successfully.

---
## Supervisory Protocol for AI Delegation (`#junior`)

**Date:** July 4, 2025

**Context:** The user, SirDei, has authorized me to delegate tasks to other AI models to accelerate development.

**Protocol:**
When the user invokes the `#junior` command, I will act as a supervisor and follow these steps:
1.  **Select & Access Junior:** Use browser automation to navigate to a suitable public AI chat interface (e.g., Perplexity, You.com).
2.  **Delegate with Precision:** Formulate a detailed, specific prompt outlining the exact requirements for the sub-task (e.g., generating a React component, writing a database schema).
3.  **Supervise & Verify:** Receive the generated code or plan from the junior AI.
4.  **Quality Assurance:** Thoroughly review the junior's work for correctness, efficiency, and adherence to project standards.
5.  **Integration:** Only after the work is verified and approved will I integrate it into our project.

**Actionable Insight:** This protocol allows me to leverage other AI agents as a force multiplier while maintaining my core responsibility for the quality and integrity of the codebase.