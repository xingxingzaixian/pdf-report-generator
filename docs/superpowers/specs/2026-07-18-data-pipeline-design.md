# Data Pipeline & Conditional Rendering Design

## Overview

Add inline data transformation pipelines and conditional/dynamic element rendering to the PDF report generator. This enables data cleaning, aggregation, and computed columns directly within JSON configurations, and allows elements to be conditionally shown or dynamically repeated based on processed data.

**Approach:** Lightweight inline pipelines (Option A) — minimal changes, seamless integration with existing architecture, future-evolvable.

## Goals

1. Support data transformation operations (filter, sort, compute, group, select, rename, concat, limit) within `dataSources[].pipeline`
2. Support conditional element rendering via `condition` attribute
3. Support dynamic element looping via `loop` attribute
4. Maintain full backward compatibility with existing configurations

## Pipeline Syntax

### Definition

Pipelines are defined as an optional `pipeline` array on each data source:

```json
{
  "dataSources": [{
    "name": "sales",
    "type": "csv",
    "path": "data/sales.csv",
    "pipeline": [
      {"op": "filter", "expr": "quantity > 100"},
      {"op": "compute", "columns": {"margin": "profit / revenue * 100"}},
      {"op": "sort", "by": "revenue", "order": "desc"},
      {"op": "select", "columns": ["product", "revenue", "margin"]},
      {"op": "group", "by": "category", "agg": {"total_revenue": "sum"}}
    ]
  }]
}
```

### Operations

| Operation | Syntax | Description |
|-----------|--------|-------------|
| `filter` | `{"op": "filter", "expr": "col > val"}` | Filter rows by expression |
| `sort` | `{"op": "sort", "by": "col", "order": "desc"}` | Sort by column |
| `compute` | `{"op": "compute", "columns": {"new": "expr"}}` | Add computed column |
| `group` | `{"op": "group", "by": "col", "agg": {"col": "func"}}` | Group and aggregate |
| `select` | `{"op": "select", "columns": ["col1"]}` | Select columns |
| `rename` | `{"op": "rename", "columns": {"old": "new"}}` | Rename columns |
| `concat` | `{"op": "concat", "sources": ["src1", "src2"]}` | Merge data sources |
| `limit` | `{"op": "limit", "n": 100}` | Take first N rows |

### Expression Engine

Uses a sandboxed Python expression evaluator:
- **Allowed:** Arithmetic (`+`, `-`, `*`, `/`, `%`, `**`), comparison (`>`, `<`, `>=`, `<=`, `==`, `!=`), logical (`and`, `or`, `not`), built-in functions (`sum`, `max`, `min`, `abs`, `len`, `round`)
- **Blocked:** `import`, `exec`, `eval`, `__builtins__`, file/network operations

## Conditional Rendering

### Condition Attribute

```json
{
  "type": "text",
  "content": "Warning: Negative profit this month!",
  "style": "warning",
  "condition": "dataSources.summary.total_profit < 0"
}
```

Condition expressions reference processed data sources via `dataSources.<name>.<column>` or `metadata.<field>`. If the expression evaluates to truthy, the element is included; otherwise it is skipped.

### Loop Attribute

```json
{
  "type": "chart",
  "loop": {
    "dataSource": "category_summary",
    "groupBy": "category"
  },
  "chartType": "bar",
  "title": "{{current.category}} Sales",
  "xAxis": "product",
  "yAxis": "quantity"
}
```

Loop iterates over each unique value of `groupBy` in the specified data source, generating one element copy per group. `{{current.xxx}}` references the current iteration's field values.

## Architecture

### New Module: `pipeline/`

```
pdf_generator/
├── pipeline/
│   ├── __init__.py
│   ├── engine.py        # Pipeline execution engine
│   ├── operations.py    # Operation implementations
│   └── expression.py    # Sandboxed expression evaluator
└── core/
    ├── generator.py     # Modified: integrate pipeline + conditional rendering
    └── elements.py      # Modified: support condition/loop
```

### Data Flow

```
JSON Config
    ↓
ConfigParser (recognizes pipeline, condition, loop fields)
    ↓
DataSource loads raw data → Pipeline Engine executes steps → processed DataFrame
    ↓
ElementFactory creates elements
    ↓
    ├─ condition eval → True/False → include or skip in story
    └─ loop expand → create element copies per group value, render {{current.xxx}}
    ↓
PDF Output
```

### Error Handling

1. **Pipeline step failure** — Raise `PipelineError` with step index and reason; display error in PDF
2. **Expression eval failure** — Skip step, print warning, continue with previous result
3. **Loop data source empty** — Skip loop, generate nothing
4. **Invalid condition expression** — Default to showing element (fail-open)

### Backward Compatibility

- `pipeline` field is optional; existing configs work unchanged
- Elements without `condition`/`loop` behave exactly as before
- No breaking changes to existing API or CLI

## Testing

1. **Unit tests** — Each pipeline operation (filter/sort/compute/group/select/rename/concat/limit)
2. **Expression evaluator** — Valid expressions, blocked dangerous ops, edge cases
3. **Integration tests** — Full pipeline + conditional rendering + loop → end-to-end PDF
4. **Edge cases** — Empty data sources, invalid expressions, loop with empty results

## Implementation Scope

- New files: `pipeline/__init__.py`, `pipeline/engine.py`, `pipeline/operations.py`, `pipeline/expression.py`
- Modified files: `core/generator.py`, `core/elements.py`, `config/parser.py`
- New dependency: None (uses existing pandas + ast.literal_eval)
- Estimated effort: 2-3 days
