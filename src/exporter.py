import json
from pathlib import Path

from src.models import ExecutionPlan


def export_execution_plan(plan: ExecutionPlan, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    serialized_plan = {
        "agent_name": plan.agent_name,
        "model": plan.model,
        "temperature": plan.temperature,
        "input_file": str(plan.input_file),
        "skills_loaded": plan.skills_loaded,
        "system_prompt": plan.system_prompt,
        "input_preview": plan.input_preview,
    }
    output_path.write_text(
        json.dumps(serialized_plan, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return output_path
