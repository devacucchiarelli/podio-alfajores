-- Crear base y usarla
CREATE DATABASE IF NOT EXISTS alfajores_db;
USE alfajores_db;

-- Reiniciar tabla (para asegurar el esquema correcto)
DROP TABLE IF EXISTS alfajores;
CREATE TABLE alfajores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(100),
    descripcion TEXT,
    imagen VARCHAR(255),
    votos INT DEFAULT 0
);

-- Datos de ejemplo completos
INSERT INTO alfajores (nombre, tipo, descripcion, imagen, votos) VALUES
('Havanna', 'Dulce de leche', 'Clásico con cobertura de chocolate semiamargo', '', 0),
('Guaymallén', 'Dulce de leche', 'Popular y económico', '', 0),
('Jorgito', 'Dulce de leche', 'De los históricos', '', 0);
