"""
Script para probar la conexión a PostgreSQL
"""
from sqlalchemy import create_engine, text
from core.config import setting

def test_connection():
    print("🔍 Probando conexión a la base de datos...")
    print(f"📍 DATABASE_URL: {setting.DATABASE_URL[:20]}...") # Mostrar solo inicio por seguridad
    
    try:
        # Crear engine
        engine = create_engine(setting.DATABASE_URL)
        
        # Probar conexión
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.fetchone()[0]
            print("✅ Conexión exitosa!")
            print(f"📊 PostgreSQL Version: {version}")
            
        # Probar si existen las tablas
        with engine.connect() as connection:
            result = connection.execute(text("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """))
            tables = [row[0] for row in result]
            
            if tables:
                print(f"\n📋 Tablas existentes: {', '.join(tables)}")
            else:
                print("\n⚠️  No hay tablas creadas aún. Ejecuta: python init_db.py")
                
    except Exception as e:
        print("❌ Error de conexión:")
        print(f"   {str(e)}")
        print("\n💡 Verifica:")
        print("   1. La URL en .env está correcta")
        print("   2. La base de datos de Render está activa")
        print("   3. La URL empieza con 'postgresql://' (no 'postgres://')")

if __name__ == "__main__":
    test_connection()


# python test_connection.py