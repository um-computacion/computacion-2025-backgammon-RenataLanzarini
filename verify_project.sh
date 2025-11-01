#!/bin/bash

echo "====================================="
echo "VERIFICACIÓN COMPLETA DEL PROYECTO"
echo "====================================="

# 1. Archivos obligatorios
echo -e "\n[1/13] Verificando archivos obligatorios..."
files=(README.md CHANGELOG.md JUSTIFICACION.md requirements.txt .pylintrc Dockerfile)
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "❌ FALTA: $file"
    fi
done

# Prompts
for prompt in prompts-desarrollo.md prompts-testing.md prompts-documentacion.md; do
    if [ -f "$prompt" ]; then
        echo "✅ $prompt"
    else
        echo "❌ FALTA: $prompt"
    fi
done

# 2. Estructura
echo -e "\n[2/13] Verificando estructura..."
dirs=(core cli pygame_ui tests)
for dir in "${dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/"
    else
        echo "❌ FALTA: $dir/"
    fi
done

# 3. Tests
echo -e "\n[3/13] Ejecutando tests..."
if command -v pytest &> /dev/null; then
    pytest tests/ --tb=short -q 2>&1 | tail -3
else
    echo "⚠️  pytest no instalado"
fi

# 4. Cobertura
echo -e "\n[4/13] Verificando cobertura..."
if command -v pytest &> /dev/null; then
    pytest tests/ --cov=core --cov-report=term 2>&1 | grep "TOTAL\|core"
else
    echo "⚠️  pytest no instalado"
fi

# 5. Pylint
echo -e "\n[5/13] Verificando calidad (Pylint)..."
if command -v pylint &> /dev/null; then
    pylint core/ --score=yes 2>&1 | tail -1
else
    echo "⚠️  pylint no instalado"
fi

# 6. Docker
echo -e "\n[6/13] Verificando Docker..."
if [ -f "Dockerfile" ]; then
    echo "✅ Dockerfile existe"
    if [ -f "docker-compose.yml" ]; then
        echo "✅ docker-compose.yml existe"
    else
        echo "⚠️  docker-compose.yml no existe (opcional pero recomendado)"
    fi
else
    echo "❌ FALTA: Dockerfile"
fi

# 7. Commits
echo -e "\n[7/13] Verificando commits..."
commit_count=$(git log --oneline 2>/dev/null | wc -l)
echo "Total commits: $commit_count (mínimo: 60)"
if [ $commit_count -ge 60 ]; then
    echo "✅ Commits suficientes"
elif [ $commit_count -ge 40 ]; then
    echo "⚠️  Tienes $commit_count commits (recomendado: 60+)"
else
    echo "❌ Solo $commit_count commits (necesitas más)"
fi

# Commits por fecha
echo -e "\nDistribución de commits por fecha:"
git log --pretty=format:"%ad" --date=short 2>/dev/null | sort | uniq -c | tail -5

# 8. Atributos con __
echo -e "\n[8/13] Verificando formato de atributos..."
bad_attrs=$(grep -rn "self\.[a-z]" core/ cli/ pygame_ui/*.py 2>/dev/null | grep -v "self\.__" | grep -v "self\.get_" | grep -v "self\.set_" | grep "self\.[a-z]" | wc -l)
if [ $bad_attrs -eq 0 ]; then
    echo "✅ Todos los atributos con formato __atributo__"
else
    echo "⚠️  Posibles $bad_attrs atributos sin formato correcto"
    echo "   (Revisar manualmente - pueden ser falsos positivos)"
fi

# 9. README contenido
echo -e "\n[9/13] Verificando README.md..."
if grep -q -i "docker" README.md 2>/dev/null; then
    echo "✅ README menciona Docker"
else
    echo "⚠️  README no menciona Docker"
fi

if grep -q -i "instalación\|install" README.md 2>/dev/null; then
    echo "✅ README tiene instrucciones de instalación"
else
    echo "⚠️  README falta instalación"
fi

# 10. CHANGELOG formato
echo -e "\n[10/13] Verificando CHANGELOG.md..."
if [ -f "CHANGELOG.md" ]; then
    if grep -q "Sprint\|Added\|Changed" CHANGELOG.md; then
        echo "✅ CHANGELOG.md con formato correcto"
    else
        echo "⚠️  CHANGELOG.md sin formato keepachangelog"
    fi
else
    echo "❌ FALTA: CHANGELOG.md"
fi

# 11. JUSTIFICACION contenido
echo -e "\n[11/13] Verificando JUSTIFICACION.md..."
if [ -f "JUSTIFICACION.md" ]; then
    checks=0
    grep -q -i "diseño" JUSTIFICACION.md && ((checks++)) && echo "✅ Diseño general"
    grep -q -i "clases" JUSTIFICACION.md && ((checks++)) && echo "✅ Justificación clases"
    grep -q -i "SOLID" JUSTIFICACION.md && ((checks++)) && echo "✅ Principios SOLID"
    grep -q -i "testing\|cobertura" JUSTIFICACION.md && ((checks++)) && echo "✅ Testing"
    grep -q -i "UML\|diagrama" JUSTIFICACION.md && ((checks++)) && echo "✅ Diagrama UML"
    
    if [ $checks -lt 5 ]; then
        echo "⚠️  JUSTIFICACION.md incompleto ($checks/5 secciones)"
    fi
else
    echo "❌ FALTA: JUSTIFICACION.md"
fi

# 12. Archivos de reportes
echo -e "\n[12/13] Verificando archivos de evidencia..."
evidence_files=(pylint_report_core.txt pylint_summary.txt reports.md)
for file in "${evidence_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file"
    else
        echo "⚠️  Falta: $file"
    fi
done

# 13. Branch protection
echo -e "\n[13/13] Verificando Git..."
current_branch=$(git branch --show-current 2>/dev/null)
echo "Branch actual: $current_branch"
if [ "$current_branch" = "main" ] || [ "$current_branch" = "master" ]; then
    echo "✅ En branch principal"
else
    echo "⚠️  No estás en main/master"
fi

echo -e "\n====================================="
echo "TAREAS MANUALES PENDIENTES:"
echo "====================================="
echo "☐ Verificar que CLI funciona: python -m cli.cli"
echo "☐ Verificar que Pygame funciona: python -m pygame_ui.ui"
echo "☐ Verificar regla de protección MAIN en GitHub"
echo "☐ Verificar archivos prompts-*.md tienen contenido real"
echo "☐ Verificar JUSTIFICACION.md tiene diagrama UML"

echo -e "\n====================================="
echo "VERIFICACIÓN COMPLETADA"
echo "====================================="
