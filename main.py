import argparse
from pathlib import Path
import sys

from src.exporter import export_execution_plan
from src.orchestrator import build_execution_plan


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Ejecuta la planificación modular del sistema agéntico."
    )
    parser.add_argument(
        "input_file",
        help="Ruta al archivo de entrada a analizar o refactorizar.",
    )
    parser.add_argument(
        "--agent",
        dest="agent_name",
        default=None,
        help="Nombre del agente a utilizar (por defecto usa default_agent en settings.json).",
    )
    parser.add_argument(
        "--export-plan",
        nargs="?",
        const=Path("outputs") / "execution_plan.json",
        type=Path,
        default=None,
        metavar="RUTA",
        help=(
            "Exporta el plan como JSON (por defecto: "
            "outputs/execution_plan.json)."
        ),
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_dir = Path(__file__).resolve().parent
    input_path = Path(args.input_file)
    if not input_path.is_absolute():
        input_path = (base_dir / input_path).resolve()

    try:
        plan = build_execution_plan(
            base_dir=base_dir,
            input_file=input_path,
            requested_agent=args.agent_name,
        )
    except (FileNotFoundError, KeyError, ValueError) as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    if args.export_plan is not None:
        output_path = args.export_plan
        if not output_path.is_absolute():
            output_path = (base_dir / output_path).resolve()
        try:
            exported_path = export_execution_plan(plan, output_path)
        except OSError as exc:
            print(f"[ERROR] No se pudo exportar el plan: {exc}", file=sys.stderr)
            return 1
        print(f"Plan exportado: {exported_path}")

    print(f"Agente: {plan.agent_name}")
    print(f"Modelo: {plan.model} (temperature={plan.temperature})")
    print(f"Archivo de entrada: {plan.input_file}")
    print(f"Skills cargadas: {', '.join(plan.skills_loaded)}")
    print("-" * 50)
    print("Vista previa de entrada:")
    print(plan.input_preview)
    print("-" * 50)
    print(f"Longitud del system_prompt ensamblado: {len(plan.system_prompt)} caracteres")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
