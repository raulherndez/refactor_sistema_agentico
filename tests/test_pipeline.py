import json
from pathlib import Path
import tempfile
import unittest

from src.exporter import export_execution_plan
from src.orchestrator import build_execution_plan


class ExecutionPlanPipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name)
        (self.base_dir / "config").mkdir()
        (self.base_dir / "agents").mkdir()
        (self.base_dir / "skills" / "skill_review").mkdir(parents=True)
        (self.base_dir / "inputs").mkdir()

        (self.base_dir / "config" / "settings.json").write_text(
            json.dumps(
                {
                    "model": "test-model",
                    "temperature": 0.1,
                    "default_agent": "reviewer",
                    "agent_skills": {"reviewer": ["skill_review"]},
                }
            ),
            encoding="utf-8",
        )
        (self.base_dir / "agents" / "reviewer.md").write_text(
            "Review agent instructions.", encoding="utf-8"
        )
        (self.base_dir / "skills" / "skill_review" / "SKILL.md").write_text(
            "Review skill instructions.", encoding="utf-8"
        )
        self.input_file = self.base_dir / "inputs" / "sample.txt"
        self.input_file.write_text("Analyze this input.", encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_builds_plan_from_configured_agent_and_skill(self):
        plan = build_execution_plan(self.base_dir, self.input_file)

        self.assertEqual(plan.agent_name, "reviewer")
        self.assertEqual(plan.model, "test-model")
        self.assertEqual(plan.temperature, 0.1)
        self.assertEqual(plan.skills_loaded, ["skill_review"])
        self.assertEqual(plan.input_preview, "Analyze this input.")
        self.assertIn("Review agent instructions.", plan.system_prompt)
        self.assertIn("Review skill instructions.", plan.system_prompt)

    def test_rejects_agent_not_configured(self):
        with self.assertRaisesRegex(KeyError, "missing"):
            build_execution_plan(
                self.base_dir, self.input_file, requested_agent="missing"
            )

    def test_exports_plan_as_json_and_creates_parent_directory(self):
        plan = build_execution_plan(self.base_dir, self.input_file)
        output_path = self.base_dir / "outputs" / "plans" / "plan.json"

        returned_path = export_execution_plan(plan, output_path)

        self.assertEqual(returned_path, output_path)
        exported = json.loads(output_path.read_text(encoding="utf-8"))
        self.assertEqual(exported["agent_name"], "reviewer")
        self.assertEqual(exported["input_file"], str(self.input_file))
        self.assertEqual(exported["skills_loaded"], ["skill_review"])
        self.assertEqual(exported["system_prompt"], plan.system_prompt)
        self.assertEqual(exported["input_preview"], plan.input_preview)


if __name__ == "__main__":
    unittest.main()
