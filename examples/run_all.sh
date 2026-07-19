#!/bin/bash
# ============================================================
# PDF Report Generator - 批量运行所有示例
#
# 用法:
#   bash examples/run_all.sh            # 运行全部
#   bash examples/run_all.sh L1         # 只运行 L1
#   bash examples/run_all.sh pipeline   # 只运行 pipeline 相关
#   bash examples/run_all.sh --skip-api # 跳过 API 相关示例
# ============================================================

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
OUTPUT_DIR="$SCRIPT_DIR/output"
VENV_PYTHON="$PROJECT_DIR/.venv/bin/python"

# 自动检测 Python
if [ -f "$VENV_PYTHON" ]; then
    PYTHON="$VENV_PYTHON"
elif command -v uv &> /dev/null; then
    PYTHON="uv run python"
elif command -v python3 &> /dev/null; then
    PYTHON="python3"
else
    PYTHON="python"
fi

# 颜色
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

PASS=0
FAIL=0
SKIP=0

# 所有示例（按编号顺序）
ALL_EXAMPLES=(
    # L1 快速入门
    "01_hello_pdf.py"
    "02_text_styles.py"
    "03_simple_table.py"
    # L2 数据源
    "04_data_csv.py"
    "05_data_json.py"
    "06_data_excel.py"
    "07_data_dataframe.py"
    "08_data_api.py"
    # L3 可视化
    "09_chart_bar.py"
    "10_chart_line_pie.py"
    "11_image.py"
    # L4 文档结构
    "12_header_footer.py"
    "13_page_number.py"
    "14_toc.py"
    "15_cover_page.py"
    "16_page_break.py"
    # L5 高级表格
    "17_table_merge.py"
    "18_table_alignment.py"
    "19_table_layout.py"
    "20_table_style_variants.py"
    # L6 Pipeline
    "21_pipeline_filter.py"
    "22_pipeline_transform.py"
    "23_pipeline_aggregate.py"
    "24_pipeline_full_workflow.py"
    # L7 综合报告
    "25_comprehensive_sales.py"
    "26_comprehensive_financial.py"
    "27_comprehensive_project.py"
    # 专题
    "28_font_auto_detect.py"
    "29_font_custom_register.py"
    "30_api_client.py"
)

# 过滤逻辑
# 支持: L1-L7, topic, font, pipeline, table, chart, data, comprehensive, api
# 也支持直接输入文件名的关键词（如 01, hello, csv）
FILTER=""
SKIP_API=false

for arg in "$@"; do
    case $arg in
        --skip-api) SKIP_API=true ;;
        L1) FILTER="0[1-3]" ;;
        L2) FILTER="0[4-8]" ;;
        L3) FILTER="09|10|11" ;;
        L4) FILTER="1[2-6]" ;;
        L5) FILTER="1[7-9]|20" ;;
        L6) FILTER="2[1-4]" ;;
        L7) FILTER="2[5-7]" ;;
        topic) FILTER="28|29|30" ;;
        font) FILTER="font" ;;
        pipeline) FILTER="pipeline" ;;
        table) FILTER="table" ;;
        chart) FILTER="chart" ;;
        data) FILTER="data" ;;
        comprehensive) FILTER="comprehensive" ;;
        api) FILTER="api" ;;
        *) FILTER="$arg" ;;
    esac
done

run_example() {
    local file="$1"
    local path="$SCRIPT_DIR/$file"

    if [ ! -f "$path" ]; then
        echo -e "${RED}  ✗ 文件不存在: $file${NC}"
        FAIL=$((FAIL + 1))
        return
    fi

    # 跳过 API 相关
    if $SKIP_API && [[ "$file" == *"api"* ]]; then
        echo -e "${YELLOW}  ⊘ 跳过: $file${NC}"
        SKIP=$((SKIP + 1))
        return
    fi

    printf "  %-45s " "$file"
    if $PYTHON "$path" > /dev/null 2>&1; then
        echo -e "${GREEN}✓${NC}"
        PASS=$((PASS + 1))
    else
        echo -e "${RED}✗${NC}"
        FAIL=$((FAIL + 1))
    fi
}

echo ""
echo -e "${CYAN}============================================================${NC}"
echo -e "${CYAN}  PDF Report Generator - 批量运行示例${NC}"
echo -e "${CYAN}============================================================${NC}"
echo ""

mkdir -p "$OUTPUT_DIR"

TOTAL=0
for file in "${ALL_EXAMPLES[@]}"; do
    # 如果指定了过滤条件，用 grep 正则匹配
    if [ -n "$FILTER" ]; then
        echo "$file" | grep -qE "$FILTER" || continue
    fi
    run_example "$file"
    TOTAL=$((TOTAL + 1))
done

echo ""
echo -e "${CYAN}------------------------------------------------------------${NC}"
echo -e "  总计: $TOTAL  |  ${GREEN}通过: $PASS${NC}  |  ${RED}失败: $FAIL${NC}  |  ${YELLOW}跳过: $SKIP${NC}"
echo -e "${CYAN}------------------------------------------------------------${NC}"
echo -e "  输出目录: ${OUTPUT_DIR}/"
echo ""

# 退出码
if [ $FAIL -gt 0 ]; then
    exit 1
fi
