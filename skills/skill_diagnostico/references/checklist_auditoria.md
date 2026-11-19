# Checklist de auditoría de modularidad

Usa esta lista para organizar la revisión. Marca cada punto como **revisado**, **no aplica** o **pendiente** y registra rutas, fragmentos o ejemplos que respalden cada conclusión.

## Lógica determinista

- [ ] ¿Las responsabilidades de carga, validación, orquestación y presentación están delimitadas?
- [ ] ¿La lógica de negocio está separada de las instrucciones dirigidas al agente?
- [ ] ¿Se distinguen los errores esperados y se comunican con contexto útil?
- [ ] ¿Las rutas y dependencias entre módulos son consistentes?

## Configuración

- [ ] ¿Los parámetros variables (por ejemplo, modelo, temperatura y rutas) están fuera del código?
- [ ] ¿La configuración tiene valores predeterminados explícitos y validaciones suficientes?
- [ ] ¿Los nombres configurados de agentes y skills coinciden con los recursos disponibles?

## Agentes y skills

- [ ] ¿Cada agente tiene un propósito y un flujo de trabajo definidos?
- [ ] ¿Las skills describen capacidades acotadas y reutilizables?
- [ ] ¿Las responsabilidades están asignadas a la capa adecuada, sin duplicar instrucciones?
- [ ] ¿Los recursos de apoyo de una skill se enlazan desde su `SKILL.md` y se usan solo cuando son pertinentes?

## Registro de evidencia

Para cada hallazgo, anota:

| Campo | Qué registrar |
| --- | --- |
| Hallazgo | Problema concreto, no una recomendación genérica |
| Evidencia | Archivo, sección o comportamiento observado |
| Capa | Lógica, configuración o comportamiento |
| Impacto | Consecuencia verificable para mantenimiento o claridad |
| Recomendación | Separación o cambio acotado que aborda el problema |

No marques un elemento como defecto si no hay evidencia suficiente; indícalo como pendiente de verificación.
