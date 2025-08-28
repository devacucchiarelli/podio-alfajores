-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS alfajores_db;
USE alfajores_db;

-- Crear tabla de alfajores
CREATE TABLE IF NOT EXISTS alfajores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    votos INT DEFAULT 0
);

-- Dejarlo inicializado
INSERT INTO alfajores (nombre, votos) VALUES
('Havanna', 0),
('Guaymallén', 0),
('Jorgito', 0);
