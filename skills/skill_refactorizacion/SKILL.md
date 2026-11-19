# Skill: Refactorización Modular de Sistemas Agénticos

## Propósito
Guiar la reorganización de un proyecto con flujos LLM o agentes para separar lógica determinista, configuración y comportamiento modular, evitando lógica monolítica o acoplada.

## Cuándo activar
- Al refactorizar código, módulos o flujos existentes que mezclan prompts, parámetros y lógica de ejecución.
- Cuando se necesite modularizar un agente o extraer capacidades reutilizables hacia skills.

## Cuándo NO activar
- Cuando solo se solicita diagnosticar un proyecto sin proponer cambios o cuando la tarea es únicamente redactar un reporte final de resultados.

## Reglas y restricciones
- Respetar el uso exclusivo de la librería estándar de Python cuando el proyecto lo exija; no introducir dependencias externas innecesarias.
- Mantener la configuración (modelos, rutas, parámetros) separada de la lógica y de las instrucciones de comportamiento.
- Conservar la funcionalidad del flujo base y hacer explícitos los cambios realizados y su impacto.

## Flujo de ejecución
1. Ubicar qué partes pertenecen a lógica/orquestación, cuáles a configuración y cuáles a comportamiento.
2. Diseñar o actualizar los módulos/skills/agentes necesarios con responsabilidades acotadas.
3. Aplicar la refactorización manteniendo rutas portables y contratos claros entre componentes.

## Formato de salida
- **Objetivo de la refactorización** (resumen breve).
- **Cambios por capa** (Lógica / Configuración / Comportamiento).
- **Archivos creados o modificados** (lista con propósito de cada uno).
