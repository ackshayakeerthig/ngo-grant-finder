**grant-finder-ai** project:

# Grant Finder AI Crew

Welcome to the grant-finder-ai Crew project, powered by [crewAI](https://crewai.com).  
This project implements an AI-powered workflow to help non-profit organizations discover, filter, and report potential grant funding opportunities.

Using a modular crew of intelligent agents, the system researches relevant grants, assesses organizational eligibility, and generates professional markdown reports — all leveraging web search tools and advanced language models.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, providing a smooth setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
````

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

* Add your API keys (e.g., OpenAI or others if applicable) into the `.env` file
* Modify `src/grant_finder/config/crews/grant_finding_team/Agents.yaml` to configure your agents
* Modify `src/grant_finder/config/crews/grant_finding_team/tasks.yaml` to define or update your tasks
* Modify `src/grant_finder/crews/grant_finding_team.py` to add custom agent logic or tools
* Modify `src/grant_finder/main.py` to customize inputs and control the flow

## Running the Project

To start the grant-finder-ai flow and begin execution, run this from your project root folder:

```bash
crewai run
```

This command will execute the flow that searches for grant funding opportunities, filters eligibility, and saves a markdown report with the findings.

## Understanding Your Crew

The grant-finder-ai Crew is composed of multiple AI agents, each specialized for different roles:

* ResearchAgent: finds potential funding sources
* EligibilityAgent: filters funding based on eligibility
* ReportAgent: generates a detailed markdown report

These agents collaborate sequentially to deliver a comprehensive grant-finding solution for nonprofits.

## Support

For support, questions, or feedback regarding the grant-finder-ai Crew or crewAI, please:

* Visit the [crewAI documentation](https://docs.crewai.com)
* Visit the [crewAI GitHub repository](https://github.com/joaomdmoura/crewai)
* Join the [crewAI Discord community](https://discord.com/invite/X4JWnZnxPb)

Let's empower nonprofits together with AI-driven grant discovery!

```

---

If you want, I can also help you generate a full LICENSE file or CONTRIBUTING guide!
