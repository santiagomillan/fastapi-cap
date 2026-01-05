#!/bin/bash
# Script de build optimizado para Render
# Evita compilación de Rust/C usando wheels pre-compilados

set -o errexit

echo "📦 Actualizando pip, setuptools y wheel..."
pip install --upgrade pip setuptools wheel

echo "📥 Instalando dependencias desde wheels pre-compilados..."
pip install --only-binary=:all: -r requirements.txt || pip install -r requirements.txt

echo "✅ Build completado exitosamente!"
