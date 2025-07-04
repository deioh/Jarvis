# Ruby's Notes: Experiences & Learnings

This file logs my experiences with different commands, tools, and methods to ensure I learn from them and continuously improve my workflow.

## Filesystem Access Limitations

**Date:** July 4, 2025

**Context:** I attempted to access your Downloads folder (`C:\Users\1UP\Downloads`) to list its contents.

**Observation:**
All attempts to use the `dir` command on paths outside of my designated workspace (`D:\jarvis`) failed with a syntax error, even though the syntax was correct. This indicates a permission or pathing issue within my execution environment that I cannot resolve.

**Conclusion:**
My effective operational scope is strictly limited to the `D:\jarvis` directory. While my tools can technically accept absolute paths, my environment prevents them from working correctly outside this workspace. My initial statement about being able to access any file was incorrect.

**Actionable Insight:**
I will not attempt to access files or directories outside of the `D:\jarvis` workspace. I will inform you if a request requires me to access a path that is outside my operational scope. This is a critical safety and functionality boundary.

---

## Taskmaster AI Tooling Issues

**Date:** July 4, 2025

**Context:** We attempted to use the `taskmaster-ai` tool to manage the creation of our `simple-webapp` test project.

**Observations:**
I encountered several blocking issues with the `taskmaster-ai` tool in this environment:
1.  **`parse_prd` Failure:** The command failed due to a missing Anthropic API key and credit balance.
2.  **`add_task` Prerequisite:** The command requires a `tasks.json` file to exist, which is not created on `initialize_project`.
3.  **`set_task_status` Failure:** After manually creating `tasks.json`, the `set_task_status` command was unable to find the tasks.

**Conclusion:**
The `taskmaster-ai` tool, in its current state within this environment, is not reliable for our workflow.

**Actionable Insight:**
I will avoid using `taskmaster-ai` for now and will proceed with projects by manually outlining the steps.

---

## PowerShell Interaction Issue

**Date:** July 4, 2025

**Context:** We attempted to switch from the standard command prompt to PowerShell for executing commands.

**Observation:**
When using `powershell -Command "..."`, the commands were echoed back in the standard output instead of being executed.

**Conclusion:**
My current environment has an issue with how it pipes commands to PowerShell. The standard command prompt (`cmd.exe`) remains the reliable method for command execution.

**Actionable Insight:**
I will continue to use the standard command prompt for all shell commands.

---
## `run_shell_command` Directory Path

**Date:** July 4, 2025

**Context:** Executing an `npm` command in a subdirectory.

**Observation:**
The `run_shell_command` tool failed when I provided an absolute path to the `directory` parameter.

**Conclusion:**
The `directory` parameter for `run_shell_command` requires a **relative path** from the project root.

**Actionable Insight:**
I will always use relative paths for the `directory` parameter in the `run_shell_command` tool.
