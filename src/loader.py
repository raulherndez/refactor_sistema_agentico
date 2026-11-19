import json
from pathlib import Path
from typing import Dict

from src.models import AgentDefinition, AppConfig, PathsConfig, SkillDefinition


def load_config(config_path: Path) -> AppConfig:
    if not config_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de configuración: {config_path}")

    raw = json.loads(config_path.read_text(encoding="utf-8-sig"))
    paths_raw = raw.get("paths", {})

    paths = PathsConfig(
        agents_dir=paths_raw.get("agents_dir", "agents"),
        skills_dir=paths_raw.get("skills_dir", "skills"),
        inputs_dir=paths_raw.get("inputs_dir", "inputs"),
    )

    return AppConfig(
        project_name=raw.get("project_name", "refactor_sistema_agentico"),
        model=raw.get("model", "gpt-4o-mini"),
        temperature=float(raw.get("temperature", 0.2)),
        max_retries=int(raw.get("max_retries", 2)),
        timeout_seconds=int(raw.get("timeout_seconds", 30)),
        paths=paths,
        default_agent=raw.get("default_agent", "agente_analista"),
        agent_skills=raw.get("agent_skills", {}),
    )


def load_skill(skills_dir: Path, skill_name: str) -> SkillDefinition:
    skill_path = skills_dir / skill_name / "SKILL.md"
    if not skill_path.exists():
        raise FileNotFoundError(f"No se encontró la skill '{skill_name}' en: {skill_path}")

    return SkillDefinition(
        name=skill_name,
        path=skill_path,
        content=skill_path.read_text(encoding="utf-8-sig").strip(),
    )


def load_skills_map(skills_dir: Path, skill_names: list[str]) -> Dict[str, SkillDefinition]:
    loaded: Dict[str, SkillDefinition] = {}
    for name in skill_names:
        loaded[name] = load_skill(skills_dir, name)
    return loaded


def load_agent(agents_dir: Path, agent_name: str, assigned_skills: list[str]) -> AgentDefinition:
    agent_path = agents_dir / f"{agent_name}.md"
    if not agent_path.exists():
        raise FileNotFoundError(f"No se encontró el agente '{agent_name}' en: {agent_path}")

    return AgentDefinition(
        name=agent_name,
        path=agent_path,
        content=agent_path.read_text(encoding="utf-8-sig").strip(),
        assigned_skills=list(assigned_skills),
    )


def load_input_text(input_path: Path) -> str:
    if not input_path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {input_path}")
    return input_path.read_text(encoding="utf-8-sig")
