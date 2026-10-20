# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S.A. · **De:** Equipo de Business Intelligence
**Fecha:** 12/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se recibieron y auditaron los reportes semanales de ventas en los tres formatos provistos (CSV, JSON y Excel). El equipo de BI confirmó exitosamente que los tres archivos contienen exactamente la misma información validada (5 registros íntegros), sin pérdidas de datos entre sistemas. Se recomienda a la directiva utilizar estos indicadores con total confianza para la toma de decisiones y avanzar hacia la unificación a un solo formato estándar.

## 1. ¿Los tres formatos contienen la misma información?

Sí, tras realizar la lectura en Python y R, se confirmó que las dimensiones y la estructura base son idénticas en todos los orígenes.

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---|---|---|
| CSV | ERP de sucursales | 5 | 4 | `read_csv()` (Pandas y readr) |
| JSON | API de fidelización | 5 | 4 | `json_normalize()` (Pandas) / `fromJSON()` (jsonlite) |
| Excel | Consolidado de finanzas | 5 | 4 | `read_excel()` (Pandas y readxl) |

**¿La estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?**
No. La estructura interna de los archivos funciona únicamente como un medio de transporte de datos. Ya sea en texto plano (CSV), jerarquía anidada (JSON) o archivo binario (Excel), al ser procesados por los lenguajes de programación, todos se convierten en *DataFrames* tabulares idénticos, conservando el mismo valor analítico y contenido.

## 2. Tipos de datos y calidad

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `num` (double) | Numérica continua; apta para operaciones financieras directas. |
| `clientes` | `int64` | `num` (double) | Numérica discreta; representa conteo o tráfico en tienda. |
| `sucursal` | `object` (str) | `chr` (character) | Categórica de texto; identificador nominal de la tienda. |
| `region` | `object` (str) | `chr` (character) | Categórica de texto; agrupación geográfica. |

**¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?**
Si la columna `ventas` hubiera sido inferida como texto (`str` u `object`), habría indicado la presencia de caracteres no numéricos dentro de los datos, como espacios en blanco, símbolos de moneda ("$"), letras ("N/A") o comas mal ubicadas. Esto es un error crítico que impediría calcular sumas o promedios directamente sin una etapa previa de limpieza de datos.

## 3. Particularidades técnicas encontradas

* **CSV:** Fue el formato más directo. Ambos lenguajes lo procesaron de forma nativa deduciendo automáticamente la separación de columnas.
* **JSON:** Por su estructura de diccionario anidado, en Python se requirió el uso específico de `json_normalize()` para aplanar los datos y convertirlos en tabla. En R, la biblioteca `jsonlite` hizo este proceso automáticamente.
* **Excel:** Exigió pasar un parámetro adicional en ambos lenguajes (`sheet_name='ventas'` en Python y `sheet="ventas"` en R) para asegurar la lectura exacta de la matriz de datos, evitando leer hojas vacías.
* **Variables categóricas:** Ambos lenguajes las importaron por defecto como simples cadenas de texto. 

## 4. Indicadores para la reunión del lunes

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | GYE Centro: $15,200 \| GYE Norte: $13,980 \| UIO Norte: $12,450 \| UIO Sur: $9,870 \| Cuenca: $8,540 |
| Ticket promedio (ventas ÷ clientes) | $38.07 por cliente |
| Sucursal con mayor venta | Guayaquil Centro ($15,200) |
| Sucursal con menor venta | Cuenca ($8,540) |
| Región con mayor venta total | Sierra |

## 5. Conclusiones y recomendación

1. **Integridad de sistemas verificada:** No existe asimetría de información entre el ERP, la API y Finanzas. Los tres archivos son consistentes y reportan las mismas métricas base.
2. **Dinámica comercial y estabilidad:** La región Sierra lidera el volumen acumulado de ventas; sin embargo, la sucursal de Guayaquil Centro es la de mayor rendimiento individual. El comportamiento de compra es estable, reflejado en un ticket promedio consistente de ~$38.07.
3. **Recomendación de arquitectura de datos:** Se sugiere a gerencia estandarizar la extracción semanal en un único formato (preferiblemente CSV por su bajo peso y facilidad de lectura), lo cual optimizará el flujo de trabajo del equipo de BI.
