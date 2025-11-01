#!/usr/bin/env python3
"""Script para generar REPORTS.md localmente"""
import subprocess
import sys
from datetime import datetime
from pathlib import Path

def run_command(cmd: str):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=300)
        return result.returncode, result.stdout + result.stderr
    except:
        return -1, "ERROR"

def get_git_info():
    info = {}
    returncode, output = run_command("git rev-parse --abbrev-ref HEAD")
    info['branch'] = output.strip() if returncode == 0 else "unknown"
    returncode, output = run_command("git rev-parse HEAD")
    info['commit'] = output.strip()[:8] if returncode == 0 else "unknown"
    returncode, output = run_command("git log -1 --format='%an'")
    info['author'] = output.strip() if returncode == 0 else "unknown"
    return info

def generate_report():
    print("🔄 Generando REPORTS.md...")
    git_info = get_git_info()
    with open("REPORTS.md", "w", encoding="utf-8") as f:
        f.write("# 📊 Reporte de Tests y Cobertura\n\n")
        f.write(f"**Fecha:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Branch:** {git_info['branch']}\n")
        f.write(f"**Commit:** {git_info['commit']}\n")
        f.write(f"**Autor:** {git_info['author']}\n")
        f.write("\n---\n\n")
        f.write("## �� Resultados de Tests\n\n```\n")
        print("  ▶️  Ejecutando tests...")
        returncode, output = run_command("pytest --tb=short -v")
        f.write(output)
        f.write("\n```\n\n---\n\n")
        f.write("## 📈 Cobertura de Código\n\n```\n")
        print("  ▶️  Generando cobertura...")
        returncode, output = run_command("pytest --cov=core --cov=cli --cov=ui --cov-report=term-missing")
        lines = output.split('\n')
        f.write('\n'.join(lines[-30:]))
        f.write("\n```\n\n---\n\n")
        f.write("## 📄 Archivos Generados\n\n")
        f.write("- `htmlcov/index.html` - Reporte HTML\n")
        f.write("- `coverage.xml` - XML para Codecov\n\n---\n\n")
        f.write("**Generado localmente** 💻\n")
    print("✅ REPORTS.md generado exitosamente")
    print("�� Ver reporte HTML en: htmlcov/index.html")

def main():
    print("=" * 60)
    print("🚀 Generador de REPORTS.md - Backgammon")
    print("=" * 60)
    print()
    if not Path("pytest.ini").exists():
        print("❌ ERROR: No se encontró pytest.ini")
        print("   Ejecuta este script desde la raíz del proyecto")
        sys.exit(1)
    try:
        generate_report()
        print("\n" + "=" * 60)
        print("✅ Proceso completado exitosamente")
        print("=" * 60)
        return 0
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
