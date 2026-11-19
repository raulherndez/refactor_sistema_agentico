from pathlib import Path
from typing import Optional

from src.loader import load_agent, load_config, load_input_text, load_skills_map
from src.models import AgentDefinition, AppConfig, ExecutionPlan


def resolve_agent_name(config: AppConfig, requested_agent: Optional[str] = None) -> str:
    agent_name = requested_agent or config.default_agent
    if agent_name not in config.agent_skills:
        raise KeyError(
            f"El agente '{agent_name}' no tiene skills mapeadas en 'agent_skills'. "
            f"Agentes disponibles: {list(config.agent_skills.keys())}"
        )
    return agent_name


def build_system_prompt(agent: AgentDefinition, skills_content: list[str]) -> str:
    sections = [
        f"# AGENT SPECIFICATION: {agent.name}\n{agent.content}",
    ]
    for skill_text in skills_content:
        sections.append(f"---\n{skill_text}")
    return "\n\n".join(sections)


def build_execution_plan(
    base_dir: Path,
    input_file: Path,
    requested_agent: Optional[str] = None,
    preview_chars: int = 240,
) -> ExecutionPlan:
    config = load_config(base_dir / "config" / "settings.json")
    agent_name = resolve_agent_name(config, requested_agent)

    assigned_skill_names = config.agent_skills[agent_name]
    skills_dir = base_dir / config.paths.skills_dir
    agents_dir = base_dir / config.paths.agents_dir

    agent = load_agent(agents_dir, agent_name, assigned_skill_names)
    skills_map = load_skills_map(skills_dir, assigned_skill_names)

    ordered_skills = [skills_map[name].content for name in assigned_skill_names]
    system_prompt = build_system_prompt(agent, ordered_skills)

    input_text = load_input_text(input_file)
    preview = input_text[:preview_chars] + ("..." if len(input_text) > preview_chars else "")

    return ExecutionPlan(
        agent_name=agent.name,
        model=config.model,
        temperature=config.temperature,
        input_file=input_file,
        skills_loaded=list(assigned_skill_names),
        system_prompt=system_prompt,
        input_preview=preview,
    )
