from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List


@dataclass(frozen=True)
class PathsConfig:
    agents_dir: str
    skills_dir: str
    inputs_dir: str


@dataclass(frozen=True)
class AppConfig:
    project_name: str
    model: str
    temperature: float
    max_retries: int
    timeout_seconds: int
    paths: PathsConfig
    default_agent: str
    agent_skills: Dict[str, List[str]]


@dataclass(frozen=True)
class SkillDefinition:
    name: str
    path: Path
    content: str


@dataclass(frozen=True)
class AgentDefinition:
    name: str
    path: Path
    content: str
    assigned_skills: List[str] = field(default_factory=list)


@dataclass
class ExecutionPlan:
    agent_name: str
    model: str
    temperature: float
    input_file: Path
    skills_loaded: List[str]
    system_prompt: str
    input_preview: str
