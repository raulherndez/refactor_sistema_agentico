# Skill: Diagnóstico de Acoplamiento y Modularidad

## Propósito
Detectar lógica monolítica, prompts mezclados con código o configuración, y responsabilidades acopladas en un proyecto o flujo agéntico existente.

## Cuándo activar
- Al analizar un proyecto previo con flujos LLM o agentes antes de refactorizar.
- Cuando se pide identificar cuellos de botella de mantenimiento o ambigüedades de comportamiento.

## Cuándo NO activar
- Cuando la tarea sea escribir código final de producción o generar reportes ejecutivos finales sin diagnóstico previo.

## Recursos adicionales
- Consultar `references/checklist_auditoria.md` como guía para verificar cobertura del diagnóstico. Omitir los puntos que no apliquen y no presentar como hallazgo aquello que no esté respaldado por evidencia.

## Reglas y restricciones
- Basarse únicamente en la evidencia del código, configuración o entrada proporcionada; no inventar archivos ni comportamientos inexistentes.
- Distinguir claramente entre **lógica determinista**, **configuración** y **comportamiento (agente/skills)**.
- Priorizar hallazgos por impacto en mantenibilidad, claridad y desacoplamiento.

## Flujo de ejecución
1. Revisar la estructura, entradas y flujos del proyecto o muestra analizada.
2. Identificar responsabilidades mezcladas o acopladas (prompts embebidos, parámetros fijos, agentes genéricos).
3. Clasificar cada hallazgo por severidad y proponer qué separar en lógica Python, configuración o skill.

## Formato de salida
- **Resumen del diagnóstico** (1 párrafo breve).
- **Hallazgos clave** (lista con problema, ubicación/evidencia y riesgo).
- **Recomendación de separación** (Lógica / Configuración / Comportamiento).
