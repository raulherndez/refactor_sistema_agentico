@'
# Sistema Agéntico Modular

Proyecto de ejemplo en Python para demostrar cómo separar la lógica determinista, la configuración y las instrucciones de comportamiento de un sistema agéntico.

El programa carga un agente, sus skills asignadas y un archivo de entrada; ensambla el `system_prompt` correspondiente y presenta una vista previa del plan de ejecución. No realiza llamadas a APIs de modelos.

## Características

- Configuración centralizada en `config/settings.json`.
- Agentes definidos como archivos Markdown.
- Skills modulares reutilizables.
- Resolución de agentes y skills según configuración.
- Exportación opcional del plan de ejecución en formato JSON.
- Pruebas de integración con `unittest` y directorios temporales.
- Validación de rutas y archivos mediante errores claros.
- Uso exclusivo de la biblioteca estándar de Python.

## Requisitos

- Python 3.10 o posterior.
- No hay dependencias externas.

## Uso

Ejecutar desde la raíz del proyecto:

```powershell
python main.py inputs/muestra.txt
```

Esto utiliza el agente configurado como `default_agent`.

Para seleccionar explícitamente otro agente:

```powershell
python main.py inputs/muestra.txt --agent agente_ejecutor
```

Para exportar el plan a `outputs/execution_plan.json`:

```powershell
python main.py inputs/muestra.txt --export-plan
```

También se puede indicar una ruta de salida específica:

```powershell
python main.py inputs/muestra.txt --export-plan outputs/analisis.json
```

La carpeta de destino se crea automáticamente. El JSON contiene el agente, el modelo, la temperatura, la ruta de entrada, las skills cargadas, el `system_prompt` ensamblado y la vista previa de la entrada. La exportación es opcional; sin `--export-plan`, el programa solo muestra el resumen en la terminal.

También se puede proporcionar una ruta absoluta o relativa a otro archivo de entrada.

La salida incluye:

- Nombre del agente seleccionado.
- Modelo y temperatura configurados.
- Archivo de entrada.
- Skills cargadas.
- Vista previa del contenido de entrada.
- Longitud del `system_prompt` ensamblado.

## Ejecución y verificación en PowerShell

Desde la raíz del proyecto (`C:\Users\raulh\OneDrive\Desktop\refactor_sistema_agentico`):

1. Correr la suite de pruebas con `unittest`:

```powershell
python -m unittest discover -s tests -v
```

2. Ejecutar el flujo principal y exportar el plan a JSON:

```powershell
python main.py inputs\muestra.txt --export-plan
```

Probar el agente ejecutor con un archivo de salida personalizado:

```powershell
python main.py inputs\muestra.txt --agent agente_ejecutor --export-plan outputs\ejecutor_plan.json
```

3. Comprobar que se generó el JSON exportado:

```powershell
Test-Path outputs\execution_plan.json
Get-Content outputs\execution_plan.json -TotalCount 25
```

## Agentes disponibles

| Agente | Skills asignadas |
| --- | --- |
| `agente_analista` | `skill_diagnostico`, `skill_reporte` |
| `agente_ejecutor` | `skill_refactorizacion`, `skill_reporte` |

El agente predeterminado es `agente_analista`.

## Configuración

`config/settings.json` define:

- Nombre del proyecto.
- Modelo y temperatura.
- Reintentos y tiempo límite.
- Directorios de agentes, skills e entradas.
- Agente predeterminado.
- Relación entre cada agente y sus skills.

Ejemplo de selección:

```json
{
  "default_agent": "agente_analista",
  "agent_skills": {
    "agente_analista": ["skill_diagnostico", "skill_reporte"]
  }
}
```

## Estructura del proyecto

```text
.
├── main.py
├── config/
│   └── settings.json
├── agents/
│   ├── agente_analista.md
│   └── agente_ejecutor.md
├── skills/
│   ├── skill_diagnostico/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── checklist_auditoria.md
│   ├── skill_refactorizacion/
│   │   └── SKILL.md
│   └── skill_reporte/
│       └── SKILL.md
├── inputs/
│   └── muestra.txt
├── outputs/
│   └── (planes JSON exportados; se crea al exportar)
├── src/
    ├── exporter.py
    ├── loader.py
    ├── models.py
    └── orchestrator.py
└── tests/
    └── test_pipeline.py
```

## Arquitectura

- `main.py` procesa los argumentos de línea de comandos y muestra el plan generado.
- `src/models.py` define los tipos de configuración y datos mediante dataclasses.
- `src/loader.py` carga JSON, agentes, skills y entradas desde disco.
- `src/orchestrator.py` valida el agente solicitado y ensambla el plan de ejecución.
- `src/exporter.py` serializa el plan a JSON y crea el directorio de destino si hace falta.
- `tests/test_pipeline.py` verifica la construcción del plan, el rechazo de agentes no configurados y la exportación.
- `config/` contiene los parámetros editables del sistema.
- `agents/` contiene las especificaciones de comportamiento de cada agente.
- `skills/` contiene capacidades independientes en archivos Markdown.

## Pruebas

Ejecutar las pruebas unitarias desde la raíz del proyecto:

```powershell
python -m unittest discover -s tests -v
```

## Ejemplo de ejecución

```powershell
python main.py inputs/muestra.txt
```

Resultado esperado, de forma resumida:

```text
Agente: agente_analista
Modelo: gpt-4o-mini (temperature=0.2)
Archivo de entrada: ...\inputs\muestra.txt
Skills cargadas: skill_diagnostico, skill_reporte
```

## Errores habituales

- Archivo de entrada inexistente: se indica la ruta que no pudo encontrarse.
- Configuración ausente: se indica la ubicación esperada de `settings.json`.
- Agente inexistente o sin skills asignadas: se muestran los agentes disponibles.
- Skill o agente definido en la configuración pero ausente del disco: se indica el archivo esperado.
'@ | Set-Content -Path README.md -Encoding UTF8

git add README.md
git commit -m "Add PowerShell execution and verification section to README"
git push